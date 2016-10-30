# Send 200 ok to any udp request on 5060

from socket import *

# Set the socket parameters
host = "localhost"
port = 5060
buf = 1024
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while 1:
    data,addr = UDPSock.recvfrom(buf)
    if not data:
        print " SIP/2.0 200 OK Via: SIP/2.0/UDP there.com:5060 From: scanner <sip:suck@me.com> To: scanned <sip:eat@me.com> Call-ID: 6969@yourmomms.com CSeq: 2 SUCKIT"
        break
    else:
        print "\nReceived message '", data,"' from ", addr

# Close socket
UDPSock.close()

