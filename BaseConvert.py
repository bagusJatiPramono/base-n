

def branch(num,type1,type2):
    match type1:
        case "biner":
            if type2 == "hexadesimal":
                print(num + " dalam " + type2  + " adalah " + toHex(num,2))                 
            elif type2 == "desimal":
                print(num + " dalam " + type2  + " adalah " + toDec(num,2))   
        case "desimal":
            if type2 == "hexadesimal":
                print(num + " dalam " + type2  + " adalah " + toHex(num,10))
            if type2 == "biner":
                print(num + " dalam " + type2  + " adalah " + toBinary(num,10))
        case "hexadesimal":
            if type2 == "desimal":
                print(num + " dalam " + type2  + " adalah " + toDec(num,16))
            if type2 == "biner":
                print(num + " dalam " + type2  + " adalah " + toBinary(num,16))

def toBinary(number, type):
    result = ""
    if type == 10:
        number = int(number)
        while number > 0:
            rem = number % 2
            number = number // 2
            result  += str(rem)
        result = reverse(result)
    if type == 16:
        number = toDec(number,16)
        result = toBinary(number,10)
    return result

def toHex(number,type):
    result = ""
    if type == 10:
        number = int(number)
        while number > 0:
            rem = number % 16
            number = number // 16
            result  += str(base16(rem))
        result = reverse(result)
    elif type == 2:
        number = toDec(number,2)
        result = toHex(number,10)
    return result

def toDec(number,type):
    res = 0
    number = str(number)
    for i in number:
        res = res*type + int(base16(i))
    return str(res)





def base16(ch):
    try:
        ch = int(ch)
        if (0<=ch<=9):
            return ch
        elif ch == 10:
            return "A"
        elif ch == 11:
            return "B"
        elif ch == 12:
            return "C"
        elif ch == 13:
            return "D"
        elif ch == 14:
            return "E"
        elif ch == 15:
            return "F"
    except:
        if ch == "A":
            return 10
        elif ch == "B":
            return 11
        elif ch == "C":
            return 12
        elif ch == "D":
            return 13
        elif ch == "E":
            return 14
        elif ch == "F":
            return 15


def reverse(result):
    res = result
    rev = ""
    for i in range(len(result)):
        rev += res[-i-1]
    return rev


print("masukkan angka yang ingin di konversi")
num = str(input())
print("apa basis bilangan tersebut?")
type1 = input()
print("apa basis yang ingin didapatkan?")
type2 = input()

branch(num,type1,type2)