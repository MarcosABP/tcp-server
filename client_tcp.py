from socket import *
import time
import tkinter as tk
from tkinter import simpledialog
import re

print("Client TCP ON")
data = []
date_format = "%d/%m"


def valid_date(date):
    pattern_str = r"^\d{2}/\d{2}"

    if re.match(pattern_str, date) or date == "n":
        return True
    else:
        return False


def ask_input():
    # Cria a janela principal
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre o pop-up para solicitar a entrada do usuário
    user_input = 0
    while user_input != "n":
        user_input = simpledialog.askstring(
            "Input",
            "Por favor, insira uma data no modelo dd/mm:\nCaso queira encerrar, digite 'n'",
        )

        if valid_date(user_input):
            if user_input != "n":
                split = user_input.split("/")
                dia = split[0]
                mes = split[1]

            if (
                user_input is not None
                and user_input != "n"
                and int(dia) >= 1
                and int(dia) <= 31
                and int(mes) >= 1
                and int(mes) <= 12
            ):
                data.append(user_input)
                print(f"Você inseriu: {user_input}")

            elif user_input == "n":
                print("Terminou de inserir")

            elif int(dia) <= 1 or int(dia) >= 31 or int(mes) <= 1 or int(mes) >= 12:
                print("Data inválida")

            else:
                print("Nenhuma entrada fornecida")
        else:
            print("Entrada inválida. Correto: dd/mm")
    # Fecha a janela principal
    root.destroy()


if __name__ == "__main__":
    ask_input()


# Configurações do cliente
server_address = "192.168.40.162"
server_port = 8089

# Lista de datas para envio


# Configura e conecta o cliente ao servidor
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((server_address, server_port))

for i in range(len(data)):
    msg = data[i]
    temp_incial = time.perf_counter()
    clientsocket.send(msg.encode())

    temp_final = time.perf_counter()
    print(f"O tempo da requisição {i+1} foi: {temp_final-temp_incial} segundos")

    resp = clientsocket.recv(1024)
    print(
        "PARABÉNS, você é um",
        resp.decode().split(" ", 1)[1],
        "por ter nascido em",
        resp.decode().split(" ", 1)[0],
    )


clientsocket.close()
