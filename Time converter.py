timeh = int(input('Print hours: '))
timem = int(input('Print minutes: '))
clas = input('Print PM or AM: ')
time = 0

if timeh > 12:
    timeh = int(input('Print hours less then 13: '))
if timem > 60:
    timem = int(input('Print minutes less then 60: '))

def time_class(timeh, timem, clas):
    if clas == 'pm' or 'PM' or 'Pm' or 'pM':
        timeh += 12
        time = "{}".format(timeh) + ':' + "{}".format(timem)
    elif clas == 'am' or 'AM' or 'Am' or 'aM':
        time = "{}".format(timeh) + ':' + "{}".format(timem)
    else:
        clas = input('Print PM or AM: ')
        time_class(timeh, timem, clas)
    return time

print(time_class(timeh, timem, clas))
