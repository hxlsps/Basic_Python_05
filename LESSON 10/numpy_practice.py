from turtle import shape
import numpy as np

#1 Create a Numpy array 1D with values between 11 and 101, step by 3.
def array_1():
    arr = np.arange(11, 101, 3)
    print(arr)

#array_1()

#2 Extract the values from the numpy array
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [1, 3, 5, 7, 9]
def extract_even_values(arr):
    print (arr[arr % 2 != 0])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#extract_even_values(arr)

#3 Replace the odd value in numpy array with -1
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
def replace_odd_value(arr):
    new_arr = np.where(arr % 2 != 0, -1, arr)
    print(new_arr)

#replace_odd_value(arr)
    

# 4. Reshape/Convert 1D array to 2D array.
# Input: np.arrange(10)
# Output: array with shape (2, 5)
arr_2 = np.arange(10)
def convert_1D_to_2D(arr):
    newarr = arr.reshape(2,5)
    print(newarr)

#convert_1D_to_2D(arr)

# 5. Stack array x and y vertically (3 ways)
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)

# 6. Stack array x and y horizontally
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)

# 7. Find common values between 2 numpy arrays:
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b = np.array([2, 5, 10, 9, 4, 8, 7, 12])
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = np.array([2, 5, 10, 9, 4, 8, 7, 12])

#print(np.intersect1d(a, b))

# 8. Remove all values of array y from array x:
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 5, 3])

def remove_all_value_of_y_from_x(x, y):
    list_x = list(np.reshape(x, -1))
    list_y = list(np.reshape(y, -1))

    new_list = []
    for char in list_x:
        if char not in list_y:
            new_list.append(char)

    new_arr = np.array(new_list)
    return new_arr

#print(remove_all_value_of_y_from_x(x, y))

# 9. Swap 2 columns/rows in 2D array
# arr = np.arange(9).reshape(3, 3)
arr = np.arange(9).reshape(3, 3)

#print(arr.T)

# 10. Reverse 2 columns/rows in 2D array
# arr = np.arange(9).reshape(3, 3)
arr = np.arange(9).reshape(3, 3)
print(arr)

#print(np.fliplr(arr)) #Reverse columns method 1

def reverse_column_row(arr, c = True, r = True):
    new_list = []
    if r:
        for i in range(arr.shape[0]):
            new_list.append(arr[i, :][::-1])
    
    if c:
        for i in range(arr.shape[1]):
            new_list.append(arr[:, i][::-1])
    
    print(new_list)
    #newarr = np.array(new_list).reshape(arr.shape)
    #print(newarr)

reverse_column_row(arr, c = False, r = True)