import shutil
import datetime
import os

def  backup_files(source_dir, backup_dir):
  today = datetime.datetime.today()
  backup_file_name = os.path.join(backup_dir, f"backup_{today}tag.gz")
  shutil.make_archive(backup_file_name.replace("tar.gz",''),'gztar',source_dir)

source_directory = input("Enter the source directory to backup: ")
backup_directory = input("Enter the backup directory: ")      
backup_files(source_directory, backup_directory)


