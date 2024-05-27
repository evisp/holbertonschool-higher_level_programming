import socket
import json

def start_server():
    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("Server listening on port 12345...")

    # Accept incoming connections
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive and process data
        data = client_socket.recv(1024)
        if data:
            received_dict = json.loads(data.decode('utf-8'))
            print("Received Dictionary from Client:")
            print(received_dict)

        # Close the connection
        client_socket.close()

    # close server socket    
    server_socket.close()  

def send_data(data):
    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Serialize and send data
    serialized_data = json.dumps(data).encode('utf-8')
    client_socket.sendall(serialized_data)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_server()  # Start the server if executed directly
