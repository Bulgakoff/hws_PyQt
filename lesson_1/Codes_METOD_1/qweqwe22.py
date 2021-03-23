import ipaddress
import subprocess

ip_addrs = []
for n in range(5):
    # ip = ipaddress.ip_address(f'192.168.0.{n}')
    ip = f'192.168.0.{n}'
    ip_addrs.append(ip)

for ip in ip_addrs:
    with subprocess.Popen(["ping", "-c1", ip]) as result:
        if result:
            print(ip, "inactive")
        else:
            print(ip, "active")
