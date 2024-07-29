import random

def run():
    people = set()
    total = 0
    while len(people) < 6:
        people.add(random.randint(1, 6))
        total += 1
    return total
x=1000000
total = 0
for i in range(x):
    total += run()
print(total/x)
