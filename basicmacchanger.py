#!/usr/bin/env python
import subprocess
import optparse
import re


# This script is designed to change the mac address of a network device on your linux computer.


def get_arguments():
    # Options for interface & new MAC address
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[!] Please Specify an Interface. Use --help for more info.")
    elif not options.new_mac:
        # code to handle error
        parser.error("[!] Please Specify a MAC address. Use --help for more info.")
    return options


def change_mac(interface, new_mac):
    # Brings the specified interface down, changes its MAC address, and brings it back up.
    print("[~] Changing MAC address of", interface, "to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[!] Could not read MAC address!")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
# change_mac(options.interface, options.new_mac)

