import json
import os
import sys

import yaml
from django.core.management.base import BaseCommand

from apps.resume.models import (Biography, Language, Education, Experience, Skill, Interest)
from apps.projects.models import Project


class Command(BaseCommand):
    
    help = 'Populate database with prepared data, Specify the file path or directory'

    def add_arguments(self, parser):
        
        parser.add_argument(
            '--db',
            required=False,
            choices=["flush", "select"],
            dest='database',
            help='specify database action, flush or select',
        )

        parser.add_argument(
            '--addjupyter',
            required=False,
            dest='jupyter_dir',
            help='specify path to jupyter notebooks folder',
        )


        parser.add_argument(
            '--addmarkdown',
            required=False,
            dest='markdown_file',
            help='specify path to markdown file',
        )

        parser.add_argument(
            '--addyaml',
            required=False,
            dest='yaml_file',
            help='specify path to yaml file',
        )

        parser.add_argument(
            '--model',
            required=True,
            dest='model',
            choices=["biography", "language", "education", "experience", "skill", "interest", "project"],
            help='specify object type',
        )

    
    def handle(self, *args, **options):
    
        model = options['model']

        jupyter_dir = options['jupyter_dir']
        markdown_file = options['markdown_file']
        yaml_file = options['yaml_file']
        database = options['database']

        if str(database) == "flush":
            self.db_flush(model)
        
        if str(database) == "select":
            self.db_select(model)

        if jupyter_dir:
            if os.path.isdir(jupyter_dir):
                self.commit_ipynb_dir(jupyter_dir, model)
                self.clean_ipynb_dir(jupyter_dir)
            else:
                self.stdout.write("You should specify an accessible directory path, check permissions")

        if markdown_file:
            if os.path.isfile(markdown_file):
                self.commit_markdown_file(markdown_file, model)
                self.clean_ipynb_dir(os.path.realpath(os.path.dirname(markdown_file)))
            else:
                self.stdout.write("You should specify an accessible markdown file path, check permissions")

        if yaml_file:
            if os.path.isfile(yaml_file):
                self.commit_yaml_file(yaml_file, model)
            else:
                self.stdout.write("You should specify an accessible YAML file path, check permissions")


    
    def commit_database(self, file_content, model):
        if model == "biography":              
            biography = Biography(**file_content)
            biography.save()
        if model == "language":
            language = Language(**file_content)
            language.save()
        if model == "education":
            education = Education(**file_content)
            education.save()
        if model == "experience":
            experience = Experience(**file_content)
            experience.save()
        if model == "skill":
            skill = Skill(**file_content)
            skill.save()
        if model == "interest":
            interest = Interest(**file_content)
            interest.save()
        if model == "project":
            project = Project(**file_content)
            project.save()

    def commit_markdown_file(self, fp, model):
        """ Take a path to markdown file,
            convert it to dict
            then add content to db table
        """
       
        new_fname = self.markdown_to_json(fp)
        file_content = self.json_to_dict(new_fname)
        if file_content:
            self.commit_database(file_content, model)


    def commit_yaml_file(self, fp, model):
        """ Take a path to a yaml file,
            convert it to dict
            then add content to db table
        """
        try:
            if os.path.isfile(fp):
                with open(fp, "r") as fp_yaml:
                    file_content = yaml.safe_load(fp_yaml)
                    if file_content:
                        self.commit_database(file_content, model)   
        except Exception as er:
            self.stdout.write(str(er))



    def commit_ipynb_dir(self, dp, model):
        """ Take a path to jupyter notebooks directory,
        
        list all ipynb files in it and convert to markdown
            then convert markdown files to json
            then add json files content to db table
        """

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.stdout.write("Converting all ipynb files to markdown format")
            self.ipynb_to_markdown(os.path.join(dp, filename))

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.commit_markdown_file(os.path.join(dp, filename), model)


    def ipynb_to_markdown(self, fp):
        try :
            if fp.endswith(".ipynb"):
                fname = os.path.realpath(fp)
                os.system("jupyter nbconvert --to markdown {}".format(fname))
        except Exception as er:
            self.stdout.write(str(er))


    def markdown_to_json(self, fp):
        
        new_fname = ""
        try :
            if fp.endswith(".md") or fp.endswith(".markdown"): 
                fname = os.path.realpath(fp)
                new_fname = "%s.json" %fname
                os.system("md_to_json -o {} {}".format(new_fname,fname))
        except Exception as er:
            self.stdout.write(str(er))

        return new_fname


    def json_to_dict(self, fp):
        
        self.stdout.write('Start parsing the file')
        file_content = ""
        try: 
            if os.path.isfile(fp) and fp.endswith(".md.json"):
                self.stdout.write("File path specified is : %s" %fp)
                with open(fp, "r+") as file_path:
                    file_content = json.load(file_path)
                    self.stdout.write(str(file_content.keys())) 
            else :
                self.stdout.write("You should specify a real file path and json format expected")

        except Exception as er:
            self.stdout.write(str(er))
        
        return file_content
    

    def clean_ipynb_dir(self, dp):
        try:
            for file in os.listdir(os.path.realpath(dp)):
                if file.endswith(".md") or file.endswith(".md.json") or file.endswith(".json"):
                    os.remove(os.path.join(dp, file))
                    self.stdout.write("The following file is delected %s" %file)
        except Exception as er:
            self.stdout.write(str(er))


    def db_flush(self, model):
        if model == "biography":
            Biography.objects.all().delete()
        if model == "language":
            Language.objects.all().delete()
        if model == "education":
            Education.objects.all().delete()
        if model == "experrience":
            Experience.objects.all().delete()
        if model == "skill":
            Skill.objects.all().delete()
        if model == "interest":
            Interest.objects.all().delete()
        if model == "project":
            Project.objects.all().delete()


    def db_select(self, model):
        if model == "biography":
            biography = Biography.objects.all()
            self.stdout.write("Found %s biography" %(len(biography)))
            for p in biography:
                self.stdout.write(str(p))
        if model == "language":
            languages = Language.objects.all()
            self.stdout.write("Found %s languages" %(len(languages)))
            for p in languages:
                self.stdout.write(str(p))
        if model == "education":
            educations = Education.objects.all()
            self.stdout.write("Found %s educations" %(len(educations)))
            for p in educations:
                self.stdout.write(str(p))
        if model == "experience":
            experiences = Experience.objects.all()
            self.stdout.write("Found %s experiences" %(len(experiences)))
            for p in experiences:
                self.stdout.write(str(p))
        if model == "skill":
            skills = Skill.objects.all()
            self.stdout.write("Found %s skills" %(len(skills)))
            for p in skills:
                self.stdout.write(str(p))
        if model == "interest":
            interests = Interest.objects.all()
            self.stdout.write("Found %s interests" %(len(interests)))
            for p in interests:
                self.stdout.write(str(p))
        if model == "project":
            projects = Project.objects.all()
            self.stdout.write("Found %s projects" %(len(projects)))
            for p in projects:
                self.stdout.write(str(p))


    