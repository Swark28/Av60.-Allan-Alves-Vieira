import socket #Importando modulo socket.

HOST = '' #Host vazio aceitando qualquer Ip.
PORT = 5000 #Número da porta UDP para comunicação.

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Variavel udp recebendo socket, abrindo uma porta em protocolo IPV4 "socket.AF_INET" no protocolo UDP "socket.SOCK_DGRAM".

origem = (HOST, PORT) #Informações de número de porta, e endereço ip.
udp.bind(origem) #ligando "origem" na variavel "udp".

print("Seviço UDP incializado. Aguardando mensagem. \n") 

#print demonstrando funcionameno.

while True: 
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg)

#Loop while recebendo informações do protocolo udp, na porta 5000.
#Print mostrando respostas de "cliente" e a "mensagem".

udp.close()

#.close finalizando o loop.