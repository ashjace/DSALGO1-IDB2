'''
#Exercise1
money = int(input("How much money do you have: "))
nintendoWii = 100
purchasedNintendoWii = int(money / nintendoWii)
neededMoney = -((money % nintendoWii) - nintendoWii)
print ("you can buy " , purchasedNintendoWii, " piece/s of Nintendo Wiis")
print ("You need ", neededMoney, " for an additional Nintendo Wii")

'''
#############################

'''
#Exercise2
sum = 0
for x in range (1,11):
    sum += x
    print (sum , " is the sum of number 1 - 10!")

'''

'''
#Exercise3

number = int(input("Enter a number: "))
factors = [i for i in range(1, number + 1)
           if number % i == 0]

print("Factors:", factors)
print("Number of factors:", len(factors))
'''

