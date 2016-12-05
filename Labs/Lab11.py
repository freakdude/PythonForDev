fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/trees.dat')
trees = []
numberoftrees = 0
for i in fin:
    try:
        height = int(i)
    except (ValueError, NameError):
        print 'That was not a valid number. Please try again...'
        continue
    trees.append(height)
    numberoftrees +=1

print 'Tallest Tree:',max(trees)
print 'Shortest Tree:',min(trees)
print 'Average height:',format(sum(trees)/float(numberoftrees),'.1f')
print 'Number of trees',numberoftrees
fin.close()
#for x in trees:
#    print x