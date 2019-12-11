with open('01.txt' ,'r') as f:
    f = f.read()
word = 0

def delete_word_from_file(f,word):
   print(f)
   word = input('Wich word do you want to delete?''\n')
   nword = input('on what word do you want to change it?''\n')
   num = int(input('How much words do you want to delete?''\n'))
   f = f.replace(word,nword,num)
   return f
print(delete_word_from_file(f,word))

