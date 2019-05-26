import sys
# check for valid input

if len(sys.argv) == 2:
    try:
        int(sys.argv[1])
        if(len(str(sys.argv[1])) == 16):
            pass
        else:
            print("Not 16 digits!")
            sys.exit()
    except ValueError:
        print('Not an integer!')
        sys.exit()
else:
    print('Not enough or too many command line arguments! \n Proper use \"python Check.py <credit card number here> \" ')
    sys.exit()

def main():
    # put the digits into a list
    number = convertToList(sys.argv[1])
    sum = cardCheck(number)
    if (sum%10 == 0):
        print('Valid Card!')
    else:
        print('Invalid Card!')

#converts initial passed int variable to list
def convertToList(num):
    numStr = str(num)
    numList = []
    for digit in numStr:
        numList.append(int(digit))
    return (numList)

def cardCheck(digitList, count = 0):
    sum = 0
    #if digit is every second digit multiply by 2
    if(count%2 == 0 & count < 15):
        digitList[count] = (digitList[count] * 2)
        #if is 2 digit number after multiplication
        if(digitList[count] >= 10):
            digitList[count] = addDigits(digitList[count])
            cardCheck(digitList, count + 1)
        else:
            cardCheck(digitList, count + 1)
    #progresses program
    elif(count < 15):
        cardCheck(digitList, count + 1)
    else:
        return 0
    for digits in digitList:
        sum += int(digits)
    return sum

#resolve 2 digit number conflict by adding the digits of the number and returning it
def addDigits(num):
    list = str(num)
    sum = 0
    for digits in list:
        sum += int(digits)
    return sum

if __name__ == '__main__':
        main()
