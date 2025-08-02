import tkinter as tk
from tkinter import ttk, messagebox
import threading
import speedtest

class SpeedTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speed Test GUI – BYLICKILABS")
        self.geometry("500x400")
        self.configure(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self, text="Speed Test – Download / Upload / Ping", font=("Arial", 14)).pack(pady=10)

        # Start button
        ttk.Button(self, text="▶ Start Test", command=self.start_test_thread).pack(pady=10)

        # Result labels
        self.result_frame = ttk.Frame(self)
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.ping_var = tk.StringVar(value="Ping: -")
        self.download_var = tk.StringVar(value="Download: -")
        self.upload_var = tk.StringVar(value="Upload: -")

        ttk.Label(self.result_frame, textvariable=self.ping_var, font=("Courier", 12)).pack(anchor="w", pady=5)
        ttk.Label(self.result_frame, textvariable=self.download_var, font=("Courier", 12)).pack(anchor="w", pady=5)
        ttk.Label(self.result_frame, textvariable=self.upload_var, font=("Courier", 12)).pack(anchor="w", pady=5)

        # Status text
        self.status_text = tk.Text(self, height=5, font=("Courier", 9), wrap="word")
        self.status_text.pack(fill=tk.BOTH, expand=True)

    def start_test_thread(self):
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, "Starting speed test...\n")
        threading.Thread(target=self.run_test, daemon=True).start()

    def run_test(self):
        try:
            self.status_text.insert(tk.END, "Connecting to best server...\n")
            st = speedtest.Speedtest()
            st.get_best_server()
            self.status_text.insert(tk.END, "Running download test...\n")
            download = st.download()
            self.status_text.insert(tk.END, "Running upload test...\n")
            upload = st.upload()
            ping = st.results.ping

            self.ping_var.set(f"Ping: {round(ping, 2)} ms")
            self.download_var.set(f"Download: {round(download / 1_000_000, 2)} Mbps")
            self.upload_var.set(f"Upload: {round(upload / 1_000_000, 2)} Mbps")

            self.status_text.insert(tk.END, "Test completed successfully.\n")
        except Exception as e:
            self.status_text.insert(tk.END, f"Error: {e}\n")
            messagebox.showerror("Test Failed", str(e))

if __name__ == "__main__":
    app = SpeedTestApp()
    app.mainloop()
