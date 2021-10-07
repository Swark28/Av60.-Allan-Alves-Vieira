import socket #Importando modulo socket.

HOST = '' #Endereço ip vazio, recebendo qualquer ip.
PORT = 5000 #Porta tcp.

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Variavel tcp recebendo socket, abrindo uma porta ipv4 no protocolo tcp.

origem = (HOST, PORT)

#Tupla que armazena iformções do host e porta.

tcp.bind(origem) #ligação da tupla origem, com o tcp.
tcp.listen(1) #Numero de conexões aceitas.
print('Serviço iniciado. ') #Exibe funcionamento do servidor.

while(True):
    con, cliente = tcp.accept()
    print('Conectado por ', cliente)
    while(True):
        mensagem = con.recv(1024)
        print(cliente, mensagem)


#Loop while que estabelece conexão, e outro while que exibe mensagens da conexão.

con.close() #Finalização