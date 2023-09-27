#!python3

# Canada Income Tax Calculator part I

#'''
#It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
#Python to determine Federal and Provincial Income Tax.

#The Canadian income tax system is a tiered system, which means you pay different percentages of
#your income for different parts of your income.
#You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
#20.5% on amounts over 49020 that are less than 98040
#26% on amounts over 98040 but less than 151978
#29% on amounts over 151978 but less than 216511
#33% on amounts over 216511

#Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

#Example:
#Enter your income: 125000
#Your federal income tax is: 24411.7

#'''
income = float(input("Enter your income amount-->"))
x26 = income - 98040
#x205 = 98040-49020
x205 = 49020
x15 = 49020
IncomeTax = 0.15*49020 + .205*49020 + .26*x26
IncomeTax = round(IncomeTax,2)
print(f"Your federal income tax is ${IncomeTax}")
