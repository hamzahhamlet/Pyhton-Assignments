# Problem: 6

totalCookies = int(input("Enter Total Number Of Cookies: "))
boxCookies = int(input("Number Of Cookies in a Box: "))
container = int(input("Number Of Boxes in a Container: "))
print("")
number_Of_Boxes = 0
number_Of_Containers = 0
leftover_cookies = 0
leftover_boxes = 0

if boxCookies >= 12:
    number_Of_Boxes = totalCookies//boxCookies
    print("Number Of Boxes:", number_Of_Boxes)
    leftover_cookies = totalCookies%boxCookies
    print("Left-Over Cookies:", leftover_cookies)
else:
    print("The Number Of Cookies in a box can't be less then 12!")


if container >= 24:
    number_Of_Containers = number_Of_Boxes//container
    print("Number Of Containers:", number_Of_Containers)
    leftover_boxes = number_Of_Boxes%container
    print("Left-Over Boxes: ", leftover_boxes)
else:
    print("The Number Of Containers can't be less then 24!")



