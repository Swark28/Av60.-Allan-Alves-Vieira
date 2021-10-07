import socket #Importação do modulo socket.

HOST = 'localhost' #Endereço ip do cliente
PORT = 5000 #Porta de conexão tcp.

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Variavel tcp recebendo modulo socket, abrindo porta IPV4, no modulo tcp "SOCK_STREAM"

destino = (HOST, PORT) #Tupla destino armazenando dados de host e porta.

tcp.connect(destino) #Conexão com o server.

while(True):
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8')
    tcp.send(mensagem) 


#Loop while que recebe mensagens e converte em bytes. 
#.send que envia mensagem para o tcp.

tcp.close() #Finalização.