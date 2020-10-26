
## Base cases uses the recursive property of our number system
units={'0':'','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

teens={'10':'ten', '20':'twenty', '11':'eleven', '12':'twelve','13':'thirteen','14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}

tens={'0':'','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}

tens2={'1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}


## could be easily extended higher with more data though for any practical purpose I can envisage it is big enough already!!!!
## https://en.wikipedia.org/wiki/Power_of_10
numDigits={3:'thousand', 6:'million',9:'billion', 12:'trillion', 15:'quadrillion',18:'quintillion', 21:'sextillion', 24:'septillion', 27:'octillion', 30:'nonillion',33:'decillion ', 36:'undecillion',39:'duodecillion',42:'tredecillion', 45:'quattuordecillion', 48:'quindecillion', 51:'sexdecillion'}

powers={1:'thousand', 2:'million',3:'billion', 4:'trillion', 5:'quadrillion',6:'quintillion', 7:'sextillion', 8:'septillion', 9:'octillion', 10:'nonillion', 11:'decillion', 12:'undecillion',13:'duodecillion',14:'tredecillion', 15:'quattuordecillion', 16:'quindecillion', 17:'sexdecillion'}


def readFile(FileName):
    if '.txt' in FileName:
        file1 = open(FileName, 'r')
    else:
        file1 = open(FileName + '.txt', 'r')
    Lines = file1.readlines()
    Numbers = []
    for line in Lines:
        Numbers.append(getWords(line))
    vals = []
    val = {}
    i = 1
    for number in Numbers:
        val[i] = []
        if number == 'number invalid':
            vals.append('number invalid')
            val[i].append('number invalid')

        else:
            for num in number:
                vals.append(getNumber(num))
                val[i].append(getNumber(num))
        string = ''
        i += 1
    for key in val.keys():
        print('line', key, 'contains', val[key])
    return val


# readFile('Ass.txt')

x = 'I received 23 456,9 KGs. '


## Treats no number as an invald number
def getWords(text):
    words = []
    for word in text.split(' '):
        if any(char.isdigit() for char in word) and word.isdigit() == False:
            return ['number invalid']
        if word.strip() != '' and word.isdigit() == True:
            words.append((word.strip()))
    return words


x = 'I received 23 456,9 KGs. '


def getWords(text):
    words = []
    for word in text.split(' '):
        if any(char.isdigit() for char in word) and word.isdigit() == False:
            return 'number invalid'
        if word.strip() != '' and word.isdigit() == True:
            words.append(word.strip())
    if len(words) == 0:
        return 'number invalid'
    return words


## This function does a lot of the heavy lifting

def threeDigits(threeDigitNumber):
    if threeDigitNumber == '':
        return ''
    if threeDigitNumber == '000':
        return ''
    if threeDigitNumber == '100':
        return 'one hundred'
    if threeDigitNumber[1] == '0' and threeDigitNumber[2] == '0':
        return units[threeDigitNumber[0]] + ' hundred'
    if threeDigitNumber[0] == '0':
        if threeDigitNumber[1] == '0':
            return units[threeDigitNumber[2]]
        elif threeDigitNumber[1] == '1':
            return teens[threeDigitNumber[1:]]
        else:
            if threeDigitNumber[2] == '0':
                return tens2[threeDigitNumber[1]]
            else:
                return tens2[threeDigitNumber[1]] + '-' + units[threeDigitNumber[2]]
    if threeDigitNumber[1] == '0' and threeDigitNumber[0] == '0':
        return units[threeDigitNumber[0]] + ' hundred'
    val = units[threeDigitNumber[0]] + ' hundred and '
    if threeDigitNumber[1] == '0':
        return val + units[threeDigitNumber[2]]
    else:
        if threeDigitNumber[2] == '0':
            return val + tens[threeDigitNumber[1] + '0']
        if threeDigitNumber[1] == '1':
            return val + teens[threeDigitNumber[1:]]
        else:
            return val + tens2[threeDigitNumber[1]] + '-' + units[threeDigitNumber[2]]


def fourDigits(fourDigitNumber):
    if fourDigitNumber[0] == '0':
        return threeDigits(fourDigitNumber[1:])
    if fourDigitNumber[1] == '0':
        return threeDigits(makeLengthMultipleOfThree(fourDigitNumber[0])) + ' thousand and ' + threeDigits(
            fourDigitNumber[1:])
    else:
        return threeDigits(makeLengthMultipleOfThree(fourDigitNumber[0])) + ' thousand, ' + threeDigits(
            fourDigitNumber[1:])


def getCoefs(Number):
    if Number == '':
        return 'number invalid'
    Number = Number[::-1]
    ## invert the digit orderings
    # Number=Number[::-1]
    if Number == '':
        return 'zero'
    Digits = len(Number)
    if Digits < 4:
        return threeDigits(Number[0:3])
    bases = list(numDigits.keys())
    bases = sorted(bases)
    word = ''
    vals = [0]
    for i in bases:
        if i < Digits:
            vals.append(i)
    vals = sorted(vals)
    coefs = []
    for i in (range(len(vals) - 1)):
        coefs.insert(0, threeDigits(Number[vals[i]:vals[i + 1]][::-1]))
    coefs.insert(0, threeDigits(makeLengthMultipleOfThree(Number[vals[len(vals) - 1]:len(Number)][::-1])))

    return coefs


## mainly just formatting to add commas etc...

def getNumber(Number):
    Number = Number.lstrip('0')
    if len(Number) > 52:
        return 'invalid number: too big'
    if Number == '':
        return 'zero'
    Digits = len(Number)
    if Digits < 4:
        return threeDigits(makeLengthMultipleOfThree(Number[0:3]))

    if Digits == 4:
        return fourDigits(Number)

    coefs = getCoefs(Number)
    Number = ''

    pows = []

    for i in range(1, len(coefs)):
        pows.append(powers[i])

    pows = pows[::-1]
    for i in range(0, len(coefs) - 1):
        if coefs[i] == '':
            continue
        if 'zero' in coefs[i]:
            Number += 'and'
            continue
        Number += coefs[i] + ' ' + pows[i] + ', '

    if len(coefs[len(coefs) - 1].split(' ')) < 3:
        Number = Number.rstrip(', ') + ' and ' + coefs[len(coefs) - 1]
    else:
        Number = Number + coefs[len(coefs) - 1]

    Number = Number.strip(' ')

    if len(Number) > 4:
        if Number[-4:] == ' and':
            Number = Number[:-4]
    return Number


def makeLengthMultipleOfThree(number):
    if len(number) % 3 == 0:
        return number
    if len(number) % 3 == 1:
        return '00' + number
    if len(number) % 3 == 2:
        return '0' + number
    return False

