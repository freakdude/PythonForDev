
def f_to_c(*args):
    for i in args:
        if isinstance(i, int) or isinstance(i,float):
            ctemp = (5.0 / 9.0 * (i - 32))
            print '{:6.1f} {:5.1f}'.format(i, ctemp)
        else:
            print i,'This data is not vaild'
    return ctemp
f_temp = ()
#while True:
#    f_temp = raw_input('Please enter a temp in Fahrenheit. q or Q to quit: ')
#    if f_temp == 'q' or f_temp == 'Q':
#        break
#    else:
#        try:
#            temp = float(f_temp)
#        except (ValueError, NameError):
#            print 'That was not a valid number. Please try again...'
#            continue
#    print 'Your temp in C is {:.2f}' .format(f_to_c(f_temp))
f_to_c(32,45,43,'e5',342,43.5)
