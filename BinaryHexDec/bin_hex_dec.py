"""

    all memory is stored in bits = 0 or 1 / off or on / 3.3 V or 0V
    
    Numbers can be represented in any base. Pick a number, 52.(dec)
    
    How do you represent it in binary?
    
        Choose each "binary digit" to be either 0 or 1.  Bit = Binary digIT
        
        We can string them together just like digits
        
        00110011 - what the heck is it?
        
        In base 10, 581 = 5 * 100 + 8 * 10 + 1 * 1
        5 * b^2 + 10 * b + 1
        10 = b,
        
        It works "exactly the same" except b = 2
        
        101(bin) = 5(dec)
        
        1 * 2^2 + 0 * 2^1 + 1 * 2^0
        4 + 0 + 1 = 5
    
        101 = 1    0    1
              fours place
                   twos place
                        ones place
        
        1101(bin)
        
        = 8 + 4 + 0 + 1 = 13 (dec)
        
        0110 1101 (4 bits == nibble)
                  (8 bits = byte)
                    kilobyte, megabyte, gigabyte, terabyte, petabyte, exabyte
                    
        1 + 4 + 8 + 32 + 64 = 109 (dec)
        
        1111 1111
        
        1 + 2 + 4 + 8  + 16 + 32 + 64 + 128 = 255
        
        0000 (bin) = 0 (dec)
        0001 (bin) = 1 (dec)
        0010 (bin) = 2 (dec) ==> joke = "There are 10 (bin/dec) kinds of people"
        0011 (bin) = 3 (dec)
        0100 (bin) = 4 (dec)
        0101 (bin) = 5 (dec)
        0110 (bin) = 6 (dec)
        0111 (bin) = 7 (dec)
        1000 (bin) = 8 (dec)
        1001 (bin) = 9 (dec)
        1010 (bin) = 10 (dec)
        1011 (bin) = 11 (dec)
        1100 (bin) = 12 (dec)
        1101 (bin) = 13 (dec)
        1110 (bin) = 14 (dec)
        1111 (bin) = 15 (dec)
        
        
    Let's pretend we know how to convert bin -> dec
    
        Wait, how do you convert dec-> bin?
        
    
        75 into binary.
        
        1001011 ==> 1001 011 or 100 1011 (this one)
                               0100 1011
        
        mod 75 % 2 == 1 (first digit on the right)
        divide by 2 (integer divide)
        75 // 2 => 37
        mod 37 by 2 == 1
        divide by 2 ==> 18
        mod 18 by 2 == 0
        divide 18 // 2 == > 9
        mod 9 by 2 == 1
        divide 9 by 2 == 4
        4 mod 2 == 0
        divide 4 by 2 == 2
        2 mod 2 == 0
        divide 2 by 2 == 1
        1 mod 2 == 1
        
        We know we're finished because:
            1 // 2 == 0 and that's it.
            
    Algorithm while number != 0:
        mod by 2 that's the new digit
        int-divide by 2.
        
    11 (dec) into binary
        <-- build this way
        1011
    11 (odd) ==> 5 (odd) ==> 2 (even) ==> 1 (odd) ==> 0 (zero, the end)
    
    28 into binary
        0001 1100 = 16 + 8 + 4? yep it is :)
    28 (even) ==> 14 (even) ==> 7 (odd) ==> 3 (odd) ==> 1 (odd)

    189 into binary
    
        1011 1101
    
    189 (odd) ==> 94 (even) ==> 47 (odd) ==> 23 (odd) ==> 11 (odd) ==> 5(odd)
        ==> 2 (even) ==> 1 (odd) ==> 0(stop)
"""

def convert_to_bin(number):
    number_string = ''
    
    if number == 0:
        return '0b0'
    
    while number > 0:
        if number % 2:
            number_string = '1' + number_string
        else:
            number_string = '0' + number_string
        
        number //= 2
        
    return '0b' + number_string


number = int(input('number: '))
while number != -1:
    print(bin(number), convert_to_bin(number))
    number = int(input('number: '))
    

my_var = 0b11
print(my_var)


"""
    What the hex is hex?
        Hexadecimal = 6 + 10 = 16 = base
    
        Reason = 16 = 2^4
        Every block of 4 bits can be represented as a single "hexadecimal digit"
        
        Need new digits to represent 10, 11, 12, 13, 14, 15 (Dec)
                                     a,  b , c,  d,  e,  f
                                     A,  B,  C,  D,  E,  F
                                     not case sensitive
        
        
        { bin } <-> {dec}
        
        {hex} -> {dec}
        {hex} -> {bin}
        
        
        0000 (bin) = 0 (dec) = 0 (hex)
        0001 (bin) = 1 (dec) = 1 (hex)
        0010 (bin) = 2 (dec) = 2 (hex)
        0011 (bin) = 3 (dec) = 3 (hex)
        0100 (bin) = 4 (dec) = 4 (hex)
        0101 (bin) = 5 (dec) = 5 (hex)
        0110 (bin) = 6 (dec) = 6 (hex)
        0111 (bin) = 7 (dec) = 7 (hex)
        1000 (bin) = 8 (dec) = 8 (hex)
        1001 (bin) = 9 (dec) = 9 (hex)
        1010 (bin) = 10 (dec)= a (hex)
        1011 (bin) = 11 (dec)= b (hex)
        1100 (bin) = 12 (dec)= c (hex)
        1101 (bin) = 13 (dec)= d (hex)
        1110 (bin) = 14 (dec)= e (hex)
        1111 (bin) = 15 (dec)= f (hex)
        
        {bin} <-> {hex}
        
        0101 1100 0111 1001 1101 1111 1011
        5c79dfb
        
        {hex} -> {dec}
        each place is a power of 16
        12a (hex) into dec
        a = 10
        10 + 2 * 16 + 1 * 16^2
        10+32+256 = 298
        
        df43 into dec?
        3 + 4 * 16 + 15 * 16^2 + 13 * 16^3
        = 57,155 (dec)
        
        12345 (hex) = 5 + 4 * 16 + 3 * 256 + 2 * 4096 + 1 * 65536 = 74565
        
        3 hex-digits is the limit.
        
        Want to convert {dec} -> {hex}
        
        Steal the binary algorithm.
"""


def convert_to_hex(number):
    number_string = ''
    
    if number == 0:
        return '0x0'
    
    while number > 0:
        if 0 <= number % 16 <= 9:
            number_string = str(number % 16) + number_string
        else:
            hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
            number_string = hex_dict[number % 16] + number_string
        
        number //= 16
    
    return '0x' + number_string


number = int(input('number: '))
while number != -1:
    print(hex(number), convert_to_hex(number))
    number = int(input('number: '))


"""
    0x48
    
    72 into hex
    mod 72 by 16 i think it's 8
    get 4,
    
    Convert 583 (dec) into hex
    583 % 16 = 7
    583 // 16 = 36
    36 % 16 = 4
    36 // 16 = 2
    2 % 16 = 2
    2 // 16 == 0 (done)
    
    0x247
"""
