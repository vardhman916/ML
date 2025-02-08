import os  #The os module lets you interact with the operating system.
from pathlib import Path
import logging
#The logging module is used to track events in a program.

logging.basicConfig(level = logging.INFO)
'''DEBUG → Log everything (like CCTV watching everything).
INFO → Log important events (like when doors open).
WARNING → Log potential issues (like smoke detected).
ERROR → Log serious issues (like fire detected).
CRITICAL → Log critical failures (like building collapse!).
By setting logging.basicConfig(level=logging.INFO), 
we ignore DEBUG messages but keep INFO, WARNING, ERROR, CRITICAL.'''

project_name = 'ML'

list_of_file = [
             f"src/__init__.py",
             f"src/{project_name}/__init__.py",
             f"src/{project_name}/components/__init__.py",
             f"src/{project_name}/components/data_ingestion.py",
             f"src/{project_name}/components/data_transformation.py",
             f"src/{project_name}/components/model_trainer.py",
             f"src/{project_name}/components/model_monitering.py",
             f"src/{project_name}/pipelines/__init__.py",
             f"src/{project_name}/pipelines/training_pipeline.py",
             f"src/{project_name}/pipelines/prediction_pipeline.py",
             f"src/{project_name}/exception.py",
             f"src/{project_name}/logger.py",
             f"src/{project_name}/pipelines/utils.py",
             "app.py",
             "Dockerfile"
]

for filepath in list_of_file:
    filepath = Path(filepath)  #string to path
    filedir,filename = os.path.split(filepath)  #Split the path into directory and file name

    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"Creating directory:{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f: #If filepath does NOT exist, Python automatically creates a new file with the given filename.
            pass#pass ensures the file remains empty.
            logging.info(f"Crating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")