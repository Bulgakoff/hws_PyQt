# Табличное представление списка словарей
from tabulate import tabulate
dicts_list = [{'programming language': 'Python',
               'type': 'interpreted',
               'year': '1991'},
              {'programming language': 'JAVA',
               'type': 'compiled',
               'year': '1995'},
              {'programming language': 'С',
               'type': 'compiled',
               'year': '1972'}]

# Выравнивание по центру
print(tabulate(dicts_list, headers='keys', tablefmt="pipe", stralign="center"))

