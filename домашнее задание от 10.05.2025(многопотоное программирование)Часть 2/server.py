# 1 задание

import socket
import threading

class TicTacToeServer:
    def __init__(self, host='localhost', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print("Сервер запущен, ожидаем подключения игроков...")
        
        self.clients = []
        self.board = [' ' for _ in range(9)]
        self.current_player = 0
        self.game_active = False

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client(self, client, player):
        while True:
            if not self.game_active:
                client.send("Ожидание второго игрока...\n".encode())
                continue
            
            try:
                move = client.recv(1024).decode()
                if move == "exit":
                    self.broadcast(f"Игрок {player + 1} вышел из игры. Вы проиграли!\n".encode())
                    self.game_active = False
                    break
                
                if self.board[int(move)] == ' ':
                    self.board[int(move)] = 'X' if player == 0 else 'O'
                    if self.check_winner():
                        self.broadcast(f"Игрок {player + 1} выиграл!\n".encode())
                        self.game_active = False
                    elif ' ' not in self.board:
                        self.broadcast("Ничья!\n".encode())
                        self.game_active = False
                    else:
                        self.current_player = 1 - player
                        self.broadcast(self.display_board().encode())
                else:
                    client.send("Эта клетка уже занята. Попробуйте снова.\n".encode())
            except Exception as e:
                print(f"Ошибка: {e}")
                break

        client.close()

    def display_board(self):
        return "\n".join([
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}",
            "---------",
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}",
            "---------",
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        ])

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False

    def start(self):
        while len(self.clients) < 2:
            client, addr = self.server.accept()
            print(f"Игрок подключен: {addr}")
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client, len(self.clients) - 1)).start()
        
        self.game_active = True
        self.broadcast("Игра началась!\n".encode())
        self.broadcast(self.display_board().encode())

if __name__ == "__main__":
    server = TicTacToeServer()
    server.start()







# 2 задание

import socket
import threading
import os

def handle_client(client_socket):
    # Получаем имя файла от клиента
    file_name = client_socket.recv(1024).decode('utf-8')
    print(f"Получено имя файла: {file_name}")

    # Запрашиваем подтверждение у клиента
    confirmation = input(f"Подтвердите получение файла '{file_name}' (y/n): ")
    client_socket.send(confirmation.encode('utf-8'))

    if confirmation.lower() == 'y':
        # Начинаем передачу файла
        with open(file_name, 'wb') as f:
            print("Начинаем получение файла...")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"Файл '{file_name}' успешно получен.")
        client_socket.send(b'Файл успешно передан.')
    else:
        print("Получение файла отменено.")
        client_socket.send(b'Получение файла отменено.')

    client_socket.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"Сервер запущен на порту {port}.")

    while True:
        client_socket, addr = server.accept()
        print(f"Подключен клиент: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server(5000)








# 3 задание

import socket
import threading

clients = []
usernames = {}

def handle_client(client_socket):
    # Получаем имя пользователя
    client_socket.send("Введите ваше имя пользователя: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    
    # Запрашиваем пароль (в данной реализации просто принимаем его)
    client_socket.send("Введите ваш пароль: ".encode('utf-8'))
    password = client_socket.recv(1024).decode('utf-8')
    
    # Здесь можно добавить проверку пароля и логина
    
    clients.append(client_socket)
    usernames[client_socket] = username
    broadcast(f"{username} вошел в чат!".encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, username + ": ")
            else:
                break
        except:
            break

    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]
    broadcast(f"{username} вышел из чата.".encode('utf-8'))

def broadcast(message, prefix=""):
    for client in clients:
        client.send(prefix.encode('utf-8') + message)

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"Сервер запущен на порту {port}.")

    while True:
        client_socket, addr = server.accept()
        print(f"Подключен клиент: {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server(5000)
