def listOfChars(intList):
    lst = []
    pos = 0
    for i in intList:
        lst.append(chr(intList[pos]))
        pos = pos + 1
    return lst


if __name__ == '__main__':
    provided = [
        65,
        32,
        115,
        104,
        111,
        114,
        116,
        32,
        115,
        101,
        110,
        116,
        101,
        110,
        99,
        101,
        46
    ]

    # Returns a list of strings to result
    result = listOfChars(provided)

    # The following block of code turns the list `result` into a string `resultStr`
    # Do not modify!
    resultStr = ""
    for char in result:
        resultStr += char
    print(resultStr)
