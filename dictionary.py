# DICTIONARY- Most important collection type. Think of it as a JavaScript object.

user = {
    "name": "Tarun",
    "age": 21,
    "city": "Haryana"
}

#Access values
print(user["name"])

# Safer Access
print(user.get("name"))

# DIFFERENCE:
# dict[key] → Returns the value if the key exists, otherwise raises a KeyError.
# dict.get(key) → Returns the value if the key exists, otherwise returns None (or a specified default value) without raising an error.

print(user.get("email", "Not provided")) 

# Add New Key
user["salary"]=30000

#Update Value
user["age"]=22
print(user)

# Delete Key
del user["age"]
print(user)

# Loop Through Dictionary
for key in user:
    print(key) #When you iterate directly over a dictionary, Python automatically gives you only the keys.
    
# Get Keys
print(user.keys())    

# Get Values
print(user.values())

# Get Both
for key, value in user.items():
    print(key,value) # Here, .items() returns pairs of (key, value).
    

# ---- Nested Dictionary -----

user1 = {
    "name": "Tarun",
    "address": {
        "city": "Lucknow",
        "state": "UP"
    }
} 

# Access
print(user1["address"]["state"])   