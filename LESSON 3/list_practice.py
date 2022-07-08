#1 Create a list named my_list with items which have different data types and length at least 5
my_list=['Loc',11.4,2000,22,'TPHCM','DHSP']
#2 Print all items of my_list in single line
for item in my_list:
    print(item)
#3 Count the number of each items in my_list
for i, item in enumerate(my_list):
    print(i, item)
#4 Reverse the order of the item in my_list
my_list.reverse()
print(my_list)
#5 Square the numeric items of items in my_list then print result:
for item in my_list:
    if type(item) is int or type(item) is float:
        print(item**2)
#6 Add some single values and iterable values to my_list:
my_list.append('Q5')
my_list.append(936475161)
print(my_list)
family=['ba','me','em']
my_list.extend(family)
print(my_list)
#7 Remove values at the end and at the second position of my_list
my_list.pop()
my_list.pop(1)
print(my_list)
#8 Display those items from my_list that are divisible by 5
for item in my_list:
    if type(item) is int:
        if item%5==0:
            print(item)
#9 Calculate the sum of all numeric items in my_list
sum=0
for item in my_list:
    if type(item) is int or type(item) is float:
        sum=sum+item
print('Sum of all numeric items in my_list is: ',sum)
#10 Create a list named my_list_str from all string item in my_list, then uppercase them
my_list_str=[]
for item in my_list:
    if type(item) is str:
        my_list_str.append(item.upper())
print(my_list_str)
#11 Create a new list named my_list_nume from all numeric items in my_list, then sort them
my_list_num=[]
for item in my_list:
    if type(item) is int or type(item) is float:
        my_list_num.append(item)
my_list_num.sort()
print(my_list_num)
#12 Find the maximum/ minimum values of my_list_num
print(max(my_list_num))
print(min(my_list_num))
#13 Remove duplicate values from my_list_num, if have
my_list_num.append(2000)
print(my_list_num)
for item in my_list_num:
    if my_list_num.count(item)>=2:
        for itemm in my_list_num:
            if itemm == item:
                my_list_num.remove(itemm)
print(my_list_num)
#14 Display odd and even number of my_list_num
odd_number=[]
even_number=[]
for item in my_list_num:
    if type(item) is int:
        if item%2==0:
            even_number.append(item)
        else:
            odd_number.append(item)
print('Odd number: ',odd_number)
print('Even number: ',even_number)
