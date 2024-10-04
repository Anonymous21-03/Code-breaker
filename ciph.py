def caesar(code):
    print("Welcome to Caesar Cipher Code Breaker!!\n")
    print("***************************************\n")
    ans = input("Do you know the key? y/n: ").lower()
    decode = [''] * len(code)
    
    if ans == 'y':
        key = int(input("Enter the key: "))
        for i in range(len(code)):
            if code[i] == ' ':
                decode[i] = code[i]
            elif 'a' <= code[i] <= 'z':
                shifted = ord(code[i]) + key
                if shifted < ord('a'):
                    decode[i] = chr(shifted + 26)
                elif shifted > ord('z'):
                    decode[i] = chr(shifted - 26)
                else:
                    decode[i] = chr(shifted)
            elif 'A' <= code[i] <= 'Z':
                shifted = ord(code[i]) + key
                if shifted < ord('A'):
                    decode[i] = chr(shifted + 26)
                elif shifted > ord('Z'):
                    decode[i] = chr(shifted - 26)
                else:
                    decode[i] = chr(shifted)
        print("The decoded code is: " + ''.join(decode))

    elif ans == 'n':
        for key in range(-26, 0):
            for i in range(len(code)):
                if code[i] == ' ':
                    decode[i] = code[i]
                elif 'a' <= code[i] <= 'z':
                    shifted = ord(code[i]) + key
                    if shifted < ord('a'):
                        decode[i] = chr(shifted + 26)
                    elif shifted > ord('z'):
                        decode[i] = chr(shifted - 26)
                    else:
                        decode[i] = chr(shifted)
                elif 'A' <= code[i] <= 'Z':
                    shifted = ord(code[i]) + key
                    if shifted < ord('A'):
                        decode[i] = chr(shifted + 26)
                    elif shifted > ord('Z'):
                        decode[i] = chr(shifted - 26)
                    else:
                        decode[i] = chr(shifted)

            if key >= -26 and key <= -13:
                print(f"The possible decoded code for key= {26 + key} is: {''.join(decode)}\n")
            if key > -13 and key <= 0:
                print(f"The possible decoded code for key= {key} is: {''.join(decode)}\n")


def transpose(code):
    print("Welcome to Transposition Code Breaker!!\n")
    print("***************************************\n")
    trans1 = [[''] * 5 for _ in range(5)]
    i = 0

    for j in range(5):
        for k in range(5):
            if i < len(code):
                trans1[j][k] = code[i]
                i += 1

    print("The message is: ", end="")
    for j in range(5):
        for k in range(5):
            if trans1[k][j]:
                print(trans1[k][j], end="")
    print("\n")


def atbash(code):
    print("Welcome to Atbash Code Breaker!!\n")
    print("***************************************\n")
    decode = [''] * len(code)

    for i in range(len(code)):
        if code[i] == ' ':
            decode[i] = code[i]
        elif 'a' <= code[i] <= 'z':
            decode[i] = chr(122 - ord(code[i]) + 97)
        elif 'A' <= code[i] <= 'Z':
            decode[i] = chr(90 - ord(code[i]) + 65)

    print("The decoded code is: " + ''.join(decode))


def main():
    print("\t\t\tWelcome to the Code Breaker!\n")
    print("\t\t\t****************************\n")
    code = input("Enter the text to be decoded here: ")

    print("Which type of cipher code is it?: \n1. Caesar cipher\n2. Transposition\n3. Atbash\n4. Try All")
    type_ = int(input("Enter the type here: "))
    print()

    if type_ == 1:
        caesar(code)
    elif type_ == 2:
        transpose(code)
    elif type_ == 3:
        atbash(code)
    elif type_ == 4:
        caesar(code)
        transpose(code)
        atbash(code)
    else:
        print("Enter a valid option.\n")


if __name__ == "__main__":
    main()
