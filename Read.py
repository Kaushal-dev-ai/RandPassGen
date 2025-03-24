import random

wordlist = []
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']

with open("wikipedia-text.txt", 'r') as file:
    data = file.readlines()
    
    for line in data:
        words = line.split()
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())
              
              
print(random.choice(wordlist))
schar = random.choice(special_chars)
num = random.choice(10,99)

password = words + schar + num
print(password)
#password = random.choice(wordlist) + schar + num
#print(password)
    