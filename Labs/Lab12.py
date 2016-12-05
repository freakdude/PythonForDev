from operator import itemgetter

fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip2012.dat', 'r')
fout = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip2012-sorted.dat', 'w')
rainlist = []
for i in range(12):
    rainlist.append([0,0,0,200]) #Total temp,days,high temp,low temp

for linein in fin:
    try:
        month = int(linein[0:2])
        day = int(linein[2:4])
        year = int(linein[4:8])
        rainfall = float(linein[8:13])
        highttemp = float(linein[13:])
    except (ValueError, NameError):
        print 'That was not a valid number. ',linein
        continue
    x = month - 1
    rainlist[x][1] += 1
    rainlist[x][0] += highttemp
    if highttemp < rainlist[x][3]:
        rainlist[x][3] = highttemp
    if highttemp > rainlist[x][2]:
        rainlist[x][2] = highttemp
print rainlist

mon = 0
fout.write('Mon High  Low   Avg\n'),
print 'Mon High  Low   Avg\n',
for ttemp,days,htemp,ltemp in rainlist:
    mon += 1
    fout.write('{0:<5.0f}{1:<5.0f}{2:<5.0f}{3:<5.1f}\n'.format(mon,htemp,ltemp,ttemp/days))
    print '{0:<5.0f}{1:<5.0f}{2:<5.0f}{3:<5.1f}'.format(mon,htemp,ltemp,ttemp/days)
for month in range(12)
    print


fin.close()
fout.close()

#print