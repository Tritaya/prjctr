import string
import random
import os

for fname in string.ascii_uppercase:
    print(fname)
    with open(fname+'.txt', 'w') as f, open('summary.txt', 'a') as s:
        x = str(random.randint(1,100))
        f.write(x)
        s.write(f'{fname}.txt: {x}\n')

# for fname in string.ascii_uppercase:
    # os.unlink(fname+'.txt')