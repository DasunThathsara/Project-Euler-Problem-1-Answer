a=0
b=0
for x in range(0,1000):
   if x%3==0:
       a=a+x
       if x%5==0:
           continue
   elif x%5==0:
       b=b+x
       if x%3==0:
           continue
print(a+b)
