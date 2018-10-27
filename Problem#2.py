# Problem: 2
# Takes a number between 0 to 35 and returns its alphanumeric number.

number = int(input("Enter A Number: "))

def num_to_alpha(number):
    if number >= 0 and number <= 9:
        print("The Number is: " , number)
    elif number >=10 and number <=35:
        print(chr(number+55))
    else:
        print("The Number cannot be greater than 35 and less than 0")

num_to_alpha(number)
