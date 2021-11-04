import socket

# IP address of ccard is configured as 0xC0A80004 = 192.168.0.4;
# netmask of ccard is configured as 0xFFFFFF00;
# ccard listens on port 30

ip_ccard='192.168.0.4'
ip_rospc='192.168.0.1'
tcp_port_ccard=30
test_data=b'AABBCCDD'
buffer_size=1024

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcpsocket.connect((ip_ccard,tcp_port_ccard))
except TimeoutError:
    print("unable to connect to socket, is connection valid?")
    quit()

while(True):
    send_data=input("type data to send: ")
    print("Sending data: %s\n"%(send_data))
    try:
        tcpsocket.send(send_data.encode())
    except Exception as ex:
        print("Error sending data via TCP: %s"%(str(ex)))
        tcpsocket.close()
        quit()
    try:
        datarcv=tcpsocket.recv(buffer_size)
    except TimeoutError:
        print("timeouterror: did not receive any data back fromcard")
        tcpsocket.close()
        quit()
    print("Received data: %s\n"%(str(datarcv)))