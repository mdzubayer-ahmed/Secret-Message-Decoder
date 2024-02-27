'''
The cipher value: 10111110
The secret message: https://www.youtube.com/watch?v=Dlto1VQ5Fv4

Extracting text from a hashcode
@Author: Md. Zubayer Ahmed
Student ID: 202160438
mzahmed@mun.ca
Comp-2002, Fall-2023
'''

# split_32bit_to_8bit(number) will take a number then make it a 32 bit binary number and split it in four 8-bit binary numbers and return the list of these four numbers
def split_32bit_to_8bit(number):
    binary_32bit = bin(number)[2:]
    split_to_8bit = [binary_32bit[i:i+8] for i in range(0, 32, 8)]
    return split_to_8bit

# xor_8bit_binary(bin_str1, bin_str2) will take two 8-bit binary numbers in string format do bitwise xor, then turn the result binary number to it's corresponding integer value, and return it
def xor_8bit_binary(bin_str1, bin_str2):
    result = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(bin_str1, bin_str2))
    xor_result = int(result, 2)
    return xor_result

# The goal of find_cipher(number) is to take an integer number, try to decode it using all possible cipher code and see which values actuall works. This will reduce the work of looking into 2816 possible values to 256 values only.Further since I can't really understand if tha's the ctualvalue so we filtered out the value which are not A-z
def find_cipher(number):
    binary_rep = split_32bit_to_8bit(number)
    for i in range(256):
        curr_cipher = format(i, '08b')
        message = ""
        for j in range(len(binary_rep)):
            message_num = xor_8bit_binary(curr_cipher, binary_rep[j])
            if message_num >= ord("A") and message_num <= ord("z"):
                message = message + (chr(message_num))
        if message != "" and len(message) == 4:
            print(curr_cipher)
            print(message)
#Turned out that "10111110" gives us "http", so it's more likely to be the cipher. let's try it out
def main():
    numbers = [3603614414, 3448017297, 3385444752, 3352415178, 3420248976, 3721515921, 3386886877, 3598829699, 4208118481, 2414407563, 4173892254]
    find_cipher(numbers[0])
    cipher = "10111110"
    full_message = ""
    for num in numbers:
        binary_representation = split_32bit_to_8bit(num)
        word =""
        for i in range(len(binary_representation)):
            num_char = xor_8bit_binary(cipher, binary_representation[i])
            word = word + (chr(num_char))
        full_message = full_message + word
    print("The Secret message is: " + full_message.strip())
    print("And the Cipher value used was: " + cipher)

main()