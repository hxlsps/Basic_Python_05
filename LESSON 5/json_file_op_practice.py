import json
#1 Write python program to read file sample.json. Display all distance and name of locations.
def read_file_distance_name():
    with open('sample.json','r', encoding='utf-8') as f:
        obj = json.load(f)
        #print(type(obj))
        features=obj['results']
        #print(type(features))
        for count in range(len(features)):
            feature=features[count]
            print(f"{count+1}: Distance: {feature['distance']}, Name: {feature['name']}")
            latitude=feature['geocodes']['main']['latitude']
            longtitude=feature['geocodes']['main']['longitude']
            print(f"Latitude={latitude}, Longtitude={longtitude}")

#read_file_distance_name()

# 2. Write a program to:
# - Define a python object (dictionary) containing fields: date, location, gps (lat, lon), weather, population.
# - Store a python object (dictionary) into a json file name sample_w.json.
def store_python_object():
    python_object={
        'date':2022,
        'location':'Ho Chi Minh city',
        'gps':{
            'latitude':20,
            'longtitude':199
        },
        'weather':'sunny'
    }
    with open('sample_w.json','w') as sp:
        json.dump(python_object,sp)
#store_python_object()           

# 3. Write a program to to create a new json file from an existing json file (sample_w.json)
def create_new_json_from_existing():
    with open('sample_w_new.json','w') as sn:
        with open('sample_w.json','r',encoding='utf-8') as f:
            json_ob=json.load(f)
            json.dump(json_ob,sn)

create_new_json_from_existing()

# 4. Write a program to add new 3 users into existing json file (users.json):


# 5. Write a program to delete users which have age is 18 from users.json file.
