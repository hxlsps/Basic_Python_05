#Get the string
string_input=input('Input the string: ')
#Set the delimeter count
count=0
#Count t in string
for x in string_input:
    if x =='t' or x=='T':
        count+=1
#Print the result
print('The number of t or T is: ', count)