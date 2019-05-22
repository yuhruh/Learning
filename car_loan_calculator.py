# ask the loan amount
# the Annual Percentage Rate (APR)
# the loan duartion

#use pyhton 2

while True:
    name = raw_input('Welcome to Mortgage Calculator! Enter your name: ')
    if len(name) > 0:
        try:    
            int(name)
            print('Make sure to use a valid name.')
        except ValueError:
            print "Hi, ", name.capitalize()
            break
    else:
        print 'Make sure to use a valid name.'
        
while True:
    while True:
        loan_amount = raw_input('Please enter your loan amount: ')
        if len(loan_amount) == 0 or loan_amount.isdigit() == False or float(loan_amount) <= 0:
            print 'Must enter positive number!'
        else:
            break
    
    while True:
        interest_rate = raw_input("What's the interest rate? \nExample: 5 for 5% or 2.5 for 2.5%\n")
        try:                      #delete if len(interest_rate) > 0 since float(interest_rate) can be detected error once type space!
            if float(interest_rate) <= 0:
                print 'Must enter positive number!'
            else:
                break
        except ValueError:
            print 'Must enter positive number!'
        
    while True:
        loan_duration = raw_input("What's your loan duration?(in years)\n")
        if len(loan_duration) == 0 or loan_duration.isdigit() == False or float(loan_duration) <= 0:
            print 'Must enter positive number!'
        else:
            break
    
    interest_rate = float(interest_rate) / 100
    monthly_interest_rate = interest_rate / 12
    months = float(loan_duration) * 12

    monthly_payment = float(loan_amount) * (monthly_interest_rate / (1 - (1 + monthly_interest_rate)**-months))
    print "Your monthly payment is: {:.2f}".format(monthly_payment)
    
    
    answer = raw_input("Do you want to perform another calculation? (Y to calculate again or press any key to leave!)\n")
    if answer.lower() == 'y':
        print "Let's do it again!"
    else:
        break
            
print 'Thank you for using the Mortgage Calculator!\nSee you!'
