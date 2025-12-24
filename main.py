import socket
import threading

HOST = "..."
PORT = 10000





def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"server listen in : {HOST}: {PORT}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"client online  {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
