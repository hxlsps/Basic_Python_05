import json

def load_json(file):
    with open(file,'r',encoding='utf-8') as f:
        json_ob=json.load(f)
    return json_ob

def write_json(file,ob):
    with open(file,'w') as f:
        json.dump(ob,f)

#1: write a program to read file sample.json. display all distance and name of locations
print("#1-------------------------------")
def display(object):
    print("distance: ",object['distance'])
    print("name: ",object['name'])
    print("latitude: ",object["geocodes"]['main']['latitude'])
    print("longitude: ",object["geocodes"]['main']['longitude'])
    print("\n")

json_ob=load_json('sample.json')
val1 = json_ob['results']
for val2 in val1:
    display(val2)


#2: write a program to define a python object (dict) containing fields: date, location, gps (lat,lon), weather, population; store below python object (dict) into a json file name sample_w.json
print("\n#2-------------------------------")
py_ob={
    'date':'22-05-2001',
    'location': 'binh giang, hai duong',
    'gps':{
        'x':12345,
        'y':67890,
    },
    'weather':'storm',
    'population':892001
}

write_json('sample_w.json',py_ob)

#3: write a program to create a new json file from an existing json file(sample_w.json)
print("\n#3-------------------------------")
json_ob=load_json('sample_w.json')
write_json('sample_w2.json',json_ob)

#4: write a program to add new item into existing json file (users.json). user input from keyboard
'''
users.json
[
    {
        'name': 'John',
        'email': 'john@example.com',
        'age': 10,
        'address': 'john street'
    },
    {
        'name': 'su',
        'email': 'su@example.com',
        'age': 18,
        'address': 'su street'
    }
]
''' 

print("\n#4-------------------------------")
check='y'

class user2():
    def __init__(self,name,age,email,add):
        self.name=name
        self.email=email
        self.age=age
        self.address=add
users=[]

while(check=='y'):
    print("Enter user infor:")
    user1=dict()
    user1['name']=input("Enter user name: ")
    user1['email']=input("Enter user email: ")
    user1['age']=int(input("Enter age of user: "))
    user1['address']=input("Enter address's user: ")
    users.append(user1)
    check=input("Do you want to continue(y/n): ")

write_json('users.json',users)

#5: write a program to delete user which have age is a number input from keyboard from users.json file
age=int(input("Enter age which you want to delete: "))
json_ob=load_json('users.json')
for v in json_ob:
    if v['age']==age:
        json_ob.remove(v)
write_json('users.json',json_ob)