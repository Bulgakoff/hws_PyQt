import os

# Создания каталога в текущей директории
# os.mkdir("test_dir")

# Проверка существования
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")

# Проверка содержимого каталога
dir_struct = os.listdir(".")
print(dir_struct)

# Проверка на объект-каталог
dirs = [d for d in dir_struct if os.path.isdir(d)]
print(dirs)

# Проверка на объект-файл
fls = [f for f in dir_struct if os.path.isfile(f)]
print(fls)

# Определение базового типа пути
base_path = os.path.basename("c:\\system\\apps\\Python\\Python.app")
print(base_path)
base_path = os.path.basename("/etc/fstab")
print(base_path)

# Определение имени директории пути path
dir_path = os.path.dirname("c:\\system\\apps\\Python\\Python.app")
print(dir_path)
dir_path = os.path.dirname("/etc/fstab")
print(dir_path)


# Разбиение пути к файлу
dir_tuple = os.path.split("c:\\system\\apps\\Python\\Python.app")
print(dir_tuple)
dir_tuple = os.path.split("/foo/bar/baz")
print(dir_tuple)
