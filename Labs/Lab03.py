

#while True:
#    f_temp = raw_input('Please enter a temp in Fahrenheit. q or Q to quit: ')
#    if f_temp == 'q' or f_temp == 'Q':
#        break
ftemp = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/temps.dat', 'r')
f = open('/Users/mrash/Desktop/PythonforDevelopers/LabsData/temps-F.dat', 'w')
for linein in ftemp:
    try:
        temp = float(linein)
    except (ValueError, NameError):
        print 'That was not a valid number. Please try again...'
        continue
    c_temp = format(5.0/9.0*(temp-32), '.2f')
    f.write('Your temp in C is {0} \n'.format(c_temp))
ftemp.close()
f.close()

#print