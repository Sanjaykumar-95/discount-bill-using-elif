n=int(input('enter amount'))
if 1000<=n<=2000:
    discount=(n*10)/100
    print discount
    print 'paid bill is',n-discount
elif 2000<=n<=3000:
    discount=(n*20)/100
    print discount
    print 'paid bill is',n-discount
elif 3000<=n<=5000:
    discount=(n*30)/100
    print discount
    print 'paid bill is',n-discount
elif n>5000:
    discount=(n*40)/100
    print discount
    print 'paid bill is',n-discount
elif n<1000:
    print 'paid bill is',n


#expected output
    #enter amount 4000
    #1200
    #paid bill is 2800

#original output
    #enter amount 4000
    #1200
    #paid bill is 2800
