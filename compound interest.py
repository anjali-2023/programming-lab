# calculate compund interest
p_amt: float = float(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest :"))
num = float(input("Enter the number of years : "))
amt =(p_amt * (1 + rate / 100) ** num)
print("The Amount is :",amt)
comp_int= float(amt-p_amt)
print("The compound interest annually is : ",comp_int)







































































