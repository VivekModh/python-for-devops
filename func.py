import os
import datetime

def myfunc(command):
  return os.system(command)

def showdate(command):
  return datetime.datetime.today()

today = showdate("date")
print(today)

