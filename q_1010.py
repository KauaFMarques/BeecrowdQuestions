"""
In this problem, the task is to read a code of a product 1,
 the number of units of product 1, 
 the price for one unit of product 1, 

 the code of a product 2, 
 the number of units of product 2,
 the price for one unit of product 2. 
After this, calculate and show the amount to be paid.
"""
code1, number1, price1 = input().split()
code2, number2, price2 = input().split()

total = (int(number1) * float(price1)) + (int(number2) * float(price2))
print(f"VALOR A PAGAR: R$ {total:.2f}")