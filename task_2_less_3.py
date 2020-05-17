phone_number = input("Введіть номер телефону:\n")
i = 0
mistakes_less_numbers = 10 - len(phone_number)
mistakes_more_numbers = len(phone_number) - 10


if phone_number.isdecimal():
    if len(phone_number) == 10:
        print("Дякуємо, ви все вірно ввели")
    elif len(phone_number) < 10:
        print(f"Ви ввели лише {len(phone_number)} знаків, не вистачає {mistakes_less_numbers}")
    else:
        print(f"Ви ввели аж {len(phone_number)} знаків, тобто на {mistakes_more_numbers} більше")
else:
    print("У введеному номері не всі символи є цифрами")
