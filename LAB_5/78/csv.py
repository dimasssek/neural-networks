import csv
import locale
import re
from collections import OrderedDict

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)


def convert_to_seconds(time_string):
    time_units = {'дн': 86400, 'час': 3600, 'мин': 60, 'сек': 1, 'ч': 3600}
    pattern = r'(\d+)\s+(\w+)\.?\s*'
    matches = re.findall(pattern, time_string)
    total_seconds = 0
    for match in matches:
        value, unit = int(match[0]), match[1]
        total_seconds += value * time_units[unit]
    return total_seconds


dict = {}

with open("1 - 2.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")

    header = next(file_reader)
    end_index = header.index('Затраченное время')
    surname_index = header.index('Фамилия')
    name_index = header.index('Имя')

    for row in file_reader:
        end = " ".join(str(row[end_index]).split())
        surname = str(row[surname_index])
        name = str(row[name_index])
        surname = surname + " " + name
        dict[surname] = end

dict.popitem()
dict.popitem()

new_dictionary = {}
for key, value in dict.items():
    new_dictionary[key] = convert_to_seconds(value)

sorted_dictionary = OrderedDict(sorted(new_dictionary.items(), key=lambda x: x[1]))

sorted_dictionary_formatted = {}
for key in sorted_dictionary:
    sorted_dictionary_formatted[key] = dict[key]

for key, value in sorted_dictionary_formatted.items():
    print(f'{key}: {value}')