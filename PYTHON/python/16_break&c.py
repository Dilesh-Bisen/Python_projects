print("\nBreak Statement : ")
for i in range(1, 15):
    if (i == 11):
        break
    print("5 x", i, "=", 5*i)
    


print("\nContinue Statement : ")
for i in range(1, 15):
    if (i == 10):
        print("Skip the iteration.")
        continue
    
    print("5 x", i, "=", 5*i)
    
    
print("\nDo-while loop : ")
i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
