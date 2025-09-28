def greeting(name):
    print('Hi', name)

# Main programme
name1 = input('What\'s ya name then?\n')
greeting(name1)
name2 = input('What\'s ya name then?\n')
greeting(name2)

#Use a global variable (messy if you want to use multiple names)
#name = input('What\'s ya name guv\n')

#greeting()

#Functions manipulating numbers
def addition(a, b):
    return a + b

def main():
    num1 = float(input('Enter first number:\n'))
    num2 = float(input('Enter first number:\n'))

    #Call the function
    result = addition(num1,num2)
    print(result)

main()