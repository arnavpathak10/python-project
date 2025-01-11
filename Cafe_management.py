from calc_program_time import program_time
@program_time
def cafe_management():
    #list of menu available
    menu = {"chat" : 45,
            "maggi" : 45,
            "tea" : 30,
            "coffe" : 25,
            "pizza" : 55,
            "burger" : 65,
            "icecream" : 45,
            "samosa" : 25,
            "noodles" : 35,
            "water" : 20,
            "paneer" : 140,
        }
    print("list of menu available")
    for i in menu:
        print(f"{i} : {menu[i]}")
        
    #get_order from customer
    item_ordered = []
    def get_order():
        while True: 
            inp = input("Do you want to order more item (yes/no) : ")
            if(inp.lower()=="y" or inp.lower()=="yes"):
                #take order input 
                order = input("what you like to order : ")
                #check whether item present in menu or not
                if((order.lower()) in menu):
                    item_ordered.append(order)
                else:
                    print("Ordered item not present")
            elif(inp.lower()=="n" or inp.lower()=="no"):
                print("Thankyou")
                break 
            else:
                print("Enter valid answer")

    #print bill of ordered item
    def get_bill():
        get_order()
        sum = 0
        for item in item_ordered:
            print(f"{item} : {menu[item]}")
            sum+=menu[item]
        print(f"Payable Amount : {sum}\nThanks for visit") 

    get_bill()
cafe_management()