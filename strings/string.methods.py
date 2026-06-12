name = "Python"

#String length
print(len(name))

#String concatenation
first="Tarun"
last="Saini"

full= first+" "+last
print(full)

#String repetition
print("Hello" * 3)

#Check existence
text= "I love Python"
print("Python" in text)

#Convert to uppercase
print(name.upper())

#Convert to lower
print(name.lower())

#title()
str= "hello world"
print(str.title()) #Capitalize first letter of each word

print(str.capitalize())

#strip()- Removes spaces from both ends.
name = "    tarun  "
print(name.strip())

#lstrip()- Remove left spaces.
print(name.lstrip())

#rstrip()- Remove right spaces
print(name.rstrip())

#Replace Text
text= "I love Java"
print(text.replace("Java","Python"))

#Split String- Converts string into list.
text="Python Java React"
print(text.split())

#Split Using Specific Character
data = "10,20,30"
print(data.split(","))

#Join Strings- Opposite of split.
words = ["Python", "Java", "React"]
print(" ".join(words))
print("-".join(words))

#Find Substring
text = "I love Python"
print(text.find("Python")) #7 (return -1 if not present)

#Startswith and Endswith
print(text.startswith("Python")) #False
print(text.endswith("Python")) #True