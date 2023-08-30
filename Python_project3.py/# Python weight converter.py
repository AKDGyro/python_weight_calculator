# Python weight converter
print("Weight Converter and Weight Loss Calculator")
print()
print()

weight = float(input("Enter your weight "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")
    
print(f"Your weight is {weight:.2f} {unit}")  # Format weight to two decimal places

def weight_loss_calculator(weight, targetweight):
    weight_difference = weight - targetweight
    return weight_difference

action = input("Would you like to set a target weight for weight loss? (yes/no): ")

if action == "yes":
    targetweight = float(input("Enter your target weight: "))
    weight_difference = weight_loss_calculator(weight, targetweight)
    if weight_difference > 0:
        print(f"To reach your target weight, you need to lose {abs(weight_difference):.2f} kg.")
    else:
        print(f"To reach your target weight, you need to gain {abs(weight_difference):.2f} kg.")
else:
    print("Thank you for using the Weight Converter and Weight Loss Calculator")
    
