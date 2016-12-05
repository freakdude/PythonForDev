
def f_to_c(a):
    ctemp = 5.0 / 9.0 * (a - 32)
    return ctemp

while True:
    f_temp = raw_input('Please enter a temp in Fahrenheit. q or Q to quit: ')
    if f_temp == 'q' or f_temp == 'Q':
        break
    else:
        try:
            temp = float(f_temp)
        except (ValueError, NameError):
            print 'That was not a valid number. Please try again...'
            continue
    print 'Your temp in C is {:.2f}' .format(f_to_c(temp))
print
