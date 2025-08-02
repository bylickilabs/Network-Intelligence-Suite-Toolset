
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from scapy.all import sniff, hexdump
import threading
import datetime

class PacketSnifferGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PacketSniffer GUI")
        self.geometry("900x600")
        self.running = False
        self.captured_packets = []
        self.create_widgets()

    def create_widgets(self):
        control_frame = ttk.Frame(self, padding=10)
        control_frame.pack(fill=tk.X)

        ttk.Label(control_frame, text="Filter (BPF):").pack(side=tk.LEFT)
        self.filter_entry = ttk.Entry(control_frame, width=40)
        self.filter_entry.pack(side=tk.LEFT, padx=5)
        self.filter_entry.insert(0, "tcp")

        ttk.Button(control_frame, text="Start", command=self.start_sniffing).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Stop", command=self.stop_sniffing).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Export PCAP", command=self.export_pcap).pack(side=tk.LEFT, padx=5)

        self.output = scrolledtext.ScrolledText(self, font=("Courier", 9))
        self.output.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def start_sniffing(self):
        if not self.running:
            self.running = True
            self.captured_packets = []
            self.output.insert(tk.END, f"=== Sniffing started at {datetime.datetime.now()} ===\n")
            thread = threading.Thread(target=self.sniff_packets, daemon=True)
            thread.start()

    def stop_sniffing(self):
        self.running = False
        self.output.insert(tk.END, f"=== Sniffing stopped at {datetime.datetime.now()} ===\n")

    def sniff_packets(self):
        sniff(filter=self.filter_entry.get(), prn=self.process_packet, store=0)

    def process_packet(self, packet):
        if not self.running:
            return
        self.captured_packets.append(packet)
        summary = packet.summary()
        self.output.insert(tk.END, summary + "\n")
        self.output.see(tk.END)

    def export_pcap(self):
        if not self.captured_packets:
            self.output.insert(tk.END, "No packets to export.\n")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".pcap", filetypes=[("PCAP files", "*.pcap")])
        if filename:
            from scapy.utils import wrpcap
            wrpcap(filename, self.captured_packets)
            self.output.insert(tk.END, f"Saved capture to: {filename}\n")

if __name__ == "__main__":
    app = PacketSnifferGUI()
    app.mainloop()
