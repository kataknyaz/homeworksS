# 1 задание

import socket

class TicTacToeClient:
    def __init__(self, host='localhost', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def start(self):
        while True:
            message = self.client.recv(1024).decode()
            print(message)
            if "Игрок" in message or "Ничья" in message:
                break



            if "Ожидание" not in message:
                move = input("Ваш ход (0-8) или 'exit' для выхода: ")
                if move in ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'exit']:
                    self.client.send(move.encode())
                else:
                    print("Неверный ввод. Попробуйте снова.")
        
        self.client.close()

if __name__ == "__main__":
    client = TicTacToeClient()
    client.start()







# 2 задание
import socket
import os

def send_file(file_name, server_ip, port):
    if not os.path.isfile(file_name):
        print("Файл не найден.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))

    # Отправляем имя файла
    client.send(file_name.encode('utf-8'))

    # Ждем подтверждения от сервера
    confirmation = client.recv(1024).decode('utf-8')
    if confirmation.lower() == 'y':
        print("Подтверждение получено. Начинаем отправку файла...")
        with open(file_name, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client.send(data)
        print("Файл успешно отправлен.")
        
        # Получаем сообщение об успешной передаче
        message = client.recv(1024).decode('utf-8')
        print(message)
    else:
        print("Передача файла отменена.")

    client.close()

if __name__ == "__main__":
    server_ip = input("Введите IP-адрес сервера: ")
    port = 5000
    file_name = input("Введите имя файла для отправки: ")
    send_file(file_name, server_ip, port)









# 3 задание

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("Ошибка при получении сообщения.")
            break

def send_messages(client_socket):
    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    server_ip = input("Введите IP-адрес сервера: ")
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    # Запускаем потоки для получения и отправки сообщений
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    threading.Thread(target=send_messages, args=(client_socket,), daemon=True).start()

    # Ожидаем завершения работы
    while True:
        pass
