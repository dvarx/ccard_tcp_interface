import socket

# IP address of ccard is configured as 0xC0A80004 = 192.168.0.4;
# netmask of ccard is configured as 0xFFFFFF00;
# ccard listens on port 30

ip_ccard='192.168.0.4'
ip_rospc='192.168.0.1'
tcp_port_ccard=30
test_msg='AABBCCDD'
buffer_size=1024

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.connect((ip_ccard,tcp_port_ccard))
tcpsocket.send(test_msg)
datarcv=tcpsocket.recv(buffer_size)
tcpsocket.close()

print("received data: %s"%(str(datarcv)))