""" Program to get system command output"""
import subprocess                       # using subprocess module
result = subprocess.check_output("dir", shell=True, universal_newlines=True)     # output storing in result
print("dir command to list file and directory")
print(result)           # showing result


