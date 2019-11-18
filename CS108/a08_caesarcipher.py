# file: a08_caesarcipher.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Caesar Shift Cipher

def shift_char(c, n):
    '''
    This method is responsible for shifting an individual character.
    '''
    # Return the same char if this is not alphabet.
    if not c.isalpha():
        return c

    # Check if the char is uppercase.
    isupper = c.isupper()

    # Lower case the current char
    # This is just to simplify the processing
    # We will correct it later
    c = c.lower()

    # Get ascii value and shift it
    ascii_val = ord(c)
    new_ascii_val = ascii_val + n

    # Check if we need to do wrapping around boundaries.
    if chr(new_ascii_val) > 'z':
        new_ascii_val -= 26
    if chr(new_ascii_val) < 'a':
        new_ascii_val += 26

    # Get corresponding char and convert to upper if needed.
    new_c = chr(new_ascii_val)
    if isupper:
        new_c = new_c.upper()

    return new_c


def cipher(plaintext, n):
    # Accumulator
    ciphertext = ""

    # Traverse through the string
    for c in plaintext:
        # Shift each char and add to accumulator
        code = shift_char(c, n)
        ciphertext += code
    return ciphertext


def codebreaker(ciphertext):
    # Print the original
    print("Cipher text: %s" % ciphertext)
    print ("Here are possible decodings:")

    # Vary the shifting from 0 to 25 and print decodings.
    for i in range(26):
        decoded_text = cipher(ciphertext, i)
        print(decoded_text)
    print("\n\n")


if __name__ == '__main__':
    # Testing the shift_char method
    # Uncomment to see the results
    #print(shift_char('a', 3))
    #print(shift_char('x', 3))
    #print(shift_char('a', -2))
    #print(shift_char(' ', 5))

    # Testing the cipher method
    # Uncomment to see the results
    #print(cipher('time', 4))
    #print(cipher('welcome to the machine', 19))
    #print(cipher('This is a test String!', -6))
    #print(cipher('Hello, this is yet another test :)', -25))

    # Testing the deciphering
    # Note that how we are testing for special chars and
    # using mixing of upper-lower casing.
    codebreaker('pxevhfx mh max ftvabgx')
    codebreaker('Nbcm cm u nymn Mnlcha!')
    codebreaker('Ifmmp, uijt jt zfu bopuifs uftu :)')
