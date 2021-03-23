# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля subprocess (UNIX) --------------

import subprocess

# Выполнить простую системную команду с помощью os.system()
# ret = subprocess.call("ls -l", shell=True)

# Выполнить простую команду, игнорируя все, что она выводит
# ret = subprocess.call("rm –f *.tmp", shell=True, stdout=open("/dev/null"))

# Выполнить системную команду, но сохранить ее вывод
# p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
# out = p.stdout.read()
# print(f'out == {out}')

# Выполнить команду, передать ей входные данные и сохранить вывод
p = subprocess.Popen(
    "wc",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
out, err = p.communicate(b"aaa bbb\n ccc ddd")  # Передать строку s дочернему процессу
print(out)

# Создать два дочерних процесса и связать их каналом
p1 = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen("wc", shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
out = p2.stdout.read()
print("pipe", out)
