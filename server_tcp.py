from socket import *

# Configurações do servidor
server_ip = gethostbyname(gethostname())
print(server_ip)
server_address = "192.168.40.162"
server_port = 8089

# Dicionários para resposta com base em dia e mês
dic_dia = {
    "01": "Cavalo",
    "02": "Elefante",
    "03": "Rinoceronte",
    "04": "Girafa",
    "05": "Hipopótamo",
    "06": "Cachorro",
    "07": "Gato",
    "08": "Macaco(a)",
    "09": "Zebra",
    "10": "Falcão",
    "11": "Tubarão",
    "12": "Golfinho",
    "13": "Pato",
    "14": "Canário",
    "15": "Gavião",
    "16": "Timbu",
    "17": "Harpia",
    "18": "Ratel",
    "19": "Abelha",
    "20": "Rato",
    "21": "Cobra",
    "22": "Dragão",
    "23": "Rena",
    "24": "Alce",
    "25": "Panda",
    "26": "Urso",
    "27": "Lobo",
    "28": "Garça",
    "29": "Tartaruga",
    "30": "Coelho",
    "31": "Gafanhoto",
}

dic_mes = {
    "01": "Inteligente",
    "02": "Sagaz",
    "03": "Cabeçudo",
    "04": "Falaz",
    "05": "Sábio",
    "06": "Calmo",
    "07": "Paciente",
    "08": "Forte",
    "09": "Relaxado",
    "10": "Atroz",
    "11": "Preguiçoso",
    "12": "Faminto",
}

# Configura e inicia o servidor
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((server_address, server_port))
serversocket.listen(5)
print("SERVER TCP ON!")

while True:
    sck_client, address = serversocket.accept()
    print(f"Connection from {address}")

    while True:
        msg = sck_client.recv(1024)
        if not msg:
            break
        msg = msg.decode().split("/")
        try:
            resp = msg[0] + "/" + msg[1] + " " + dic_dia[msg[0]] + " " + dic_mes[msg[1]]
            sck_client.send(resp.encode())
        except KeyError:
            sck_client.send("Invalid date".encode())
            break

    sck_client.close()
    print(f"Connection closed from {address}")
