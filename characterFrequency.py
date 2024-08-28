# count the frequency of each character in a given string and store the result in a dictionary

my_dict = {}
num = int(input("Enter the size of ypur dictionary:"))

for i in range(num):
    word = input(f"Enter a character @ {i+1}:")
    char_freq = {}
    for letter in word:
            if letter in char_freq:
                char_freq[letter] += 1
            else:
                char_freq[letter] = 1

    my_dict.update({word: char_freq})
    
for key,value in my_dict.items():
    print(f"{key}: {value}")