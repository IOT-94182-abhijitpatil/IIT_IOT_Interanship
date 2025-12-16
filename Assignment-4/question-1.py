# conversion functions
def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inches):
    return inches * 2.54


# Function that performs conversion
def distance_conversion(distance, conv_type, conv_func):
    result = conv_func(distance)
    print(f"{distance} {conv_type} = {result}")


# main program
distance = float(input("Enter distance: "))

distance_conversion(distance, "km to m", km_to_m)
distance_conversion(distance, "m to cm", m_to_cm)
distance_conversion(distance, "cm to mm", cm_to_mm)
distance_conversion(distance, "feet to inches", feet_to_inches)
distance_conversion(distance, "inches to cm", inches_to_cm)
