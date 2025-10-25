name_seller=input()
fixeed_salary=float(input())
total_sales=float(input())

def calcular_salary(fixeed_salary, total_sales):
    salary_total=fixeed_salary+(total_sales*0.15)
    return salary_total

calc=calcular_salary(fixeed_salary, total_sales)
print(f"TOTAL = R$ {calc:.2f}")