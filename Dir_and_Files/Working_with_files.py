from pathlib import Path
from os import path

print('os:', path.curdir) # current working directory

print('os:', path.abspath('.')) # absolute path of current working directory


my_dir = Path('.')
print('Path:', my_dir)
print('Path', my_dir.absolute())
other_dir = Path('Dir_and_Files')
if not other_dir.exists():
   other_dir.mkdir()
# if other_dir.exists():
#       other_dir.rmdir()






with open('test.txt', 'w') as test_file:
     test_file.write('First string.\n')
     test_file.write('Second string.\n')
     test_file.write('Third string.\n')

with open('test.txt') as test_file:
      print(test_file.read())

with open('test.txt') as test_file:
     lines = test_file.readlines()
     for line in lines:
         print(line)


with open('test.txt', 'w') as test_file:
    test_file.write('')

# if Path('test.txt').exists(): # Always check for file presence.
#     Path('test.txt').unlink()