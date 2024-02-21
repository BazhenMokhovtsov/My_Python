from zipfile import ZipFile
from pathlib import Path


if not Path('ZipDir').exists():
    Path('ZipDir').mkdir(exist_ok=True)

if not Path('ZipDir/my-files').exists():
    Path('ZipDir/my-files').mkdir(exist_ok=True)

if not Path('ZipDir/my-files/first.txt').exists():
    with open('ZipDir/my-files/first.txt', 'w') as my_file:
        my_file.write('This is my first file.')

if not Path('ZipDir/my-files/second.txt').exists():
    with open('ZipDir/my-files/second.txt', 'w') as my_file:
        my_file.write('This is my second file.')


with ZipFile('ZipDir/my-file.zip', 'w') as my_zip_file:
    for file in Path('ZipDir/my-files').iterdir():
        print(file)
        my_zip_file.write(file)

with ZipFile('ZipDir/my-file.zip') as my_zip_file:
    my_zip_file.extractall('ZipDir/My-files-unzip')
    # print(my_zip_file.filename)
