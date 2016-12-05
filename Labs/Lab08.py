

#while True:
#    f_temp = raw_input('Please enter a temp in Fahrenheit. q or Q to quit: ')
#    if f_temp == 'q' or f_temp == 'Q':
#        break
fin = open('../Resources/LabsData/tmpprecip2012.dat', 'r')
fout = open('../Resources/LabsData/tmpprecip2012-had.dat', 'w')
i = 0
total_rainfall = 0
for linein in fin:
    day = linein[0:8]
    rainfall = linein[8:13]
    hightemp = linein[13:]
    try:
        value = float(rainfall)
    except (ValueError, NameError):
        print('That was not a valid number. Please try again...')
        continue
    if value > 0:
        i += 1
        total_rainfall = total_rainfall + value
        fout.write('{0} did have ran fall \n'.format(value))
    else:
        fout.write('{0}\n'.format(value))
print('There were {0} days that had rainfall with a total of {1}'.format(i,total_rainfall))
fin.close()
fout.close()

#print