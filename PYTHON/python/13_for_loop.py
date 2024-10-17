name = "Dilesh"
for i in name:
    print(i)
    # if(i=="D"):
    #     print("Something special.")
print("\n")

# iterating over a list :
colors = ["red", "blue", "green", "black", "white"]
for i in colors:
    print(i)
    for j in i:
        print(j)

''' 
This is invalid in python :

for(int i= 0;i<=10; i++){
    print(i);
}
'''

print("\nPrint the numbers :")
for i in range(11):
    print(i, end=" ")
print("\n")

for i in range(5, 10):   
# 5(include) but 10(exclude)
    print(i)
print("\n")

for j in range(1, 10, 2):  
# 1(include),but 10(exclude),2(increment)
    print(j)
print("\n")

for k in range(10, 1, -2):  
# 10(include),but 1(exclude),-2(decrement)
    print(k)
print("\n")
