"""Program to get the command-line arguments (name of the script, the number of arguments, arguments)
passed to a script"""
import sys

print(f'Script name: {sys.argv[0]}')        # sys.argv is list of arguments
print(f' No of arguments: {len(sys.argv)}')              # sys.argv[0] is script name
print(f'Arguments: {sys.argv}')
