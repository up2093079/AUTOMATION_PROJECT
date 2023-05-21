
from netmiko import ConnectHandler
import re
from getpass import getpass
import warnings
warnings.filterwarnings(action='ignore',module='paramiko.*')
from project_devices import csr_pe_rtr1,csr_pe_rtr2,csr_pe_rtr3,csr_pe_rtr4,veos_pe_rtr6,veos_pe_rtr7
csr_commands = ['show bgp vpnv4 unicast all','show run vrf']

project_devices_csr = [csr_pe_rtr1,csr_pe_rtr2,csr_pe_rtr3,csr_pe_rtr4]
project_devices_veos = [veos_pe_rtr6,veos_pe_rtr7]
for my_devices in project_devices_csr:
	yott_csr_conn = ConnectHandler(**my_devices)
	print(yott_csr_conn.find_prompt())
	yott_csr_conn.enable()
	print(yott_csr_conn.send_command('show bgp vpnv4 unicast all'))

for my_devices in project_devices_veos:
	yott_veos_conn = ConnectHandler(**my_devices)
	print(yott_veos_conn.find_prompt())
	#yott_veos_conn.enable()
	print(yott_veos_conn.send_command('show bgp vpn-ipv4 rd 65000:3'))
