import logging
from datetime import datetime
import subprocess
import sys


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)


try:
    from scapy.all import *

except ImportError:
    print("Install Scapy")
    sys.exit()    
    
print("Run the Tool with root previlages")

net_iface = input("Enter the interface on which to run the sniffer: ")

#Setting network interface in promiscuous mode
try:
    subprocess.call(["ifconfig", net_iface, "promisc"], stdout = None, stderr = None, shell = False)

except:
    print("Failed to set Promiscuous mode")

else:
    print("Interface %s is set to PROMISC mode" % net_iface)


#Taking input of the no of packets to be sniffed
no_of_packets = input("How many packets to be sniffed [0 for no limit]: ")

if int(no_of_packets) != 0:
    print("The program will capture %d packets." % int(no_of_packets))
    
elif int(no_of_packets) == 0:
    print("The program will keep on capturing until the timeout expires.")


#How long should the packets be sniffed
time_to_sniff = input("How long should the packet capturing happen [give no of seconds]: ")

if int(time_to_sniff) != 0:
    print("The program will capture packets for %d seconds." % int(time_to_sniff))
    

protocols_to_be_sniffed = input("Enter the protocol to filter by (arp|bootp|icmp|0 is all): ")

if (protocols_to_be_sniffed == "arp") or (protocols_to_be_sniffed == "bootp") or (protocols_to_be_sniffed == "icmp"):
    print("The program will capture only %s packets." % protocols_to_be_sniffed.upper())
    
elif (protocols_to_be_sniffed) == "0":
    print("The program will capture all protocols.")


file_name = input("Please give a name to the log file: ")

sniffer_log = open(file_name, "a")

def packet_log(packet):
    
   
    now = datetime.now()
    
    if protocols_to_be_sniffed == "0":
        print("Time: " + str(now) + " Protocol: ALL" + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)
        
    elif (protocols_to_be_sniffed == "arp") or (protocols_to_be_sniffed == "bootp") or (protocols_to_be_sniffed == "icmp"):
        print("Time: " + str(now) + " Protocol: " + protocols_to_be_sniffed.upper() + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)

print("Starting packet capture: ")

if protocols_to_be_sniffed == "0":
    sniff(iface = net_iface, count = int(no_of_packets), timeout = int(time_to_sniff), prn = packet_log)

elif (protocols_to_be_sniffed == "arp") or (protocols_to_be_sniffed == "bootp") or (protocols_to_be_sniffed == "icmp"):
    sniff(iface = net_iface, filter = protocols_to_be_sniffed, count = int(no_of_packets), timeout = int(time_to_sniff), prn = packet_log)
    
else:
    print("Could not identify the protocol.")
    sys.exit()

print(" Please check the %s file to see the captured packets." % file_name)
sniffer_log.close()


