# 1. Write a program to read an entire the sample.txt file
def read_file():
    with open('sample.txt',mode='r',encoding='utf-8') as g:
        print(g.read()) 

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
def read_file_first_last(file_name,n,first=True):
    with open(file_name,mode='r',encoding='utf-8') as g:
        lines=g.readlines()
        if first:
            print(f'{n} first lines:')
            print(lines[:n])
        else:
            print(f'{n} last lines:')
            print(lines[-n:])

# 3. Write a program to read line by line os the sample.txt file and store them in a list. Sort the list by length of each line.
def read_file_line(filename):
    with open(filename, 'r') as g:
        lines = g.readlines()
        lines.sort(key=len)
        for line in lines:
            print(line)

# 3. Write a program to append a line to the sample.txt file with line is argument come from keyboard. Print the length of file and
# the line with longest length.
def append_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text) #append a line to the file
        lines = f.readlines()
        print(f'File length: {len(lines)}')
        lines.sort(key=len)
        print('The longest sentence is:')
        print(lines[-1])

# 4. Write a program to count frequency of each word in the sample.txt file.
def word_count(filename):
    word_count = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    print(word_count)

# 5. Write a program to remove a line which line number is a argument from the keyboard.
def delete_line(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for idx, line in enumerate(lines):
            if idx != n:
                f.write(line)
# n = int(input('Enter the line number: '))
# delete_line('sample.txt', n)

# 6. Write a program to store the below content in a file name sample_w.txt:
