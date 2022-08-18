import socket

host = "web.whatsapp.com"
print ("we will get ip adrress and host name of whatsapp in this script ")
host_ip = socket.gethostbyname(host)
print("Hostname is =  ",host)
print("IP  =  ",host_ip)
