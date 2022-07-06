keep_going = 'y'
while keep_going == 'y':
    sales=int(input('The amount of sale: '))
    comm_rate=float(input('Commission rate: '))
    commission=sales*comm_rate
    print(commission)
    keep_going=input('Do you want to calculate another commission? (Enter y for yes)')

