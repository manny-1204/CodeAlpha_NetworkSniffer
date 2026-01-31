# Network Sniffer (CodeAlpha Task)

## 📌 Project Description
This project is a Python-based **network packet sniffer** developed as part of the CodeAlpha Cyber Security internship tasks.  
The tool captures live network traffic and displays useful packet information such as source and destination IP addresses, protocols, packet size, and timestamps.

The project demonstrates a practical understanding of:
- Network traffic analysis
- Packet sniffing concepts
- Ethical use of cybersecurity tools

---

## ⚙️ Features
- Live packet capture
- Displays source IP and destination IP
- Identifies protocols (TCP, UDP, ICMP)
- Shows packet length
- Includes timestamps for each packet
- Simple and readable output
- Can be extended with a GUI or logging functionality

---

## 🛠️ Technologies Used
- **Python 3**
- **Scapy** (for packet sniffing)
- **Npcap** (required on Windows)
- **Linux / Windows** compatible

---

## ▶️ How It Works (Brief Explanation)
The sniffer uses the Scapy library to listen to network interfaces in real time.  
Each captured packet is analyzed to extract key fields such as IP addresses, protocol type, and size.  
Timestamps are added to show when each packet was captured.

---

## 🚀 How to Run the Project

### 🔹 Requirements
Install dependencies:
```bash
pip install scapy
