"""
References:
    https://realpython.com/python-sockets/#background
"""

# Import Python Socket API
import socket
import sys

"""
client application to establish a tcp connection with a server
"""
def tcpClient(portNum):

    # initiate server host and port variables. host is set to the
    # loopback interface only allowing processes on the localhost will
    # be able to connect to the server
    serverHost = '127.0.0.1'
    serverPort = int(portNum)

    # initiate end of message and end of transmission signals
    eomSignal = b"\r\n"
    eotSignal = b"/q"

    # 'with' allows us to use socket() without calling .close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:

        # client connects to server host and port
        clientSocket.connect((serverHost, serverPort))
        print(f"Connected to: localhost on port: {serverPort}")
        print("Enter message to send...")
        # print(">", end="")

        # maintain connection to the server until end of transmission signal
        # is sent
        while True:


            # take user input as bytes literal and append end of message signal
            # to the end before sending the entire message
            print(">", end="")
            message = input().encode() + eomSignal
            clientSocket.sendall(message)

            if message == eotSignal + eomSignal:
                break

            # initialize recvMsg as empty bytes literal each message iteration
            recvMsg = b""

            # loop until full message is received
            while True:

                # receive the tcp message
                recvMsg = recvMsg + clientSocket.recv(1024)

                # if end of message has been reached, print message
                if eomSignal in recvMsg:
                    # print only the message without crlf
                    print(recvMsg.decode().replace("\r\n", ''))
                    break

            if recvMsg == eotSignal + eomSignal:
                break





def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} port_number")
        return 0

    tcpClient(sys.argv[1])

if __name__ == "__main__":
    main()