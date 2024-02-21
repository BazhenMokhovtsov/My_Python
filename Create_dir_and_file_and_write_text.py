from pathlib import Path

if not Path('files').exists():
    Path('files').mkdir()

with open('files/first.txt', 'w') as first_file:
    first_file.write('Hello World! \n')
    first_file.write('My name is Bazhen \n')
    first_file.write("i'm a python programmer \n")

with open('files/second.txt', 'w') as second_file:
    second_file.write('Bye World!\n')
    second_file.write('My name is NOT Bazhen\n')
    second_file.write("i'm a NOT python programmer\n")

with open('files/first.txt') as first_file:
    text = first_file.read()
    print(text)

with open('files/second.txt') as second_file:
    while True: # Better than the method .read() – no need for storage a large list of lines.
        line = second_file.readline()
        if not line:
            break
        print(line.strip())


# if Path('files/first.txt').exists():
#     Path('files/first.txt').unlink()
#
# if Path('files/second.txt').exists():
#     Path('files/second.txt').unlink()
#
# if Path('files').exists():
#     Path('files').rmdir()
