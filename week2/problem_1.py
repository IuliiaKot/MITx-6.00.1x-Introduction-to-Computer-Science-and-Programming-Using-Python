count = 0
for i in range(1,13):
    print "Month: ",i
    minimum_month_pay = monthlyPaymentRate*balance
    print "Minimum monthly payment:",round(minimum_month_pay,2)
    month_interest_rate =  annualInterestRate/ 12.0
    month_unpaid_balance = balance - minimum_month_pay
    balance = month_unpaid_balance + month_interest_rate * month_unpaid_balance
    print "Remaining balance:", round(balance,2)
    count = count + minimum_month_pay 
print "Total paid:", round(count,2)
print "Remaining balance:", round(balance,2)