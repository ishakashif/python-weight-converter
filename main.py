# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    print(f"Your weight is: {round(weight, 1)} {unit}")
    unit = "Lbs."
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit")

