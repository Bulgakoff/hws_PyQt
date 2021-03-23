from pprint import pprint

# Отображение словаря с вложенными словарями

dict_dicts = {
    "el_1": {"el_1.1": "val_1.1", "el_1.2": "val_1.2", "el_1.3": "val_1.3"},
    "el_2": {"el_2.1": "val_2.1", "el_2.2": "val_2.2", "el_2.3": "val_2.3"},
    "el_3": {"el_3.1": "val_3.1", "el_3.2": "val_3.2", "el_3.3": "val_3.3"},
}

print(dict_dicts)
pprint(dict_dicts)

# Отображение строки
str_pp = (
    "\n programming language Python\n type interpreted\n year 1991\n license free \n"
)
print(str_pp)
pprint(str_pp)
