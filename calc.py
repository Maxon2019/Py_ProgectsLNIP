password = input('Enter your password:')
hard = 0 
if len(password) > 6:   # for nums
    hard += 1
     
if 'a'or 'A' in password:     # A
    hard += 1

if 'b'or'B' in password:     # B
    hard += 1

if 'c'or'C' in password:     # C
    hard += 1

if 'd'or'D' in password:     # D
    hard += 1

if 'e'or'E' in password:     # E
    hard = 1+hard

if 'f'or'F' in password:     # F
    hard += 1

if 'g'or'G' in password:     # G
    hard += 1

if 'h'or'H' in password:     # H
    hard += 1

if 'i'or'I' in password:     # I
    hard += 1

if 'j'or'J' in password:     # J
    hard += 1

if 'k'or'K' in password:     # K
    hard += 1

if 'l'or'L' in password:     # L
    hard += 1

if 'm'or'M' in password:     # M
    hard += 1

if 'n'or'N' in password:     # N
    hard += 1

if 'o'or'O' in password:     # O
    hard += 1

if 'p'or'P' in password:     # P
    hard += 1

if 'q'or'q' in password:     # Q
    hard += 1

if 'r'or'R' in password:     # R
    hard += 1

print('Your password rate is:',hard,'/100')
