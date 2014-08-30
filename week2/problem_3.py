monthlyInterestRate = annualInterestRate/12.0
high = (balance * (1 + monthlyInterestRate)**12)/12.0
low = balance/12
fixedPayment2 = (high + low)/2
searching = True

def adequatePayment(balance,monthlyInterestRate,fixedPayment2):

    month = 1
    while month <= 12:
        balance -=  fixedPayment2 
        balance += monthlyInterestRate*balance 
        month += 1
    return balance

while searching:
    z = adequatePayment(balance,monthlyInterestRate,fixedPayment2)
    if  round(z) < 0:
        high = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) > 0:
        low = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) == 0:
        searching = False
        print 'Lowest Payment:',round(fixedPayment2,2)