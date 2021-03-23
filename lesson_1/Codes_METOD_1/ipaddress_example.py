import ipaddress

ip_1 = '10.0.1.1/24'
ip_2 = '10.0.1.0/24'

def ip_network_check(ip_addr):
    try:
        ipaddress.ip_network(ip_addr)
        return True
    except ValueError:
        return False

print(ip_network_check(ip_1))
print(ip_network_check(ip_2))