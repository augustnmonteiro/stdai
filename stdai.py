import socket
import threading
import requests
import json

class Server:
    def __init__(self, host="localhost", port=9999, ollama_host="localhost", ollama_port=11434):
        self.host = host
        self.port = port
        self.ollama_host = ollama_host
        self.ollama_port = ollama_port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(10 * 1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f"Received: {message}")
                self.send_to_ollama(message)
        except ConnectionResetError:
            pass
        finally:
            client_socket.close()

    def send_to_ollama(self, message):
        url = f"http://{self.ollama_host}:{self.ollama_port}/api/chat"
        payload = {
            "model": "llama3",
            "messages": [
                {
                    "role": "system",
                    "content": "My code threw this error and I don't know what to do."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "stream": False
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            try:
                response_data = response.json()
                print("HELP ====================================")
                print(response_data['message']['content'])
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            except json.JSONDecodeError as json_err:
                print(f"STDAI ERROR - JSON decode error: {json_err}")
                print(f"STDAI ERROR - Raw response content: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"STDAI ERROR - Failed to send message to Ollama: {e}")

    def run(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"STDAI Running at {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = Server()
    server.run()
