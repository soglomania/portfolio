#-*-coding:utf-8-*-
#!/usr/bin/env python
import sys
import os
import json

def convert_file(fp):
    try :
        if fp.endswith(".md") or fp.endswith(".markdown"): 
            fname = os.path.realpath(fp)
            new_fname = "%s.json" %fname
            os.system("md_to_json -o {} {}".format(new_fname,fname))
    except Exception as er:
        print(str(er))


def convert_files_in_directory(dp):
    for file in os.listdir(os.path.realpath(dp)):
        filename = os.fsdecode(file)
        convert_file(os.path.join(dp, filename))


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(path)
        if os.path.isdir(path):
            convert_files_in_directory(path)
        elif os.path.isfile(path):
            convert_file(path)