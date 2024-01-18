#Infinite Loop for

from itertools import count

for i in count():
    print(i)
    if i > 5:
        break
