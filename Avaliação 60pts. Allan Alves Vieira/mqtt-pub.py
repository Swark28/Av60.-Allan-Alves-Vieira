import paho.mqtt.client as mqtt #Importando paho.mqtt.client por meio da simplificação "mqtt".
import json #Importando 
BROKER = "localhost"  #Endereço Ip da conexão.
PORT = 1883 #Porta da conexão.

client = mqtt.Client('pub-py') #Objeto "client" recebe classe client, que se comunicara com o broker mqtt.

client.connect(BROKER, PORT) #Conexão do broker e a porta.

def on_publish_callback(client, userdata, result): #Callback que exibe resultado da ação.
    print("Dado publicado")

client.on_publish = on_publish_callback #Executa callback ao receber mensagem.

status = "false"  #Valor setado como falso.

while(True):
    value = input('Digite 1 para ligado ou 0 para desligado: ')
    if(value == "0"):
        status = "false"
    elif(value == "1"):
        status = "true"
#Loop While que realiza o controle
    client.publish('casa/sala/lampada/1','{ "status": %s }' % status)
    print('{ "status": %s }' % status)
    #Publish com topico e mensagem, recebendo status e transformando em str Json
    #Publicando resultado, e aguardando novo controle.