import threading
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# GUI setup
window = tk.Tk()
window.title("Advanced Network Sniffer - CodeAlpha")
window.geometry("800x500")

text_area = ScrolledText(window, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

def log(message):
    text_area.insert(tk.END, message + "\n")
    text_area.see(tk.END)

def packet_handler(packet):
    if IP in packet:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = packet[IP].src
        dst = packet[IP].dst

        if TCP in packet:
            proto = "TCP"
        elif UDP in packet:
            proto = "UDP"
        elif ICMP in packet:
            proto = "ICMP"
        else:
            proto = "OTHER"

        log(f"[{time}] {src} → {dst} | {proto}")

def start_sniffing():
    log("Sniffing started...\n")
    sniff(prn=packet_handler, store=False)

button = tk.Button(window, text="Start Sniffing", command=lambda: threading.Thread(target=start_sniffing).start())
button.pack(pady=10)

window.mainloop()

