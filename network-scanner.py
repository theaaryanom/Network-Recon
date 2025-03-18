#!/usr/bin/env python3
import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Automated Network Scanner")
    parser.add_argument("-t", "--target", dest="target", help="Target IP range to scan (e.g., 192.168.1.1/24)")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP range. Use --help for more info.")
    return options

def scan_network(ip_range):
    # Create an ARP request packet
    arp_request = scapy.ARP(pdst=ip_range)
    # Create an Ethernet frame to broadcast the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the ARP request and Ethernet frame
    arp_request_broadcast = broadcast / arp_request
    # Send the packet and receive the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Parse the response and extract device information
    devices = []
    for element in answered_list:
        device = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices.append(device)
    return devices

def display_results(devices):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    # Get the target IP range from the user
    options = get_arguments()
    target_ip_range = options.target

    print(f"[+] Scanning network {target_ip_range}...\n")
    # Scan the network and get the list of devices
    connected_devices = scan_network(target_ip_range)
    # Display the results
    display_results(connected_devices)
