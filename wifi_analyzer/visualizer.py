import random

def plot_channel_usage(ax, networks):
    channel_map = {}
    for net in networks:
        try:
            ch = int(net.get("Channel"))
            channel_map[ch] = channel_map.get(ch, 0) + 1
        except:
            continue
    if channel_map:
        x = sorted(channel_map.keys())
        y = [channel_map[ch] for ch in x]
        base_colors = [
            "tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple",
            "tab:brown", "tab:pink", "tab:gray", "tab:olive", "tab:cyan"
        ]
        colors = [base_colors[i % len(base_colors)] for i in range(len(x))]
        ax.bar(x, y, color=colors, width=1.2, edgecolor='black', linewidth=2)
        ax.set_title("Channel Usage")
        ax.set_xlabel("Channel")
        ax.set_ylabel("Networks")
        ax.grid(True)
    else:
        ax.set_title("No channel data available")
