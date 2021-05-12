import xmlrpc.client as xmlrpclib

x = input('write message: ')
print(type(x))
# Create an object to represent our server.
server_url = 'http://localhost:8000/RPC2';
server = xmlrpclib.Server(server_url);

# Call the server and get our result.
result = server.sample.add(x)
print(result)