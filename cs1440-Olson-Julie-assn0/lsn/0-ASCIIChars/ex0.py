def displayASCII():
    num = 32
    while (num <= 126):
        symbol = chr(num)
        f"chr({num}) = {symbol}"
        num += 1
    pass

if __name__ == '__main__':
    displayASCII()
