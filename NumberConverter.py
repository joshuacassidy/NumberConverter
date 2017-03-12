import math
import os

def Convert():
    x = []

    def clear():
        if os.name != 'nt':
            os.system('clear')
        else:
            os.system('cls')

    hexlibrary = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    def ConvertedToAns():
        x.reverse()
        convertedNumber = ''.join(str(joinNum) for joinNum in x)
        print ("{} converted to {} is {}".format(num,NumberType,convertedNumber))
    def ConvertedFromAns():
        initialNum = ''.join(str(joinNum) for joinNum in num)
        print ("{} converted to {} is {}".format(initialNum,NumberType,sum(out)))

    while True:
        clear()
        choice = input('Would you like to convert your number to To or From Decimal? ')
        NumberType = input('Would you like you number converted {} Binary,Octal or Hex? '.format(choice))

        if choice.lower() == 'to' and NumberType.lower() == 'binary':
            num = int(input("Enter a number to be converted: "))
            out = num
            convert = num
            while True:
                if int(convert) > 0:
                    out = convert % 2
                    x.append(math.floor(out))
                    convert = convert / 2
                else:
                    ConvertedToAns()
                    break
            break

        elif choice.lower() == 'from' and NumberType.lower() == 'binary':
                num = int(input("Enter a number to be converted."))
                num = [int(toArray) for toArray in str(num)]
                out = []
                num.reverse()
                for i in range(len(num  )-1, -1, -1):
                    x = (num[i] * (2 ** i))
                    out.append(x)
                ConvertedFromAns()
                break


        elif choice.lower() == 'to' and NumberType.lower() == 'octal':
            num = int(input("Enter a number to be converted: "))
            out = num
            convert = num
            while True:
                if int(convert) > 0:
                    out = convert % 8
                    x.append(math.floor(out))
                    convert = convert / 8
                else:
                    ConvertedToAns()
                    break
            break

        elif choice.lower() == 'from' and NumberType.lower() == 'octal':
            num = int(input("Enter a number to be converted."))
            num = [int(toArray) for toArray in str(num)]
            out = []

            num.reverse()
            for i in range(len(num  )-1, -1, -1):
                x = (num[i] * (8 ** i))
                out.append(x)
            ConvertedFromAns()
            break

        elif choice.lower() == 'to' and NumberType.lower() == 'hex' or NumberType.lower() == 'hexadecimal':
            num = int(input("Enter a number to be converted: "))
            out = num
            convert = num
            while True:
                if int(convert) > 0:
                    out = convert % 16
                    x.append(math.floor(out))

                    convert = convert / 16
                else:
                    for replace,index in enumerate(x):
                        x[replace]=hexlibrary[index]
                    ConvertedToAns()
                    break
            break

        elif choice.lower() == 'from' and NumberType.lower() == 'hex' or NumberType.lower() == 'hexadecimal':
            num = input("Enter a number to be converted.")
            out = []
            num = [str(toArray) for toArray in str(num.lower())]
            x =[]
            hexmap = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
            '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
            y = []
            for index,replace in enumerate(num):
                y = hexmap[replace]
                x.append(y)
            x.reverse()
            for i in range(len(x)-1, -1, -1):
                z = (x[i] * (16 ** i))
                out.append(z)
            ConvertedFromAns()
            break
        else:
            print('You cannot convert a number {} {}'.format(choice,NumberType))
            break
Convert()
