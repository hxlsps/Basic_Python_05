#1. Rewrite functions using lambda
from re import X


def cube(x):
    return x * x * x

cube_l = lambda x: x* x * x

#print(cube(2))
#print(cube_l(2))

#2 Create a list as follow: 10, 20, .... 100 using lambda function
f = lambda x: x*10
new_list = [f(x) for x in range(1,11)]
#print(new_list)

#3 Given a list: [[2, 3, 1], [1, 4, 19, 13], [5, 9, 2, 0, 6]]
#Create a list with second max values of each item in above list: expect: [2, 13, 6] using lambda function
given_list = [[2, 3, 1], [1, 4, 19, 13], [5, 9, 2, 0, 6]]

sorted_item_list_func = lambda x: (sorted(item) for item in x)

second_max_list_func = lambda x, f: [y[len(y)-2] for y in f(x)]

second_max_list = second_max_list_func(given_list, sorted_item_list_func)
#print(second_max_list)

#Map example
#1.
def addition(n):
    return n + 2*n

num_set = [1, 2, 3, 4]
#print(list(map(addition, num_set)))

#use lambda
#print(list(map(lambda n: n + 2*n, num_set)))

#2.
list_1 = [1, 2, 4]
list_2 = [5, 6, 3]

result = map((lambda x, y: x + y), list_1, list_2)
#print(list(result))

#Decorator
def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a, b):
    return a+b

print(add_together([(1,3), (3,7), (5,5), (6,7)]))