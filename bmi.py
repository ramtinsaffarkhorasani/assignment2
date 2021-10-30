a=float(input('enter your weight'))
b=float(input('enter your height'))
c=a/(b**2)
if c <=18.5:
    print('underwieght')
elif c<24.9 and c>18.5:
    print('normal')
elif c>24.9 and c<29.9:
    print('overwieght')
elif c>29.9 and 34.9>c:
    print('obese') 
elif c>=35:
    print('exteremly obese') 
