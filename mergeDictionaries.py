# merge two dictionaries 

my_dict1 = {"frank": 22,
            "Ancilla": 34,}
my_dict2 = {"city": "Nairobi",
            "country": "Kenya"}

major_Dict = {}

major_Dict.update(my_dict1) # can also use the | in merging (major_Dict = my_dict1 | my_dict2)
major_Dict.update(my_dict2)
print(major_Dict)