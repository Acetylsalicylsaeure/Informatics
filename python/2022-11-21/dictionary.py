# dictionarys assign a value to another value

person = {"name": "John",
          "age": 45,
          "city": "Vienna",
          "active": True,
          "enrolled_subjects": ["maths", "programming", "physics"]
         }

# prints value associated with given value
print(person["name"])

# prints the whole thing
print(person)

# prints the indices
for key in person:
    print(key)
# or
print(person.keys())
