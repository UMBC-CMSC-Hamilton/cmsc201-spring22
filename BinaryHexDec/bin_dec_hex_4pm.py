"""
    
    Binary Decimal and Hex
    
    Binary and Decimal
    
    we say decimal is base 10, but what do we mean by that?
    
        24 = 4 + 2 * 10
        576 = 6 + 7 * 10 + 5 * 100 (10^2)
        
        In base 10, we have 10 digits: 0, 1, 2, 3,4 ,5 ,6, 7, 8, 9
        
    What is binary?
        
        base 10 -> base 2:
        
            binary digits = "bit"
                0, 1 = bits
                
            101(b) = 1 + 4 = 5 (dec)
            1101 (bin) = 1 + 4 + 8 = 13
            0111 (bin) = 1 + 2 + 4 = 7
            
            Write out each place if there's a 1 and don't if there's a zero,
                add them up.
            
            0101 1100 (bin) = 64 + 16 + 8 + 4 = 92 (dec)
            1100 0011 (bin) = 128 + 64 + 2 + 1 = 195
            1001 1101 0010 (bin)
            4 bits together is called a nibble
            8 bits in a "word" is called a byte
            
            Counting in binary
            
            0000(b) = 0 (dec)
            0001(b) = 1 (dec)
            0010 (b) = 2 (dec) joke = there are 10 types of people, those who understand binary and those who don't
            0011 (b) = 3 (dec)
            0100 (b) = 4 (dec)
            0101 (b) = 5 (dec)
            0110 (b) = 6 (dec)
            0111 (b) = 7 (dec)
            1000 (b) = 8 (dec)
            1001 (b) = 9 (dec)
            1010 (b) = 10 (dec)
            1011 (b) = 11 (dec)
            1100 (b) = 12 (dec)
            1101 (b) = 13 (dec)
            1110 (b) = 14 (dec)
            1111 (b) = 15 (dec)
            
        While number > 0:
            number % 2 that is the new digit
            number //= 2
            
        83 (dec) ==> bin
        <-- build the number this way
        1010011
        83 (odd) ==> 41 (odd) ==> 20 (even) ==> 10 (even) ==> 5 (odd) ==> 2 (even)
            ==> 1 (odd) ==> 0 (zero, done)
        
        1010011 ==> dec
        1 + 2 + 16 + 64 = 83
        
        27 (odd) ==> 13 (odd) ==> 6 (even) ==> 3 (odd) ==> 1 (odd) ==> (0, done)
        
        11011 = 0001 1011
        1 + 2 + 8 + 16 = 27
        
        395 (odd) ==> 197 (odd) ==> 98 (even) ==> 49 (odd) ==> 24 (even)
            ==> 12 (even) ==> 6 (even) ==> 3 (odd) ==> 1 (odd) ==> 0 (done)
        0001 1000 1011
        
        1 + 2 + 8 + 128 + 256 = 395
"""

def convert_to_binary(number):
    number_string = ''
    if number == 0:
        return '0b0'
    
    while number > 0:
        number_string = str(number % 2) + number_string
        number //= 2

    return '0b' + number_string

# 1100

my_int = int(input('int: '))
while my_int != -1:
    print(convert_to_binary(my_int), bin(my_int))
    my_int = int(input('int: '))

my_bin = 0b1100
print(my_bin)


"""
    Hexadecimal = 6 + 10 = 16 = base
    
    We need digits to represent 10, 11, 12, 13, 14, 15
    10  11  12  13  14  15
    a   b   c   d   e   f
    A   B   C   D   E   F
    
    
    Hex -> Dec
    
    f3 (hex) to (dec)
    3 * 1 + f * 16 = 3 * 1 + 15 * 16 = 243 (dec)
    
    8d (hex) to (dec)
    d + 8 * 16 = 13 + 128 = 141 (dec)
    
    a5f
    f + 5 * 16 + a * 16^2
    15 + 5 * 16 + 10 * 256 = 2560 + 80 + 15 = 2655
    
    4632 (hex)
    2 + 3 * 16 + 6 * 256 + 4 * 16^3
    2 + 3 * 16 + 6 * 256 + 4 * 4096 = 17,970
    
    
    {bin} <-> {dec}
    {hex} -> {dec}
    {bin} <-> {hex} (nice)
    
         
            0000(b) = 0 (dec) = 0 (hex)
            0001(b) = 1 (dec) = 1 (hex)
            0010 (b) = 2 (dec) = 2 (hex)
            0011 (b) = 3 (dec) = 3 (hex)
            0100 (b) = 4 (dec) = 4 (hex)
            0101 (b) = 5 (dec) = 5 (hex)
            0110 (b) = 6 (dec) = 6 (hex)
            0111 (b) = 7 (dec) = 7 (hex)
            1000 (b) = 8 (dec) = 8 (hex)
            1001 (b) = 9 (dec) = 9 (hex)
            1010 (b) = 10 (dec) = a (hex)
            1011 (b) = 11 (dec) = b (hex)
            1100 (b) = 12 (dec) = c (hex)
            1101 (b) = 13 (dec) = d (hex)
            1110 (b) = 14 (dec) = e (hex)
            1111 (b) = 15 (dec) = f (hex)
            
            1101 1100 0011 1001 1011 0011 1110 1010
            dc39b3ea
            
            0101 1100 0010 0001 0000 1111
            
            5c210f
            
            abcd246 into binary
            1010 1011 1100 1101 0010 0100 0110
            
        Hex is a compact way to write binary.
        
        {dec} -> {hex}

        While number > 0:
            number % 16 that is the new digit
            number //= 16
            
        143 (dec) into hex
        
        143 % 16 = 15 ==> f digit
        143//16 ==> 8
        8 % 16 = 8 digit
        8 // 16 = 0 (end)
        <-
        8f


        2872 (dec) => hex
        mod 16 = 8, div by 16 = 179
        mod 16 = 3, div by 16 = 11
        11 mod 16 = 11 => b
        b38
        
        0b denotes binary
        0x denotes hex
"""

