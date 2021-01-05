import csv

reader = csv.DictReader(open('data_csv.csv','r'))
codes = {}
for row in reader:
    codes[row['Name']] = row['Code']
code_one = input()
code_two = input()
if code_one >= code_two:
    temp = code_one
    code_one = code_two
    code_two = temp
for key,value in codes.items():
    if code_one == value:
        code_one = key
    elif code_two == value:
        code_two = key
print(code_one)
print(code_two)
answer = dict()
for key,value in codes.items():
    if key > code_one and key < code_two:
        answer[key] = value
print(sorted(answer))
