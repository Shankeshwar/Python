# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# update the configuration
#port = 443
#is_https_enabled = False

#print the updated configuration
print(f"updated Port: {port}")
print(f"updated HTTPS Enabled: {is_https_enabled}")
