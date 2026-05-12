# 📡 Network Monitor

A simple Python tool to measure and visualize network performance using ICMP (ping).

## 📊 What It Tracks

* ✅ RTT (latency)
* ✅ Jitter
* ✅ Packet loss

---

## 🚀 Features

* Easy-to-use CLI
* Visual graphs using matplotlib
* Customizable target host and test parameters

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/soite/Ppping.git
cd Ppping
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run with default settings

```bash
python monitor.py
```

### Run with custom options

```bash
python monitor.py --host google.com --tests 10 --count 4
```

---

## ⚙️ Arguments

| Argument  | Description           | Default  |
| --------- | --------------------- | -------- |
| `--host`  | Target domain or IP   | divar.ir |
| `--tests` | Number of test rounds | 10       |
| `--count` | Pings per round       | 4        |

---

## 📈 Example Output

The script opens a window with three graphs:

1. RTT (ms)
2. Jitter (ms)
3. Packet Loss (%)

---

## 🖼️ Screenshots

```md
## 🖼️ Screenshots
### RTT
![test](https://raw.githubusercontent.com/soite/Ppping/master/screenshots/rtt.png)
### Jitter
![test](https://raw.githubusercontent.com/soite/Ppping/master/screenshots/jitter.png)
### Packet Loss
![test](https://raw.githubusercontent.com/soite/Ppping/master/screenshots/packet_loss.png)
```

---

## 🛠️ Requirements

* Python 3.8+
* See `requirements.txt`

---

## 📁 Project Structure

```
Ppping/
│
├── monitor.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 💡 Future Improvements

* Save results to CSV
* Real-time monitoring
* Web dashboard (Flask or Streamlit)