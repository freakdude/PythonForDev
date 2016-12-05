vnumberofstocks = 125 #Stocks sold
vpurchaseprice = 25.32 #Purchase price
vsellprice = 48.97 #Sell price

x = (vnumberofstocks * vsellprice) - (vnumberofstocks * vpurchaseprice)

print 'You purchased ', vnumberofstocks, ' stocks for ', vpurchaseprice, ' and sold for ', vsellprice, ' you made $', x
print '\n'
print '\n'

vproductprice = 127.99
vpercentoff = .16

vamountoffprice = vproductprice * vpercentoff
vnewprice = vproductprice - vamountoffprice

print 'Original product price is',vproductprice,'you get %',vpercentoff*100,'off. Your new price is $'+str(vnewprice),'\n'
print 'Original product price is',vproductprice,'you get',vpercentoff,'off. Your new price is ${0:.2f}' .format(vnewprice),'\n'
print 'Original product price is ${0} you get {1:.0%} off. Your new price is ${2:.2f}'.format(vproductprice,vpercentoff,vnewprice),'\n'
print 'Original product price is',vproductprice,'you get',vpercentoff,'off. Your new price is',round(vnewprice,2),'\n'

print id(vproductprice)
