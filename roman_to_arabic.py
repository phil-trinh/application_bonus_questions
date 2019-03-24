def roman_to_arabic(roman_num):
    arabic_num = 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    while roman_num:
        current_num = roman_dict[roman_num[0]]
        try:
            next_num = roman_dict[roman_num[1]]

            if next_num > current_num:
                arabic_num += next_num - current_num
                roman_num = roman_num[2:]
            else:
                arabic_num += current_num
        except:
            arabic_num += current_num
        finally:
            roman_num = roman_num[1:]

    return arabic_num


print(roman_to_arabic("MDCCLXXVI"))
