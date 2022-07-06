hours_worked=float(input('Number of hours worked: '))
hourly_pay_rate=float(input('Hourly pay rate: '))
if hours_worked>40:
    print('The gross pay: ',((hours_worked-40)*1.5+40)*hourly_pay_rate)
else:
        print('The gross pay: ',(hours_worked)*hourly_pay_rate)