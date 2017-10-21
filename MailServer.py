from socket import *
import ssl
import base64

msg = "\r\n I love computer networks! Sean Kennedy Project 1 CS6043"
endmsg = "\r\n.\r\n"

recipient = "<recipient@email.com>\r\n"
sender = "<sender@gmail.com>"
username = "username"  # for gmail just repeat gmail email account
password = 'password'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
print("sending HELO command")
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Start a TLS connection
TLSCommand = 'STARTTLS\r\n'
clientSocket.send(TLSCommand.encode())
recvtls = clientSocket.recv(1024).decode()
print(recvtls)
if recvtls[:3] != '220':
    print('220 reply not received from server')

# SSL the socket
SSLclientSocket = ssl.SSLSocket(clientSocket)

# Send AUTH LOGIN command
print("Sending AUTH LOGIN command")
authCommand = 'AUTH LOGIN\r\n'
SSLclientSocket.write(authCommand.encode())
recvAUTH = SSLclientSocket.read(1024).decode()
print(recvAUTH)
if recvAUTH[:3] != '334':
    print('334 reply not received from server')


# Send the username specified above
USRname = base64.b64encode(username.encode()) + "\r\n".encode()
print("Sending Username")
SSLclientSocket.write(USRname)
recvUSRname = SSLclientSocket.read(1024).decode()
print(recvUSRname)
if recvUSRname[:3] != '334':
    print('334 reply not received from server')

# Send the password for the username specified above
PSword = base64.b64encode(password.encode()) + '\r\n'.encode()
print("Sending password")
SSLclientSocket.write(PSword)
recvPSword = SSLclientSocket.read(1024).decode()
print(recvPSword)
if recvPSword[:3] != '235':
    print('235 reply not received from server')

# Send MAIL FROM command and print server response.
# Fill in start
print("sending MAIL FROM command")
SSLclientSocket.send("MAIL FROM:".encode() + sender.encode() + "\r\n".encode())
recv1 = SSLclientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
print("sending RCPT TO command")
SSLclientSocket.send("RCPT TO:".encode() + recipient.encode())
recv1 = SSLclientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
SSLclientSocket.send("DATA\r\n".encode())
recv1 = SSLclientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
SSLclientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
SSLclientSocket.send(endmsg.encode())
recv1 = SSLclientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
QUIT = 'QUIT\r\n'.encode()
SSLclientSocket.send(QUIT)
recv1 = SSLclientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '221':
    print('221 reply not received from server.')
# Fill in end
