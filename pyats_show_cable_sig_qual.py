from genie.testbed import load
import time
from datetime import datetime
import csv

tb = load('yaml/cbr8_testbed.yaml')

print("\n")
print('################################################################################################')
print('    pyATS - show cable signal-quality mer                                                       ')
print('    - Generates a csv file with US MER values                                                   ')
print('    - Used in conjunction with parser:                                                          ')
print('    /home/devasc/pyATS/genieparser/src/genie/libs/parser/iosxe/ShowCableSignalQualitytMer.py    ')
print('################################################################################################')
print("\n")
print("\n")
host = input('Host you want to poll signal-quality MER for the upstream: ')
print("\n")
interv_poll = input('Polling interval in seconds: ')
interv_poll = int(interv_poll)
print("\n")
nb_times = input('How many times you want to poll: ')
nb_times = int(nb_times)
print("\n")
intf = input('Interface cable x/y/z: ')
print("\n")
ups = input('Enter upstreams separated by space (ex. "U0 U1 U2 U3"): ')
ups_list = ups.split()
print("\n")

intf_list = []
for i in range(len(ups_list)):
    intf_list.append('Cable' + intf + '/' + ups_list[i])

header = ['Time']
header.append(intf_list)

f = open('show_cable_signal_quality.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

while nb_times > 0:
    
    nb_times -= 1

    dev = tb.devices[host]
    dev.connect()
    p1 = dev.parse('show cable signal-quality mer')
    data = [(datetime.now()).strftime('%H:%M'), p1['I/F'][intf_list[0]]['mer'], p1['I/F'][intf_list[1]]['mer'], p1['I/F'][intf_list[2]]['mer'], p1['I/F'][intf_list[3]]['mer']]
    writer.writerow(data)
    dev.disconnect()
    time.sleep(interv_poll)

f.close()
