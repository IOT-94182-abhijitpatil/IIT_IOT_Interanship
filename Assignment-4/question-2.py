# Lambda conversion functions
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda feet: feet * 12
inches_to_cm = lambda inches: inches * 2.54


# Function that takes another function as argument
def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{distance} {conversion_type.split(' to ')[0]} = {result} {conversion_type.split(' to ')[1]}")


# Taking input from user
distance = float(input("Enter distance value: "))

print("\n--- Distance Conversions using Lambda Functions ---")
distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_converter(distance, "feet to inches", feet_to_inches)
distance_converter(distance, "inches to cm", inches_to_cm)