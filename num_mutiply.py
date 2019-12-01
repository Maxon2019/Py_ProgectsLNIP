n = input()
mult = 1
summ = 0
for i in n:
	if int(i) != 0:
		mult *= int(i)
 
print("Произведение значащих цифр:", mult)
