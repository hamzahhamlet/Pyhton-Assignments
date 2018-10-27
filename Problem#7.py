# Problem: 7

print("{:^50}".format("The Right-Angled Triangle"))

length_1 = int(input("Enter the length of Side-1: "))
length_2 = int(input("Enter the length of Side-2: "))
length_3 = int(input("Enter the length of Side-3: "))


def rightTriangle(side1,side2,side3):
    side1 = pow(side1,2)
    side2 = pow(side2,2)
    side3 = pow(side3,2)
    if side1 + side2 == side3:
        return True
    elif side1 + side3 == side2:
        return True
    elif side2 + side3 == side1:
        return True
    elif side3 + side1 == side2:
        return True
    else:
        return False



right_angle_triangle = rightTriangle(length_1, length_2, length_3)
print("")
if right_angle_triangle == True:
    print("Congratulations, Its a Right-Angled Triangle.")
else:
    print("Sorry! Try Again, Its not a Right-Angled Triangle.")