def convert_to_hex(number):
    number_string = ''
    
    if number == 0:
        return '0x0'
    
    while number > 0:
        
        # come back to the digit
        if 0 <= number % 16 <= 9:
            number_string = str(number % 16) + number_string
        else:
            hex_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
            number_string = hex_map[number % 16] + number_string
        number //= 16
        
    return '0x' + number_string


my_int = int(input('int: '))
while my_int != -1:
    print(convert_to_hex(my_int), hex(my_int))
    my_int = int(input('int: '))
    
    
"""
    
    bin <-> hex (table)
    hex <-> dec
    bin <-> dec

bin     hex     bin     hex     bin     hex     bin     hex
0000    0       0100    4       1000    8       1100    C (12)
0001    1       0101    5       1001    9       1101    D (13)
0010    2       0110    6       1010    A (10)  1110    E (14)
0011    3       0111    7       1011    B (11)  1111    F (15)

0xabcd
1010 1011 1100 1101

0x38a2
0011 1000 1010 0010

101 into hex
is it 0101 ? (yes) or 1010 (hint:no)
05 = 5, 5 = 50 (no i don't think so)
0101 = 5 Hex 5 dec

0110 1110 1111 0010 into hex
6EF2
"""


"""
    How to convert binary -> dec or hex -> dec
    
    
    1001 1100 0110 into dec
    2 + 4 + 64 + 128 + 256 + 2048 = 2502
    
    1011 0101
    1 + 4 + 16 + 32 + 128 = 181
    
    1001 1111
    1 + 2 + 4 + 8 + 16 + 128 = 159
    
    hex -> dec
    f9 -> dec
    15 * 16 + 9 = 249
    
    2a -> dec
    2 * 16 + 10 = 42
    
    5a3 -> dec
    5 * 256 + 10 * 16 + 3
    2560 / 2 = 1250 + 30 = 1280????????? maybe
    1280 + 160 + 3 = 1440 + 3 = 1443
    
    b is in the 4096 place
    b34d (not exam)
    11 * 4096 + 3 * 256 + 4 * 16 + 13
    40960 + 4096 + 768 + 64 + 13
    45000 + 56 + 768 + 64 + 13
    45000 + 888 + 13
    45888 + 13
    45901
"""

"""
    Hardest thing... converting dec -> bin or hex
    
    while number > 0:
        next digit = number % base (16 or 2)
        divide number by the base
        
        
    644 into binary
    
    644 (even) => 322 (even) => 161 (odd) => 80 (even) => 40 (even) => 20 (even)
    => 10 (even) => 5 (odd) => 2 (even) => 1 (odd) => 0 (zero, stop)
        number % 2 == 0, odd % 2 == 1
        
    read backwards
    0010 1000 0100
    
    512 + 128 + 4 = 644 :)
    
    842 (even) => 421 (odd) => 210 (even) => 105 (odd) => 52 (even) => 26 (even)
    => 13 (odd) => 6 (even) => 3 (odd) => 1 (odd) => (0, stop)
    
    0011 0100 1010 <-- answer
    2 + 8 + 64 + 256 + 512  = 778 + 64 = 842 <-- me checking
    
    281 into hex
    281 % 16 = 9
    281  = 256 + 16 + 9 (hint)
    17 % 16 = 1
    1 % 16 = 1
    0 % 16 = 0
    0x119
    
    289,746 => hex
    289,746 % 16 = 2
    289,746 // 16 = 18,109
    18,109 % 16 = 13
    18,109 // 16 = 1131
    1131 % 16 = 11
    1131 // 16 = 70
    70 % 16 = 6
    70 // 16 = 4
    4 % 16 = 4
    4 // 16 = 0 (stop)
    
    46(11)(13)2
    0x46bd2
    
    
"""

