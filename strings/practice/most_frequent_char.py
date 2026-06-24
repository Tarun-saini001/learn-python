name="banana"
count={}

for chr in name:
    count[chr]=count.get(chr,0)+1

max_count=0
most_frequent=""

for ch in count:
    if count[ch]>max_count:
        max_count=count[ch]   
        most_frequent=ch
        
print(most_frequent)     


#OR

most_frequent=max(count,key=count.get)
print(most_frequent)
