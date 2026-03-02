import socket
import threading
import time

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8080))
    server.listen(1)
    
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Socket Server"
    conn.sendall(response.encode())
    conn.close()
    server.close()

def run_client():
    time.sleep(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    
    request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n"
    client.sendall(request.encode())
    
    response = client.recv(4096).decode()
    print(response)
    client.close()

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    run_client()
