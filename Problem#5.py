# Problem: 5

print("{:^50}".format("The New Development Scheme"))

colonial_price = int(input("Base price for Colonial: "))
colonial_area = int(input("Total area for Colonial: "))

splitEntry_price = int(input("\nBase price for Split-Entry: "))
splitEntry_area = int(input("Total area for Split-Entry: "))

singleStory_price = int(input("\nBase price for Single-Story: "))
singleStory_area = int(input("Total area for Single-Story: "))

price_per_squareFootList = []

def house(basePrice, finishedArea):
    square_foot = basePrice/finishedArea
    price_per_squareFootList.append(square_foot)


house(colonial_price, colonial_area)
house(splitEntry_price, splitEntry_area)
house(singleStory_price, singleStory_area)


if min(price_per_squareFootList) == price_per_squareFootList[0]:
    print("\nThe Colonial Model has the least price per square foot:" , min(price_per_squareFootList))
elif min(price_per_squareFootList) == price_per_squareFootList[1]:
    print("\nThe Single-Entry Model has the least price per square foot:", min(price_per_squareFootList))
elif min(price_per_squareFootList) == price_per_squareFootList[2]:
    print("\nThe Single-Story Model has the least price per square foot:", min(price_per_squareFootList))