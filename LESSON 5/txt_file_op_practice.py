# 1. Write a program to read an entire the sample.txt file
with open('sample.txt',mode='r',encoding='utf-8') as g:
    print(g.read()) 

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
with open('sample.txt',mode='r',encoding='utf-8') as g:
    n=int(input('Input n or 0 (for first line) or -1 (for last line): '))
    h=g.readlines()[n]
    print(h)


# 3. Write a program to read line by line os the sample.txt file and store them in a list. Sort the list by length of each line.
g=open('sample.txt',mode='r',encoding='utf-8')
list_line=[]
count_line=0
for line in g.readlines():
    count_line+=1
    print(f'Line {count_line}: {line}')
    list_line.append(line)
print(list_line)
g.close()

# 3. Write a program to append a line to the sample.txt file with line is argument come from keyboard. Print the length of file and
# the line with longest length.
g=open('sample.txt',mode='r',encoding='utf-8')
input=('Input a line: ')
print(len(list_line))
g.close()

# 4. Write a program to count frequency of each word in the sample.txt file.

# 5. Write a program to remove a line which line number is a argument from the keyboard.

# 6. Write a program to store the below content in a file name sample_w.txt:
