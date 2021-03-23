# Табличное представление списка словарей
from tabulate import tabulate

dicts_list = [
    {"programming language": "Python", "type": "interpreted", "year": "1991"},
    {"programming language": "JAVA", "type": "compiled", "year": "1995"},
    {"programming language": "С", "type": "compiled", "year": "1972"},
]

# grid-формат
print(tabulate(dicts_list, headers="keys", tablefmt="grid"))
print()

# markdown-формат
print(tabulate(dicts_list, headers="keys", tablefmt="pipe"))
print()

# html-формат
html_table = tabulate(dicts_list, headers="keys", tablefmt="html")
print(html_table)
print()

print(tabulate(dicts_list, headers="keys", tablefmt="psql"))


# github

print('github-формат')# github-формат
github_table = tabulate(dicts_list, headers="keys", tablefmt="github")
print(github_table)
print()


print(tabulate(dicts_list, headers="keys", tablefmt="tsv"))

print(tabulate(dicts_list, headers='keys', tablefmt="pipe", stralign="center"))

