"""
    Binary Hex and Decimal
    
    6 things we know how to do
    
    {bin} <-> {hex}
        Easy one because we have a table that does 99.99% of the work
    {bin} <=> {dec}
    {hex} <=> {dec}
    Bin     Hex     Bin     Hex     Bin     Hex     Bin     Hex
    0000    0       0100    4       1000    8       1100    C (12)
    0001    1       0101    5       1001    9       1101    D (13)
    0010    2       0110    6       1010    A (10)  1110    E (14)
    0011    3       0111    7       1011    B (11)  1111    F (15)

    1011 1101 0101 1000 0111 0000 0000 0010 1100
    BD587002C

    af53
    1010 1111 0101 0011
    
    93a2
    1001 0011 1010 0010
    
    1101 1000 0010 0110 1101 1001 0000 1111
    d826d90f
    
"""

"""
    {bin, hex} -> {dec}
    
    bin not as bad you just add up the places
    
    short = 2 bytes
    regular int = 4 bytes
    long int = 8 bytes
    
    1000 0110 1010 0110
    2 + 4 + 32 + 128 + 512 + 1024 + 32768
    = 34,470
    
    1100 0101
    1 + 4 + 64 + 128 = 197
    
    0110 0111
    1 + 2 + 4 + 32 + 64 = 103
    
    Hex into decimal works basically the same way.
    ab12f9 = do not convert this by hand
    
    f9 = more testable
    f = 15
    15 * 16 + 9 = 249
    
    3a = 3 * 16 + 10 = 58
    
    ba7 = b * 256 + a * 16 + 7
        = 11 * 256 + 10 * 16 + 7
        = 10 * 256 + 256 + 160 + 7
        = 2560 + 256 + 160 + 7
        = 2560 + 416 + 7
        = 2560 + 423
        = 2983
        
    7dc2 = 7 * 4096 + 13 (256) + 12 (16) + 2
         = 32194

    {hex} <-> {bin}
    {hex} -> {dec}
    {bin} -> {dec}
"""


"""
    dec -> bin
    
    while number > 0:
        number % base becomes the next digit
        divide the number by the base
        
    725 into binary
        base = 2
    
    725 (odd) => 362 (even) => 181 (odd) => 90 (even) => 45 (odd) => 22 (even)
    => 11 (odd) => 5(odd) => 2(even) => 1 (odd) => (0, stop)
    0010 1101 0101
    1 + 4 + 16 + 64 + 128 + 512
    
    282 (even) => 141 (odd) => 70 (even) => 35 (odd) => 17 (odd) => 8 (even)
    => 4 (even) => 2(even) => 1 (odd) => 0 (stop)
    0001 0001 1010
    
    Go backwards only to check if i'm actually right.
    2 + 8 + 16 + 256 = 282 yes
   
   
   dec -> hex
        How do we do this?
        
        Mod by 16 to get the next digit, divide by 16 to get the next number.
        
        322 into hex.
        322 mod 16 ?
        0x22
        
        581 into hex
        0x245
"""

"""
    Why do we care about all this?
    
    Let's say we have four switches, you have to represent them with one varible

    
    switch_one = True
    switch_two = False
"""

switch_code = 0b0111
print(switch_code)
if switch_code & 0b1000:
    print('switch one is on')
if switch_code & 0b0100:
    print('switch two is on')
if switch_code & 0b0010:
    print('switch three is on')
if switch_code & 0b0001:
    print('switch four is on')


print(bin(0b101101 ^ 0b011100))


def get_letters(a_string):
    if not a_string:
        return []
    
    # if it didn't return, it's non-empty
    
    first_letter = a_string[0]
    # a_string[1:] = a_string[1: len(a_string)] taking everything but the
    # first letter.
    # notice that i'm putting the letter itself into a list
    # maintain the same type that comes out of get_letters
    return [first_letter] + get_letters(a_string[1:])


def remove_all_z(the_z_string):
    if not the_z_string:
        return ''
    
    if the_z_string[0] == 'z':
        return remove_all_z(the_z_string[1:])
    else:
        return the_z_string[0] + remove_all_z(the_z_string[1:])
    



the_string = input('Tell me a string: ')
# print(list(the_string))
print(remove_all_z(the_string))

