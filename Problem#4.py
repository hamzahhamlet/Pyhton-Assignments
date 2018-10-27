# Problem: 4
# Time

current_hour = int(input("Enter Hour: "))
check = int(input("Is the hour in AM or PM? (1/2): "))
increment = int(input("How many hours into the future do you want to go: "))

if check == 1:
    check = True
elif check == 2:
    check = False
else:
    print("Error")

for i in range(0,increment):
    current_hour += 1
    if current_hour > 12:
        check = not check
        current_hour = 1

if check == True:
    print(current_hour,"AM")
elif check == False:
    print(current_hour,"PM")