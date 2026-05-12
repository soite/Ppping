📡 Network Monitor

A simple Python tool to measure and visualize network performance using ICMP (ping).

It tracks:

✅ RTT (latency)
✅ Jitter
✅ Packet loss
🚀 Features
Easy-to-use CLI
Visual graphs using matplotlib
Customizable target host and test parameters
📦 Installation

Clone the repository:

git clone https://github.com/yourusername/network-monitor.git
cd network-monitor

Install dependencies:

pip install -r requirements.txt
▶️ Usage

Run the script with default settings:

python monitor.py

Run with custom options:

python monitor.py --host google.com --tests 10 --count 4
Arguments
Argument	Description	Default
--host	Target domain or IP	divar.ir
--tests	Number of test rounds	10
--count	Number of pings per round	4
📊 Example Output

The script will open a window with 3 graphs:

RTT (ms)
Jitter (ms)
Packet Loss (%)