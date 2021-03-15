import scapy.all as scapy
import argparse
import re, uuid
import requests
import argparse

def merge_two_dicts(dictOne, dictTwo):
    dictThree = dictOne.copy()
    dictThree.update(dictTwo)
    return dictThree

def get_mac_details(mac_address):
	url = "https://api.macvendors.com/"
	response = requests.get(url+mac_address)
	if response.status_code != 200:
		raise Exception("[!] Invalid MAC Address!")
	return response.content.decode()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    return  options

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[0].psrc, "mac": element[1].hwsrc}
        value=client_dict["mac"]
        mac_address = value
        try:
            vendor_name = get_mac_details(mac_address)
            #print("[+] Device vendor is "+vendor_name)
            vendor_dict = {"Vendor":vendor_name}
        except:
            print("[!] An error occured. Check "
            "your Internet connection.")

        new_dict = merge_two_dicts(client_dict , vendor_dict)
        client_list.append(new_dict)

    return client_list

def print_result(scan_list):
    print("IP\t\t\tMAC\t\t\t\tManufacturer\n------------------------------------------------------------------------------")
    for client in scan_list:
        print(client["ip"] + "\t\t" + client["mac"] + "\t\t" + client["Vendor"])


#scan("192.168.0.0/24")
options = get_arguments()
result_list = scan(options.target)
print_result(result_list)
