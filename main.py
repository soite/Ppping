import asyncio
from icmplib import *

def check_network():
    ans = asyncio.run(async_ping("quera.org", count=1000, timeout=2, interval=0.1))
    print(ans)

def main():
    check_network()

if __name__ == '__main__':
    main()

