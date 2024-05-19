def rsufficient(ingre):
    """RETURNS WHETHERE THE RESOURCE IS SUFFICIENT OR NOT"""
    for i in ingre:
        if ingre[i]>=resource[i]:
            print(f"Insufficent Resource {i}!!")
            return False
        return True


def coins():
    """RETURNS THE TOTAL CALCULATED FROM COINS INSERTED"""
    print("Enter Coins!!!")
    q=int(input("How many Quaters?"))*0.25
    d=int(input("How many dimes?"))*0.1
    n=int(input("How many nickels?"))*0.05
    p=int(input("How many Pennies?"))*0.01
    total=q+d+n+p
    return total

def trenscation(m,dc):
    """Return true when the payment is accepted or false if money is insufficient"""
    if m>=dc:
        c=round(m-dc,2)
        print(f"Here is the change ${c}")
        global profit
        profit+=dc
        return True
    else:
        print("Sorry insufficient money!!!")
        return False

# def re(resource,profit):
#     for i in resource:
#         print(f"{i}:{resource[i]}")
#     print(f"Money:${profit}")

def coffees(dn,oi):
    for i in oi:
        resource[i]-=oi[i]
    print(f"Here is your Drink {dn.upper()}. ENJOY!!!☕")




MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18},"cost": 1.5,},

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24, 
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resource ={
    'water':300,
    'milk':200,
    'coffee':100
}
profit=0
coffee=True
while coffee:
    choice=input("What would you like?\n(espresso/latte/cappuccino):").lower()

    if choice=='report':
        for i in resource:
            print(f"{i}:{resource[i]}")
        print(f"Money:${profit}")
        # re(resource,profit)
    
    elif choice=='off':
        
        print("Machine is Off!!!")
        coffee=False

    else:
        if choice not in MENU:
            print(f"DRINK {choice.upper()} NOT AVAILABLE!!!")
            coffee = False
        else:
            drink =MENU[choice]
            if rsufficient(drink['ingredients']):
                pay=coins()
                if trenscation(pay,drink['cost']):
                    coffees(dn=choice,oi=drink['ingredients'])
    print("\n"*4)

            
        
