#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_list = list(roman_string)
    rom_num = rom[rom_list[0]]
    i = 1
    while (i < len(rom_list)):
        if (rom_list[i - 1] == "I") and (rom_list[i] == ("X" or "V")):
            rom_num -= 2
        rom_num += rom[rom_list[i]]
        i += 1
    return rom_num
