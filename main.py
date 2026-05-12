import asyncio
import matplotlib.pyplot as plt
from icmplib import *

addr = "divar.ir"

def check_network():
    num = 10
    packet_loss = []
    jitter = []
    rtts = []
    for i in range(num):
        test = ping(addr, count=4, interval=0.1, timeout=1)
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
    check_network()

if __name__ == '__main__':
    main()

