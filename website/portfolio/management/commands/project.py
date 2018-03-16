import json
import os
import sys

from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    
    help = 'Populate database with prepared data, Specify the file path or directory, expecting markdown formatted data'

    def add_arguments(self, parser):
    
        parser.add_argument(
            '--sql',
            required=False,
            choices=["flush", "printall"],
            dest='sql',
            help='Specify action',
        )

        parser.add_argument(
            '--addproject',
            required=False,
            dest='addproject',
            help='specify project file path to add to database',
        )

    def convert_ipynb_file_to_markdown(self, fp):
        self.stdout.write("convert_ipynb_file_to_markdown : File path specified is : %s" %fp)
        try :
            if fp.endswith(".ipynb") :
                fname = os.path.realpath(fp)
                self.stdout.write("convert_ipynb_file_to_markdown : File realpath specified is : %s" %fname)
                os.system("jupyter nbconvert --to markdown {}".format(fname))
        except Exception as er:
            print(str(er))


    def convert_markdown_file_to_json(self, fp):
        
        new_fname = ""
        try :
            if fp.endswith(".md") or fp.endswith(".markdown"): 
                fname = os.path.realpath(fp)
                new_fname = "%s.json" %fname
                os.system("md_to_json -o {} {}".format(new_fname,fname))
        except Exception as er:
            print(str(er))

        return new_fname

    #convert all markdown files in directory
    def convert_files_in_directory(self, dp):
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
            self.stdout.write(str(er))
        
        return file_content
    
    def load_file_content_to_db(self, fp):
        """ Take a path to markdown file,
            convert it to json
            then add content to Project db table
        """
       
        new_fname = self.convert_markdown_file_to_json(fp)

        file_content = self.parse_json_file(new_fname)
        if file_content:                
            proj = Project(**file_content)
            proj.save()
            

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
            self.load_file_content_to_db(os.path.join(dp, filename))



    def clean_useless_files_in_directory(self, dp):
        try:
            for file in os.listdir(os.path.realpath(dp)):
                if file.endswith(".md") or file.endswith(".md.json") or file.endswith(".json"):
                    os.remove(os.path.join(dp, file))
                    self.stdout.write("The following file is delected %s" %file)
        except Exception as er:
            self.stdout.write(str(er))


    # sql action

    def delete_everything(self):
        Project.objects.all().delete()
    
    # sql action
    
    def print_everything(self):
        projs = Project.objects.all()
        self.stdout.write("Total results %s" %len(projs))
        for proj in projs:
            self.stdout.write(str(proj.title))
            
            
    def handle(self, *args, **options):
        sql_action = options['sql']

        if str(sql_action) == "flush":
            self.delete_everything()
        
        if str(sql_action) == "printall":
            self.print_everything()

        fp = options['addproject']
        if fp:
            if os.path.isdir(fp):
                self.load_directory_files_to_db(fp)
                self.clean_useless_files_in_directory(fp)
            elif os.path.isfile(fp): #expect a markdown format in this case
                self.load_file_content_to_db(fp)
                self.clean_useless_files_in_directory(os.path.realpath(os.path.dirname(fp)))
