day=-1

match day:
    case -1 | 0: #Matching Multiple Values
        print("Day 0")
    case 1:
        print("Day 1")
    case 2:
        print("Day 2")
    case _: #Default case
        print("Day 3")     
        
        
# Unlike switch statements in languages like C, C++, or Java, Python's match automatically stops 
# after the first matching case and does not "fall through" to the next case.           