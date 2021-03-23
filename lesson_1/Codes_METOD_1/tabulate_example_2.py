# Табличное представление списка словарей
from tabulate import tabulate

tuples_list = [
    ("programming language", "type", "year"),
    ("Python", "interpreted", "1991"),
    ("JAVA", "compiled", "1995"),
    ("С", "compiled", "1972"),
]

# Указание первой строки таблицы как набора заголовков
print(tabulate(tuples_list, headers="firstrow"))
