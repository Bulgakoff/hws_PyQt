# Табличное представление списка словарей
from tabulate import tabulate

tuples_list = [
    ("Python", "interpreted", "1991"),
    ("JAVA", "compiled", "1995"),
    ("С", "compiled", "1972"),
]

columns = ["programming language", "type", "year"]
# Указание заголовков в параметре headers
table = tabulate(tuples_list, headers=columns)
print(table)
