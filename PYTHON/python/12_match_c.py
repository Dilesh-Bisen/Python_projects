a = int(input("Enter a number : "))

match a:
    case 1:
        print("Case 1 is matched.")
    case 2:
        print("Case 2 is matched.")
    case 3:
        print("Case 3 is matched.")
    case 4:
        print("Case 4 is matched.")
    case 5:
        print("Case 5 is matched.")
    case _ if(a!=50):
        print(a,"is not equal to 50.")
    case _ if (a != 100):
        print(a, "is not equal to 100.")
    # case _:
    #     print("Invalid Case.")
 
        

