from operator import itemgetter

fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip.dat', 'r')
fout = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip-sorted-dict.dat', 'w')
templist = {}
month_list = [range(1,13)]
rainlist = []

for i in range(12):
    rainlist.append([]) #Total temp,days,high temp,low temp,year
#
for linein in fin:
    try:
        year = int(linein[4:8])
        month = int(linein[0:2])
        day = int(linein[2:4])
        rainfall = float(linein[8:13])
        hightemp = float(linein[13:])
    except (ValueError, NameError):
        print 'That was not a valid number. ',linein
        continue
    if year not in templist:
        templist[year] = month_list
        x = 0
        for o in templist[year]:
            o = 0,0,0,200,0
p=0
#while True:
#    print
#    for i in templist[year][p]:
#        print i


#    elif year in templist:
#        for i in templist[year][x]:
#            print
#    else:
#        linein
#    print '{:14d}'.format(year)
#    for month in range(12):
#        data = templist[year][month]
#        if len(data) == 0:
#            print '{:2d} No data'.format(month + 1)
#        else:
#            avg = float(sum(data)) / len(data)
#            print '{0:<5.0f}{1:<5.0f}{2:<5.0f}{3:<5.1f}'.format(month + 1, avg, max(data), min(data))
print templist
print templist[year]
fin.close()
fout.close()

#print