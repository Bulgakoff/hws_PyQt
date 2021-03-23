import subprocess

args = ["ping", "www.yndex.ru"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)

data = process.communicate()
print(data)
for line in data:
    print(f'====={line}')