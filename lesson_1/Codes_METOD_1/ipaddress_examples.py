import ipaddress

# Создание IPv4-адреса - функция ip_address()
ipv4 = ipaddress.ip_address("192.168.0.1")
# print(dir(ipv4))

# Проверка диапазона, к которому принадлежит адрес - атрибуты is_loopback,
# is_multicast, is_reserved, is_private
print(ipv4.is_loopback)
print(ipv4.is_multicast)
print(ipv4.is_reserved)
print(ipv4.is_private)

# Операции с объектом адреса
ip1 = ipaddress.ip_address("192.168.1.0")
ip2 = ipaddress.ip_address("192.168.1.255")

if ip2 > ip1:
    print("compare", True)

print("str(ip1)", str(ip1))
print("int(ip1)", int(ip1))
print(ip1 + 5)
print(ip1 - 5)

# Создание объекта, описывающего сеть - функция ip_network()
subnet = ipaddress.ip_network("80.0.1.0/28")
ba = subnet.broadcast_address
print("broadcast_address", ba)

# Просмотр всех хостов для объекта-сети
print("hosts", list(subnet.hosts()), len(list(subnet.hosts())))

# Разбиение сети на подсети
print("subnets", list(subnet.subnets()))

# Обращение к люьому адресу в сети
print(subnet[1])

# Создание интерфейса
ipv4_int = ipaddress.ip_interface("10.0.1.1/24")

# Получение адреса
print("ip", ipv4_int.ip)
# Получение маски
print("netmask", ipv4_int.netmask)
# Получение сети
print("network", ipv4_int.network)
