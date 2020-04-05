import json
import os
import sys

import yaml
from django.core.management.base import BaseCommand

from apps.projects.models import Project


class Command(BaseCommand):
    
    help = 'Populate database with prepared data, Specify the file path or directory'

    def add_arguments(self, parser):
    
        parser.add_argument(
            '--db',
            required=False,
            choices=["flush", "select"],
            dest='database',
            help='Specify action',
        )

        parser.add_argument(
            '--addjupyter',
            required=False,
            dest='jupyter_dir',
            help='specify path to folder with jupyter notebooks',
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

    def convert_ipynb_file_to_markdown(self, fp):
        self.stdout.write("convert_ipynb_file_to_markdown : File path specified is : %s" %fp)
        try :
            if fp.endswith(".ipynb") :
                fname = os.path.realpath(fp)
                self.stdout.write("convert_ipynb_file_to_markdown : File realpath specified is : %s" %fname)
                os.system("jupyter nbconvert --to markdown {}".format(fname))
        except Exception as er:
            self.stderr.write(str(er))


    def convert_markdown_file_to_json(self, fp):
        
        new_fname = ""
        try :
            if fp.endswith(".md") or fp.endswith(".markdown"): 
                fname = os.path.realpath(fp)
                new_fname = "%s.json" %fname
                os.system("md_to_json -o {} {}".format(new_fname,fname))
        except Exception as er:
            self.stderr.write(str(er))

        return new_fname


    def convert_markdown_files_in_dir(self, dp):
        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            convert_markdown_file_to_json(os.path.join(dp, filename))


    def parse_json_file(self, fp):
        
        self.stdout.write('parse_json_file : Start parsing the file')
        self.stdout.write("parse_json_file : File path specified is : %s" %fp)
        file_content = ""
        try: 
            if os.path.isfile(fp) and fp.endswith(".md.json"):
                self.stdout.write("parse_json_file : Correct File path specified is : %s" %fp)
                with open(fp, "r+") as file_path:
                    file_content = json.load(file_path)

                    self.stdout.write(str(file_content.keys())) 
            else :
                self.stdout.write("parse_json_file : You should specify a real file path and json format expected")

        except Exception as er:
            self.stderr.write(str(er))
        
        return file_content
    
    def load_markdown_file_content_to_db(self, fp):
        """ Take a path to markdown file,
            convert it to json
            then add content to Project table
        """
       
        new_fname = self.convert_markdown_file_to_json(fp)

        file_content = self.parse_json_file(new_fname)
        if file_content:                
            proj = Project(**file_content)
            proj.save()
            
    def load_yaml_file_content_to_db(self, fp):
        """ Take a path to a yaml file,
            then add content to Project table
        """
        try:
            if os.path.isfile(fp):
                with open(fp, "r") as fp_yaml:
                    file_content = yaml.safe_load(fp_yaml)
                    if file_content:                
                        proj = Project(**file_content)
                        proj.save()
        except Exception as er:
            self.stderr.write(str(er))

    def load_directory_files_to_db(self, dp):
        """ Take a path to a directory,
        list all ipynb files in it and convert to markdown
        then convert markdown files to json
        then add json content to Project db table
        """

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.stdout.write("Converting all ipynb files to markdown format")
            self.convert_ipynb_file_to_markdown(os.path.join(dp, filename))

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.load_markdown_file_content_to_db(os.path.join(dp, filename))



    def clean_useless_files_in_directory(self, dp):
        try:
            for file in os.listdir(os.path.realpath(dp)):
                if file.endswith(".md") or file.endswith(".md.json") or file.endswith(".json"):
                    os.remove(os.path.join(dp, file))
                    self.stdout.write("The following file is delected %s" %file)
        except Exception as er:
            self.stderr.write(str(er))


    def delete_everything(self):
        Project.objects.all().delete()


    def print_everything(self):
        projs = Project.objects.all()
        self.stdout.write("Total results %s" %len(projs))
        for proj in projs:
            self.stdout.write(str(proj.title))
            
            
    def handle(self, *args, **options):

        database = options['database']
        jupyter_dir = options['jupyter_dir']
        markdown_file = options['markdown_file']
        yaml_file = options['yaml_file']


        if str(database) == "flush":
            self.delete_everything()
        
        if str(database) == "select":
            self.print_everything()

        if jupyter_dir:
            if os.path.isdir(jupyter_dir):
                self.load_directory_files_to_db(jupyter_dir)
                self.clean_useless_files_in_directory(jupyter_dir)
            else:
                self.stdout.write("You should specify an accessible directory path, check permissions")

        if markdown_file:
            if os.path.isfile(markdown_file):
                self.load_markdown_file_content_to_db(markdown_file)
                self.clean_useless_files_in_directory(os.path.realpath(os.path.dirname(markdown_file)))
            else:
                self.stdout.write("You should specify an accessible markdown file path, check permissions")

        if yaml_file:
            if os.path.isfile(yaml_file):
                self.load_yaml_file_content_to_db(yaml_file)
            else:
                self.stdout.write("You should specify an accessible YAML file path, check permissions")
