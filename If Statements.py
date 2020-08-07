# example_1 = '''
# Example 1:
# if it is a hot day
# It's a hot day ,
# Drink plenty of water
# otherwise
# if it's cold It's cold day
# Wear warm clothes
# otherwise
# It's a lovely day "
# '''
# print(example_1)


is_hot = False  # True or False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Example 2



print("Example2: price of a house is 10000000, if buyer has good credit they need to put down 10% otherwise they need to put down 20%")

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment:{down_payment}")


# Example 3
# If applicant has high income AND good credit then he is Eligible for loan
# If applicant has high income OR good credit then he is Eligible for loan
#  AND: with logical AND operator all statments (conditions) must be True
#  OR: with logical OR operator at least one statments (conditions) must be True
# NOT: Inverse any Boolean value we given
has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    # print("Example 3:  If applicant has high income AND good credit then he is Eligible for loan")
    print("Eligible for loan")
else:
    print("Sorry Not Eligible for loan")

# Example4 (NOT operator): Inverse any Boolean value we given
#  If applicant has good credit AND doesn't have a criminal record then they Eligible for Loan



has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    # print("Example 3:  If applicant has high income AND good credit then he is Eligible for loan")
    print("Eligible for loan")
else:
    print("Sorry Not Eligible for loan")

if has_good_credit or not has_criminal_record:
    # print("Example 3:  If applicant has high income AND good credit then he is Eligible for loan")
    print("Eligible for loan")
else:
    print("Sorry Not Eligible for loan")