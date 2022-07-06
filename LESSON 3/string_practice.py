#1. Assign a string to a variable and display
str_txt='My favorite space is heaven.'
print(str_txt)
#2. String as array: display some characters of str_txt
print(f'{str_txt[-4:]},\n{str_txt[1:4]},\n{str_txt[:5]},\n{str_txt[1:]} ')
#3. Loop through string
for value in range(len(str_txt)):
    print(str_txt[value])
#4. Length of string
print(len(str_txt))
#5. Check if string str_txt contains another string. If has, print start position of that substring.
get_check=input('Enter string: ')
if get_check in str_txt:
    print(str_txt.find(get_check))
else:
    print('No substring')    
#6. Print str with all the characters are capitalized/ normalized
print(str_txt.upper())
print(str_txt.lower())
print(str_txt.title())
#7. Remove all the white space
print(str_txt.replace(' ',''))
#8. Replace all the h character with m character
print(str_txt.replace('h','m'))
#9. Split str_txt by white spaces and display second item of array
print(str_txt.split(' '))