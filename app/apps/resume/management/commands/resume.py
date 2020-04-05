import json
import os
import sys

import yaml
from django.core.management.base import BaseCommand

from apps.resume.models import Biography


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

        parser.add_argument(
            '--model',
            required=True,
            dest='model',
            help='specify data type, django model',
        )


    def convert_ipynb_file_to_markdown(self, fp):
        try :
            if fp.endswith(".ipynb") :
                fname = os.path.realpath(fp)
                os.system("jupyter nbconvert --to markdown {}".format(fname))
        except Exception as er:
            self.stdout.write(str(er))


    def convert_markdown_file_to_json(self, fp):
        
        new_fname = ""
        try :
            if fp.endswith(".md") or fp.endswith(".markdown"): 
                fname = os.path.realpath(fp)
                new_fname = "%s.json" %fname
                os.system("md_to_json -o {} {}".format(new_fname,fname))
        except Exception as er:
            self.stdout.write(str(er))

        return new_fname

    def convert_markdown_files_in_dir(self, dp):
        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            convert_markdown_file_to_json(os.path.join(dp, filename))


    def parse_json_file(self, fp):
        
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
    
    def load_markdown_file_content_to_db(self, fp, datatype):
        """ Take a path to markdown file,
            convert it to json
            then add content to db table
        """
       
        new_fname = self.convert_markdown_file_to_json(fp)

        file_content = self.parse_json_file(new_fname)
        if file_content: 
            if datatype == "Biography":              
                personal_info = Biography(**file_content)
                personal_info.save()
            #TODO:
            #Add other subcases, (Skills, Education, Work Experience) for the API


    def load_yaml_file_content_to_db(self, fp, datatype):
        """ Take a path to a yaml file,
            then add content to db table
        """
        try:
            if os.path.isfile(fp):
                with open(fp, "r") as fp_yaml:
                    file_content = yaml.safe_load(fp_yaml)
                    if file_content: 
                        if datatype == "Biography":              
                            biography = Biography(**file_content)
                            biography.save()
                        #TODO:
                        #Add other subcases, (Skills, Education, Work Experience) for the API
        except Exception as er:
            self.stdout.write(str(er))

    def load_directory_files_to_db(self, dp, datatype):
        """ Take a path to a directory,
        
        list all ipynb files in it and convert to markdown
        then convert markdown files to json
        then add json content to db table
        """

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.stdout.write("Converting all ipynb files to markdown format")
            self.convert_ipynb_file_to_markdown(os.path.join(dp, filename))

        for file in os.listdir(os.path.realpath(dp)):
            filename = os.fsdecode(file)
            self.load_markdown_file_content_to_db(os.path.join(dp, filename), datatype)



    def clean_useless_files_in_directory(self, dp):
        try:
            for file in os.listdir(os.path.realpath(dp)):
                if file.endswith(".md") or file.endswith(".md.json") or file.endswith(".json"):
                    os.remove(os.path.join(dp, file))
                    self.stdout.write("The following file is delected %s" %file)
        except Exception as er:
            self.stdout.write(str(er))


    # sql action
    def delete_everything(self, datatype):
        
        if datatype == "Biography":
            Biography.objects.all().delete()
    
    
    def print_everything(self, datatype):
        
        if datatype == "Biography":
            personal_infos = Biography.objects.all()
            self.stdout.write("Total results %s" %len(personal_infos))
            for p in personal_infos:
                self.stdout.write(str(p))
                    
    def handle(self, *args, **options):

        model = options['model']
        jupyter_dir = options['jupyter_dir']
        markdown_file = options['markdown_file']
        yaml_file = options['yaml_file']


        database = options['database']

        if str(database) == "flush":
            self.delete_everything(model)
        
        if str(database) == "select":
            self.print_everything(model)

        if jupyter_dir:
            if os.path.isdir(jupyter_dir):
                self.load_directory_files_to_db(jupyter_dir, model)
                self.clean_useless_files_in_directory(jupyter_dir)
            else:
                self.stdout.write("You should specify an accessible directory path, check permissions")


        if markdown_file:
            if os.path.isfile(markdown_file):
                self.load_markdown_file_content_to_db(markdown_file, model)
                self.clean_useless_files_in_directory(os.path.realpath(os.path.dirname(markdown_file)))
            else:
                self.stdout.write("You should specify an accessible markdown file path, check permissions")

        
        if yaml_file:
            if os.path.isfile(yaml_file):
                self.load_yaml_file_content_to_db(yaml_file, model)
        else:
            self.stdout.write("You should specify an accessible YAML file path, check permissions")
