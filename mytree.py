import time
x = 8

for i in range(1,x+1,1):
    for j in range(i):
        print(" ", end="")
    for p in range(x - i,0,-1):
        print(" ",end="")
    for s in range(x - i,0,-1):
        print(" ",end="")
    for t in range(i):
        print("*", end="")
    for z in range(i-1):
        print("*",end="")
    print()
    time.sleep(0.1)
for i in range(x):
    for p in range(x - i-1,0,-1):
        print(" ",end="")    
    for j in range(i+1,x,1):
        print("0", end="") 
    for t in range(0,i+1,1):
        print("*",end="")
    for m in range(0,i,1):
        print("0", end="")
    for b in range(0,i,1):
        print("0", end="")    
    for k in range(0,i+1,1):
        print("*",end="")   
    for z in range(i+1,x+1,1):
        print("0", end="")    
    print()
    time.sleep(0.1)
for i in range(x):
    for j in range(x*2-3):
        print(" ",end="")
    for p in range(1):
        print("|  |")
        time.sleep(0.1)
print("     ",end="")
for n in "Marry Christmast ":
    print(n,end="")
    time.sleep(0.1)
