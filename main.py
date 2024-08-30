userinput = float (input ("How much money ya got': " ) ) ;
nintendo = 100
affordabol = int(userinput/100)
needmoney = 100 - (nintendo%100)
print  ("You can buy ",affordabol, "nintendos")
print ("You needa hustle cuh you need \u20b1",needmoney," if ya want more  ")


if userinput < 500:
    print("You cant be using mah code broke ahh")
    for x in range(1, 5):
        print ( "get a job")
else:
    for x in range (99,0,-1):
        print(x, "Bottles of beer")
    print ("\nFactoring numbers")
    inputfactorial = int (input("Enter a number foo: "))
    factorial = 1
    for i in range(1, inputfactorial + 1):
        factorial *= i
    print ("Factorial of your number is ", factorial)
    pass;
factorcount = 0
factoring= int(input("input a number to count the factors: "))
for x in range (1,factoring+1):
    if factoring % x==0:
        factorcount + 1
        print(x ,end = ' ')

print("Factor count", factorcount)


