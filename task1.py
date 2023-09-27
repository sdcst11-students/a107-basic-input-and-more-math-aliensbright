#'''
##### Task 1 Percent Error
#Ask the user to input the following:
#* the expected number
#* the actual result
#Calculate the percent difference between the two results. Round your answer to 2 decimal places

#```
#https://www.skillsyouneed.com/num/percent-change.html

ExpNum = float(input("Enter the expected number -->"))
print(ExpNum)
ActNum = float(input("Enter the actual result -->"))
Increase = (ActNum - ExpNum)
PercentDif = Increase / ExpNum * 100
PercentDif = round(PercentDif,2)
print(f"{PercentDif}%")