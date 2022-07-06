salary=float(input('Your salary:' ))
if salary>=30000:
    years_worked=float(input('Your years on job: '))
    if years_worked>=2:
        print('You qualify for the loan')
    else:
        print('You must have been on your current job for atleast 2 years to qualify')
else:
    print('You must earn at least $30000 per year to qualify')