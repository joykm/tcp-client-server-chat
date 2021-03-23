** Instructions on how to run client server chat:
1. Run server.py using "python3 server.py port_number"
	a. It is recommended to use a port number above 5000.
2. Run client in a separate shell using "python 3 client.py port_number"
	a. port_number must match the port number server is running on.
3. Client will be prompted to send a message first. Server will be prompted to send the following message, and it will alternate.
4. To quit, in either the client or the server shell, type "/q". This will terminate both the client and server.