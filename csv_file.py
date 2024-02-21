from pathlib import Path
import csv

Path('csv_files').mkdir(exist_ok=True)

with open('csv_files/test.scv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5522, 'Bazhen', 211])
    writer.writerow([734, 'Bob', 31])
    writer.writerow([1522, 'Lisa', 111])

with open('csv_files/test.scv') as csv_file_for_read:
    reader = csv.reader(csv_file_for_read)
    for string in reader:
        print(string)
