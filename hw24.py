import re
import os


def custom_print(data):
    os.system(f'echo {data}')


with open("text.txt", 'r') as file:
    text = file.read()

res = re.findall('[a-z]', text.lower())

letters = []
for i in res:
    if i not in letters:
        letters.append(i)

for i in letters:
    count = res.count(i)
    custom_print(i)
    custom_print(count)
    custom_print("\n")





