import json
marks = None
runner = 1
all_name = None
ans = 0
a = {}
data = {}
data[all_name] = {}

def marks_choise(all_name):
    print('For whom do you want to print marks?')
    surname = input('Print surname: ')
    name = input('Print name: ')
    all_name = surname +' '+ name
    marks = input('Print marks: ')
    a = {all_name : marks }
    return a

def load_json(marks,a):
    with open("data_file.json", "w") as w_file:
        json.dump(a, w_file)
    return w_file

def read_json(a):
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

while runner == 1:
    ans = int(input('Press 1 if you want to write marks or 0 if you want to read them: '))
    if ans == 1:
        a = marks_choise(all_name)
        load_json(marks,a)
        runner = int(input('If you want to continue press 1 if no press 0: '))
    elif ans == 0:
         print(read_json(a))
         runner = int(input('If you want to continue press 1 if no press 0: '))
    else:
        print("This is not 1 or 0 reprint please")

if runner == 0:
    print('Thanks for using this app!Goodbye!')
