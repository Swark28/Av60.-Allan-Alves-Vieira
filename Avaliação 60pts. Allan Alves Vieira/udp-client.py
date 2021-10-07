import socket #importando modulo socket

HOST = 'localhost' #Endereço ip do cliente.
PORT = 5000 #Número da porta udp para comunicação.

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Variavel udp recebendo socket, abrindo uma porta em protocolo IPV4 "socket.AF_INET" no protocolo UDP "socket.SOCK_DGRAM".

destino = (HOST, PORT) 

#Tupla armazenando endereço ip e porta udp.

while(True):
    mensagem = bytes(input('Digite sua mensagem: '),encoding='utf-8')
    udp.sendto(mensagem, destino)

#Loop While para enviar "Mensagem" e informações do cliente para o server.

udp.close #finalização do loop.