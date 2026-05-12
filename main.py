import argparse
import matplotlib.pyplot as plt
from icmplib import *


def check_network_plot(addr, num, ping_count):
    packet_loss = []
    jitter = []
    rtts = []
    for i in range(num):
        test = ping(addr, count=ping_count, interval=0.1, timeout=1)
        packet_loss.append(test.packet_loss)
        jitter.append(test.jitter * 1000)
        rtts.append(test.avg_rtt * 1000 if test.avg_rtt is not None else 0)
    rtt_diff = [0] + [rtts[i] - rtts[i - 1] for i in range(1, len(rtts))]
    fig, ax = plt.subplots(3,1, figsize=(10,10))

    #plot rtt
    ax[0].plot(rtts, marker='o', label='rtt')
    ax[0].set_title('rtt over ping tests')
    ax[0].set_ylabel('rtt (ms)')
    ax[0].grid(True)
    #plot jitter
    ax[1].plot(jitter, marker='o', label='jitter')
    ax[1].set_title('jitter over ping tests')
    ax[1].set_ylabel('jitter (ms)')
    ax[1].grid(True)
    #plot packet loss
    ax[2].plot(packet_loss, marker='o', label='packet_loss')
    ax[2].set_title('packet over ping tests')
    ax[2].set_ylabel('packet loss (%)')
    ax[2].grid(True)

    for axx in ax:
        axx.set_xticks(range(num))

    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='ICMP ping test')
    parser.add_argument("--host", default="google.com", help="Target host")
    parser.add_argument("--tests", type=int, default=10, help="Number of tests to run")
    parser.add_argument("--ping_count", type=int, default=4, help="Number of pings per test")
    args = parser.parse_args()
    check_network_plot(args.host, args.tests, args.ping_count)

if __name__ == '__main__':
    main()

