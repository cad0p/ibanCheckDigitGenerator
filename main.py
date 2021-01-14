
def ibanCheckDigitGenerator(iban):
    """
    https://en.wikipedia.org/wiki/International_Bank_Account_Number

    :param iban: The iban with the check digits set to 00.
    :return: The iban with the right check digits.
    """
    iban3 = iban[4:] + iban[:4]
    iban4 = ''
    for char in iban3:
        if char.isdigit():
            iban4 += char
        else:
            iban4 += str(ord(char) - 55)
    print(f'iban4: {iban4}')
    iban5 = int(iban4)
    remainder6 = iban5 % 97
    print(f'remainder6: {remainder6}')
    checkDigits7 = 98 - remainder6
    print(f'checkDigits7: {checkDigits7}')
    iban = iban[:2] + str(checkDigits7) + iban[4:]
    return iban


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_iban = ibanCheckDigitGenerator('IT00ZZZ0000092194430341')
    print(my_iban)
