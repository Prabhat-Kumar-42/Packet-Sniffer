# 📡 Packet Sniffer

## 📖 Overview
The **Packet Sniffer** is a Python-based tool that allows users to monitor network traffic in real-time. It detects active network interfaces, provides an option to select one or multiple interfaces, and captures packets flowing through them.

## ✨ Features
- 🔍 Detects and lists all active network interfaces with their IP addresses.
- 🎛️ Allows users to select specific interfaces or sniff on all interfaces.
- 📡 Captures and displays details of TCP, UDP, and IP packets.
- 💻 Compatible with **Windows** (requires Npcap) and **Linux**.

## ⚙️ Requirements
- 🐍 **Python 3.x**
- 📦 **Scapy** (`pip install scapy`)
- 📦 **Psutil** (`pip install psutil`)
- 🖥️ **Windows Users:** Install [Npcap](https://nmap.org/npcap/) (ensure **WinPcap API-compatible mode** is enabled).

## 🛠️ Installation
1. Clone this repository or download the script:
   ```sh
   git clone https://github.com/your-repo/Packet-Sniffer.git
   cd Packet-Sniffer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
1. Run the script:
   ```sh
   python packet-sniffer.py
   ```
2. Select the network interface(s) by entering their corresponding numbers, or press **Enter** to sniff on all interfaces.
3. View captured packets in the terminal in real-time.

## 📊 Example Output
```
Connected network interfaces:
[0] Wi-Fi - IP: 192.168.0.102
[1] Ethernet - IP: 192.168.1.2
Enter interface numbers separated by commas (or press Enter to select all): 0
Sniffing on: Wi-Fi
[+] Packet: 192.168.0.1 -> 192.168.0.102 | Protocol: 6 (TCP)
    TCP Packet | Src Port: 443 -> Dst Port: 53421
```

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Contributions are welcome! Feel free to submit **issues** or **pull requests** to improve this tool. 🚀

