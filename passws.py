import random

upper_char = ["A", "B","C","D","E"]
Lower_char = ["a", "b","c","d","e",]
num = ["1", "2", "3", "4", "5"]
special_char = ['@', '#','%','&','*',]

passw = random.choice(upper_char) + random.choice(Lower_char) + random.choice(num) + random.choice(special_char)     

print(passw)
