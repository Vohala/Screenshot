import socket
import os
from datetime import datetime

HOST = '0.0.0.0'
PORT = 5005

def receive_exact(sock, length):
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            return None
        data += packet
    return data

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            try:
                hostname = receive_exact(conn, 64).decode().strip()
                print(f"Client hostname: {hostname}")
                
                os.makedirs(hostname, exist_ok=True)
                
                while True:
                    size_data = receive_exact(conn, 10)
                    if not size_data:
                        break
                    img_size = int(size_data.decode())
                    
                    img_data = receive_exact(conn, img_size)
                    if not img_data:
                        break
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{hostname}/screenshot_{timestamp}.png"
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                    print(f"Saved {filename}")
                    
            except ConnectionResetError:
                print(f"Client {addr} disconnected")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                conn.close()

if __name__ == "__main__":
    main()