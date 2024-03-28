# add file structure for creating files
import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name="text_summarizer"

#it will help in ci cd deployment, automatically create the files
list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",   
    f"src/{project_name}/entity/__init__.py",  
    f"src/{project_name}/constants/__init__.py",  
    "config/config.yaml/"
    "params.yaml"
    "app.py",
    "main.py",
    "Docker",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory:{filedir} for the file{filename}")

    #to check if file not exists or file size is zero
    if(not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        pass #only for creating the file and not to make any changes
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
    




