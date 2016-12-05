from operator import itemgetter

fin = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip.dat', 'r')
fout = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/tmpprecip-sorted.dat', 'w')
templist = []
min_year = 1921
max_year = 2012
for yr in range(min_year, max_year+1):
    yr_data = []
    for mon in range(12):
        yr_data.append([])
    templist.append(yr_data)

rainlist = []
#for i in range(12):
#    rainlist.append([0,0,0,200,0]) #Total temp,days,high temp,low temp,year
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
    month -= 1
    year -= min_year
    templist[year][month].append(hightemp)
#    d[year][month] = {'Temp': hightemp}
#    x = month - 1
#    rainlist[x][1] += 1
#    rainlist[x][0] += hightemp
#    if hightemp < rainlist[x][3]:
#        rainlist[x][3] = hightemp
#    if hightemp > rainlist[x][2]:
#        rainlist[x][2] = hightemp


#mon = 0
#print 'Mon High  Low   Avg\n',
#for ttemp,days,htemp,ltemp,ytemp in rainlist:
#    mon += 1
#    print '{0:<5.0f}{1:<5.0f}{2:<5.0f}{3:<5.1f}'.format(mon,htemp,ltemp,ttemp/days)
for year in range(min_year, max_year+1):
    print '{:14d}'.format(year)
    year -= min_year
    for month in range(12):
        data = templist[year][month]
        if len(data) == 0:
            print '{:2d} No data'.format(month + 1)
        else:
            avg = float(sum(data)) / len(data)
            print '{0:<5.0f}{1:<5.0f}{2:<5.0f}{3:<5.1f}'.format(month + 1, avg, max(data), min(data))
print templist
fin.close()
fout.close()

#print