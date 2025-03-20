# import collections
import time
import socket
import psutil
import keyboard
from bytes2human import bytes2human

def calcsize(rate, postfix = ""):
    return "{0}{1}".format(bytes2human(rate), postfix)

## svmem = collections.namedtuple('svmem', ['total', 'available', 'percent', 'used', 'free'])

def netspeed(interface):
    dt = 1

    t0 = time.time()

    try:
        counter = psutil.net_io_counters(pernic=True)[interface]
    except KeyError:
        return []

    tot = (counter.bytes_sent, counter.bytes_recv)
    while True:
        last_tot = tot
        time.sleep(dt)
        try:
            counter = psutil.net_io_counters(pernic=True)[interface]
        except KeyError:
            break
        t1 = time.time()
        tot = (counter.bytes_sent, counter.bytes_recv)
        ul, dl = [
            (now - last) / (t1 - t0)
            for now, last
            in zip(tot, last_tot)
        ]
        t0 = time.time()
        return [int(ul), int(dl)]

def ipAddress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return [hostname, IPAddr]

def storageSize(drive):
    # import shutil
    # usage = shutil.disk_usage(drive)
    usage = psutil.disk_usage(drive)
    return usage

def ramUsage():
    # total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    # return [free_memory, used_memory, total_memory]
    return psutil.virtual_memory()

def cpuUsage():
    return psutil.cpu_percent(5)
