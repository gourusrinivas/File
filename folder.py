import os

directory = '/Plan'

os.system("find " + directory + " -mtime +60 -print")
os.system("find " + directory + " -mtime +60 -delete")
