# create a dictionary from two lists: one containing keys and the other containing values

names = []
ages = []

# Input for names
for i in range(3):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Input for ages
for i in range(3):
    age = int(input(f"Enter age {i + 1}: "))
    ages.append(age)

# Create a dictionary by pairing names with ages
my_dict = dict(zip(names, ages))

# Print the resulting dictionary
print("The resulting dictionary is:", my_dict)
