count=0
sum=0
print("Before",count)
for thing in [9,41,12,3,75,15]:
    count=count+1
    sum=(sum+thing)
    average=int(sum/count)
print("The average is",average)
