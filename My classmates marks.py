import json
marks = None
runner = 1
all_name = None
class Classmates:
    def __init__(self, all_name, marks):
        self.all_name = all_name
        self.marks = marks

def marks(all_name):
    print('For whom?')
    name = input('Print name: ')
    surname = input('Print surname: ')
    all_name = name +'_'+ surname
    marks = input('Print marks for {name}: '.format(name = all_name))
    n = Classmates('{k}'.format(k = all_name), '{f}'.format(f = marks))
    return marks

def output_marks(marks):
    print('For whom?')
    name = input('Print name: ')
    surname = input('Print surname: ')
    all_name = name +'_'+ surname
    with open("data_file.json", "w") as write_file:
        json.dump(all_name, marks)
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

while runner == 1:
    ans = int(input('If you want to read marks press 1 or 2 for write them''\n'))
    if ans == 2:
        marks(all_name)
        runner = int(input('if you want to continue press 1 if no press 0: '))
    elif ans == 1:
        d = output_marks(marks)
        print(d)
        runner = int(input('if you want to continue press 1 if no press 0: '))
    else:
        print('What? I dont understand you...Reprint please')
        ans = int(input('If you want to read marks press 1 or 2 for write them''\n'))
        runner = int(input('if you want to continue press 1 if no press 0: '))

