# This Python file uses the following encoding: utf-8

'''
Задача 3 (1.25т.)
Напишете функция is_valid, приемаща license_plate - низ, съдържащ български регистрационен номер на превозно средство. Тя трябва да провери дали номерът е валиден и да върне или областта на регистрация, или съобщение за грешка.

Приемаме, че всички валидни номера са във формат AA0000AA или A0000AA, където A означава буква, а 0 - цифра. В license_plate може буквите да са малки, трябва да се погрижите да ги преобразувате към главни. Позволените букви от кирилицата може да намерите в даденото от нас множество ALLOWED_LETTERS. Номерът е валиден, ако всичките му букви са позволени. (Ако са подадени на латиница, за простота нека считаме номерът за невалиден. Иначе ако имплементираме такава система в реалния свят ще е хубаво да се обръщат от латиница в кирилица :) ) Буквата/буквите преди цифрите трябва да съответстват на реигонален код на област в България, което може да проверите чрез речника REGION_CODES.

Функцията да връща две стойности (в tuple), спрямо валидността на номера:

Случай 1: номерът е валиден: връща True и областта, в която е регистрирано превозното средство
Случай 2: номерът не е валиден: връща False и текст за грешка, който е един от следните:
"Невалиден формат" - когато форматът не съответства на гореописаните два
"Невалидни букви" - когато бъдат подадени букви, които не са позволени
"Невалиден регионален код" - когато буквите преди цифрите не съответстват на реигонален код на област в България
(Забележка: няма да бъдат подавани специални номера, като такива на автомобили от Българската армия (ВА000000), електрически (ЕА...), дипломатически и др.)

За проверка дали даден str съдържа само цифри, използвайте str.isdigit().

За проверка дали даден str съдържа само букви, използвайте str.isalpha().

Hint: За по-лесно (ако не ви се въртят цикли), може да използвате някои от операторите |, &, <= , които изпълнени върху две множества са съотв. операциите обединение, сечение и подмножество.
'''

INVALID_FORMAT_MSG = "Невалиден формат"
INVALID_LETTERS_MSG = "Невалидни букви"
INVALID_CODE_MSG = "Невалиден регионален код"

ALLOWED_LETTERS = set("АВЕКМНОРСТУХ")

REGION_CODES = {
    "Е": "Благоевград",
    "А": "Бургас",
    "В": "Варна",
    "ВТ": "Велико Търново",
    "ВН": "Видин",
    "ВР": "Враца",
    "ЕВ": "Габрово",
    "ТХ": "Добрич",
    "К": "Кърджали",
    "КН": "Кюстендил",
    "ОВ": "Ловеч",
    "М": "Монтана",
    "РА": "Пазарджик",
    "РК": "Перник",
    "ЕН": "Плевен",
    "РВ": "Пловдив",
    "РР": "Разград",
    "Р": "Русе",
    "СС": "Силистра",
    "СН": "Сливен",
    "СМ": "Смолян",
    "СО": "София (област)",
    "С": "София (столица)",
    "СА": "София (столица)",
    "СВ": "София (столица)",
    "СТ": "Стара Загора",
    "Т": "Търговище",
    "Х": "Хасково",
    "Н": "Шумен",
    "У": "Ямбол",
}


def is_valid(license_plate):
    if len(license_plate) == 7:
        regional_code = license_plate[:1]
        numbers = license_plate[1:5]
        trail_letters = license_plate[5:]
    elif len(license_plate) == 8:
        regional_code = license_plate[:2]
        numbers = license_plate[2:6]
        trail_letters = license_plate[6:]
    else:
        return False, INVALID_FORMAT_MSG

    regional_code = regional_code.upper()

    if not (regional_code.isalpha() and numbers.isdigit() and trail_letters.isalpha()):
        return False, INVALID_FORMAT_MSG

    if not ((set(regional_code) | set(trail_letters)) <= ALLOWED_LETTERS):
        return False, INVALID_LETTERS_MSG

    if regional_code not in REGION_CODES.keys():
        return False, INVALID_CODE_MSG

    return True, REGION_CODES[regional_code]

assert is_valid("СА1234АВ") == (True, "София (столица)")
assert is_valid("С1234АВ") == (True, "София (столица)")
assert is_valid("ТХ0000ТХ") == (True, "Добрич")
assert is_valid("ТХ000ТХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000Т") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000ТХХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("У8888СТ") == (True, "Ямбол")
assert is_valid("Y8888CT") == (False, INVALID_LETTERS_MSG)
assert is_valid("ПЛ7777АА") == (False, INVALID_LETTERS_MSG)
assert is_valid("РВ7777БВ") == (False, INVALID_LETTERS_MSG)
assert is_valid("ВВ6666КН") == (False, INVALID_CODE_MSG)

print("✅ All OK! +1.25 points")
