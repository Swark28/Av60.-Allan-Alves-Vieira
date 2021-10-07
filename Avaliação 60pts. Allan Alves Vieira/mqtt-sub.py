import paho.mqtt.client as mqtt #Importando paho.mqtt.client por meio da simplificação "mqtt".
import json #Importando 

client = mqtt.Client(client_id='sub-py')

#Objeto "client" recebe classe client, que se comunicara com o broker mqtt.
 
client.connect('localhost', port=1883) #Endereço Ip que efetuara a conexão com o broker, e a sua porta.
client.subscribe('casa/sala/lampada/1') #Subscribe com topico

print("Subscriber connected!")#Exibe funcionamento.

def on_message_callback(client, userdata, message): #Função callback assíncrona que exibe estatus.
    
    msg = json.loads(message.payload.decode('utf-8'))
    if(msg["status"] == True):
        
        print("Pino X ligado")
    elif(msg["status"] == False):
        
        print("Pino X desligado")


client.on_message = on_message_callback #Executa callback ao receber mensagem.

client.loop_forever()#Loop infinito.
