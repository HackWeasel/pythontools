#!/usr/bin/env python
import subprocess
import optparse

#This script is designed to change the MAC address of a network interface in linux.


def get_arguments():
    #Options for interface & new MAC address
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    #Brings the specified interface down, changes its MAC address, and brings it back up.
    print("[+] Changing MAC address of", interface, "to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
