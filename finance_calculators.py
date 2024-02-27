import math

'''The program runs two different financial calculators: an investment calculator and
   a home loan repayment calculator.
   The user can choose the calculator needed and by entering some values the program will make 
   the requested calculations. '''

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()
requested_calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#After selecting 'investment' the user can choose between 'simple interest' and 'compound interest'.
#Then the program will output the amount of interest the user will get back after the given period.
if requested_calculation == "investment":
   P = int(input("Please enter the amount of money to deposit: "))
   r = int(input("Please enter the interest rate desired: "))
   r = r/100
   t = int(input("Please enter the number of years planned for the investment: "))
   interest = input("Please enter 'simple interest' or 'compound interest': ")
   if interest == "simple interest":
       simple_interest = P *(1 + r*t)
       r = r*100
       print("After the given period at {}% of interest, you will get back {}.".format(r, simple_interest))
   if interest == "compound interest":
       compound_interest = P * math.pow((1+r),t)
       r =r*100
       print("After the given period at {}% of interest, you will get back {}.".format(r, compound_interest))

#After selecting 'bond' and entering the requested values, the user will get the monthly payment amount.
elif requested_calculation == "bond":
    P = int(input("Please enter the present value of the house: "))
    i = int(input("Please enter the interest rate desired: "))
    i = (i/100)/12
    n = int(input("Please enter the number of months over which the bond will be repaid: "))
    monthly_payment = (i * P)/(1 - (1 +i)**(-n))
    print("The monthly repayment is {}.".format(monthly_payment))

#If the user does not type in a valid input, there will be an error message.
else:
    print("Please type 'investemet' or 'bond'.")
