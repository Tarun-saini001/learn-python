age = 20

if age >= 18:
    print("You can vote")
    
#if else
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
    
# if  elif else
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")        
    
    
# nested if
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry Allowed")    