import string
from operator import itemgetter

fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/alice_in_wonderland.dat', 'r')

alicebook = fin.read().upper()
numberofe = alicebook.upper().count('E')
numberofall = 0.0
whitespace = string.whitespace
dict_all = {}
for linein in alicebook:
#    if string.whitespace:
#        print
    if linein in whitespace:
        print
    elif linein not in dict_all:
            dict_all[linein] = 1
    else:
        dict_all[linein] += 1
templist = dict_all.items()
templist.sort(key=itemgetter(1), reverse=True)
for a, b in templist:
    print '{:5}{:<}'.format(a,b)


#percentofe = numberofe/numberofall
#print numberofe
#print numberofall
#print 'There are {0} e\'s in alice in wonderland out of {1:.0f} which is {2:.2%}' .format(numberofe,numberofall,percentofe)
print dict_all
fin.close()
