import subprocess
import re
import psutil
from scapy.all import sniff, IP, TCP, UDP

def get_connected_interfaces():
    interfaces = {}
    for iface_name, iface_addrs in psutil.net_if_addrs().items():
        for addr in iface_addrs:
            if addr.family == 2:  # AF_INET (IPv4)
                interfaces[iface_name] = addr.address
    return interfaces

def list_interfaces():
    interfaces = get_connected_interfaces()
    print("Connected network interfaces:")
    interface_map = {}
    for i, (iface, ip) in enumerate(interfaces.items()):
        print(f"[{i}] {iface} - IP: {ip}")
        interface_map[i] = iface
    return interface_map

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"[+] Packet: {packet[IP].src} -> {packet[IP].dst} | Protocol: {packet[IP].proto}")
        if packet.haslayer(TCP):
            print(f"    TCP Packet | Src Port: {packet[TCP].sport} -> Dst Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    UDP Packet | Src Port: {packet[UDP].sport} -> Dst Port: {packet[UDP].dport}")

def main():
    interface_map = list_interfaces()
    if not interface_map:
        print("No active network interfaces found.")
        return
    
    selected = input("Enter interface numbers separated by commas (or press Enter to select all): ")
    if not selected.strip():
        selected_interfaces = list(interface_map.values())
    else:
        selected_indices = [int(i) for i in selected.split(',') if i.isdigit() and int(i) in interface_map]
        selected_interfaces = [interface_map[i] for i in selected_indices]
    
    print(f"Sniffing on: {', '.join(selected_interfaces)}")
    sniff(iface=selected_interfaces, prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
