
fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/alice_in_wonderland.dat', 'r')

alicebook = fin.read()
numberofe = alicebook.upper().count('E')
numberofall = 0.0
for linein in alicebook:
    if linein.isalpha():
        numberofall = numberofall + 1
percentofe = numberofe/numberofall
print numberofe
print numberofall
print 'There are {0} e\'s in alice in wonderland out of {1:.0f} which is {2:.2%}' .format(numberofe,numberofall,percentofe)

fin.close()
