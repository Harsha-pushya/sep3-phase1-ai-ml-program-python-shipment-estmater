
BASE_FEE = 5.00 
RATE_PER_KG = 2.50 
INSURANCE_RATE = 0.01 
FRAGILE_SURCHARGE = 3.50

try:
    cost=float(input("enter the cost of the item:"))
    weight=float(input("enter the weight of the item:"))
    fragile=input("is item fragile? (yes/no):")
    
    total_cost=BASE_FEE+weight*RATE_PER_KG+cost*INSURANCE_RATE


    if fragile.lower() == "yes":
        total_cost += FRAGILE_SURCHARGE
    
    print("Total shipping cost: $", total_cost)
    print(" SHIPMENT COST RECEIPT") 
    print("-----------------------------") 
    print(f"Weight: {weight:.2f} kg") 
    print(f"Declared Value: {cost:.2f}") 
    print(f"Weight Cost: {weight*RATE_PER_KG:.2f}") 
    print(f"Insurance: {cost*INSURANCE_RATE:.2f}")
    print(f"Fragile Surcharge: {FRAGILE_SURCHARGE:.2f}") 
    print(f"Base Fee: {BASE_FEE:.2f}") 
    print("-----------------------------") 
    print(f"TOTAL COST: {total_cost:.2f}") 
    print("-----------------------------")
except ValueError:
    print("Invalid input. Please enter valid numbers.")