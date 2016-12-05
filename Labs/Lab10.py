import random
x = 0
j = 0
rolls = 10000
dice1 = []
dice2 = []
total = 13 * [0]
while x < rolls:
    dice1.append(random.randint(1,6))
    dice2.append(random.randint(1,6))
    j = dice1[x] + dice2[x]
    print (j,end = ',')
    total[j] += 1
    x += 1
roll = 2
print ('\n',total)
for i in total[2:14]:
    tmp = float(i) / rolls
    print ('{0:2d} {1:6.2%}'.format(roll, tmp))
    roll += 1
