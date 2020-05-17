sample_string = input("Введіть свій рядок\n")
string_number = len(sample_string)

if string_number < 2:
    print("")
else:
    print(sample_string[:2] + sample_string[-2:])