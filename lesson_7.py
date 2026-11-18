
product_list=""


while (True):
    print("1) add product")
    print("2) see list")
    print("3) exit shop")
    user = input("choose:")
    if (user == "3"):
        break
    elif user== "1":
        product=input("enter product name")
        product_list=product_list+product
    elif (user=="2"):
        print(product_list)