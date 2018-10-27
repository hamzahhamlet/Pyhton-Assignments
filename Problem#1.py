# Problem: 1
# Takes the temperature in celsius and returns its value according to the condition...

temp = float(input("Enter Temperature In Celsius: "))

def temp_status(celsius):
    if celsius < -273.15:
        return "The Temperature is Invalid because it is below absolute zero."
    elif celsius == -273.15:
        return "Temperature is absolute zero."
    elif celsius > -273.15 and celsius < 0:
        return "The Temperature is below the freezing point."
    elif celsius == 0:
        return "The Temperature is at the freezing point."
    elif celsius > 0 and celsius < 100:
        return "The Temperature is in the normal range."
    elif celsius == 100:
        return "The Temperature is at the boiling point."
    else:
        return "The Temperature is above the boiling point."


result = temp_status(temp)
print(result)
