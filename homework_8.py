class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        ips_reversed = list()
        for value in self._ipList:
            value = value.split(".")
            value.reverse()
            ips_reversed.append(".".join(value))
        return ips_reversed

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        ips_without_first_octets = list()
        for value in self._ipList:
            value = value.split(".")  # или value = value.split(".", 1)[1]
            del value[0]              # ips_without_first_octets.append(".".join(value))
            ips_without_first_octets.append(".".join(value))
        return ips_without_first_octets

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        ips_with_last_octets = list()
        for value in self._ipList:
            value = value.split(".")[-1]
            ips_with_last_octets.append(value)
        return ips_with_last_octets


a = IpHandler(['10.11.12.13', '127.0.0.1', '34.54.0.10', "10.11.14.13"])
print(a.ipList)
print(a.reverse_IP())
print(a.get_oct_1_3())
print(a.get_oct_3())


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_unit_name):
        self._unit_name = new_unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_mac_address):
        self._mac_address = new_mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        self._ip_address = new_ip_address

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password


conn = ConnHandler()

conn.unit_name = 'server'
print(conn.unit_name)

conn.mac_address = '10.11.12.13'
print(conn.mac_address)

conn.ip_address = '127.0.0.1'
print(conn.ip_address)

conn.login = 'administrator'
print(conn.login)

conn.password = 'sAd@45js,9R'
print(conn.password)



my_str = '10.11.12.13'
print(my_str.split(".", 1))






