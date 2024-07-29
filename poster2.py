import random

def run():
    people1 = set()
    people2 = set()
    total = 0
    while len(people2) < 6:
        num = random.randint(1, 6)
        total += 1
        if num not in people1:
            people1.add(num)
            continue
        people2.add(num)
    return total
x=1000000
total = 0
for i in range(x):
    total += run()
print(total/x)
