# remove key-value pairs where the value is less than 10

students = { }
num = int(input("Enter the size of your dictionary:"))

for i in range(num):
    name = input("Enter the key:")
    score = int(input("Enter the value:"))
    students.update({name: score})
    
print("your new dictionary is:", students)

keys_to_remove = [key for key, value in students.items() if value < 10]

for key in keys_to_remove:
        del students[key]
        
print("The newest dictionary is", students)