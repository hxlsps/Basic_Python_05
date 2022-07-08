#Set the correct_length variable to false
correct_length=False
#Set the has_uppercase variable to false
has_uppercase=False
#Set the has_lowercase variable to false
has_lowercase=False
#Set the has_digit variable to false
has_digit=False
#Get the password
password=input('Input password: ')
#Check password is valid or not
if len(password)>=7:
    correct_length=True 
    for x in password:
        if x.isupper():
            has_uppercase=True
        if x.islower():
            has_lowercase=True
        if x.isdigit():
            has_digit=True
#Check the result
if correct_length and has_uppercase and has_lowercase and has_digit:
    is_valid=True
else:
    is_valid=False
#Print the result
print(is_valid)


