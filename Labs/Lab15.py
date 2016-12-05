from sys import argv

def f_to_c(*args):
    for i in args:
        if isinstance(i, int) or isinstance(i,float):
            ctemp = (5.0 / 9.0 * (i - 32))
            print '{:6.1f} {:5.1f}'.format(i, ctemp)
        else:
            print i,'This data is not vaild'
    return ctemp

for i in argv[1:]:
    try:
        temp = float(i)
    except (ValueError, NameError):
        print 'That was not a valid number. Please try again...'
        continue
    f_to_c(temp)