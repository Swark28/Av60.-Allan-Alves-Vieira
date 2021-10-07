from http.server import BaseHTTPRequestHandler, HTTPServer

#Importando modulos da biblioteca http.

HOST = 'localhost' #Endereço ip da conexão
PORT = 5000 #Porta da conexão

class MyHandler(BaseHTTPRequestHandler): #Classe manipulador herdando classe http
    def do_GET(self): #Método ouvindo servidor. 
        self.send_response(200) #Resposta estando ok
        self.send_header("Content-type", "text/html") #Cabeçario tipo texto. 
        self.end_headers() #Finalização do cabeçario.
        self.wfile.write(bytes("<html><head><title>S</title>AULA HTTP</head>","utf-8")) #Mensagem cabeçario.
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Servidor HTTP de exemplo.</p>", "utf-8"))#Texto a ser exibido.
        self.wfile.write(bytes("</body></html>", "utf-8"))

webServer = HTTPServer((HOST,PORT), MyHandler) #Variavel recebe http, tupla e classe.
print("Servidor iniciado em http://%s:%s" % (HOST, PORT)) #Print exibindo link da pagina.

webServer.serve_forever()#Inicia server ao receber informações.