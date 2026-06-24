str="ttaarunn"
count={}

for s in str:
    count[s]=count.get(s,0)+1
    
for s in str:
    if count[s]==1:
       print(s)    
       break
   
else:
    print("No non-repeating character")   