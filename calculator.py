# ask the user for two numbers
# ask the user for an operation to perform
# perform the operation on the two numbers
# output the results
# use python 2


while True:
    name = raw_input('Welcome to Calculator! Enter your name: ')
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
        number1 = raw_input("What's the first number: ")
        if number1.isdigit() == True:
            break
        else:
            print "Hmm... that does't look like a valid number"
    
    while True:    
        number2 = raw_input("What's the second number: ")
        if number2.isdigit() == True:
            break
        else:
            print "Hmm... that does't look like a valid number"
        
    while True:
        user_input = raw_input("what operation would you like to perform?\n 1) add\n 2) substract\n 3) multiply\n 4) divide\n" ) 
        operation = ['1', '2', '3', '4']
        if user_input in operation:
            if user_input == '1':
                print 'Adding the two numbers....'
                result = float(number1) + float(number2)
                print 'The result is ', result
                break
            elif user_input == '2':
                print 'Substracting the two numbers....'
                result = float(number1) - float(number2)
                print 'The result is ', result
                break
            elif user_input == '3':
                print 'Multiplying the two numbers....'
                result = float(number1) * float(number2)
                print 'The result is ', result
                break
            elif user_input == '4':
                print 'Dividing the two numbers....'
                if number2 == '0':
                    print "Please input valid number, zero can't be in denominator(the second number)!"
                    break
                else:
                    result = float(number1) / float(number2)
                    print 'The result is ', result
                    break
        else:
            print "Must choose 1, 2, 3 or 4"
            
    answer =raw_input("Do you want to perform another calculation? (Y to calculate again)\n")
    if answer.lower() == 'y':
        print "Let's do it again!"
    elif answer.lower() == 'n':
        break
    
print 'Thank you for using the calculator! See you again~'