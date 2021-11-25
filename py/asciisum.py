def asciisum(str):
    value = 2
    list = str.strip()
    for i in list: value += ord(i)
    return value

if __name__ == '__main__':
    print("Password: 'password'")
    print("Ascii Sum:", asciisum("password"))