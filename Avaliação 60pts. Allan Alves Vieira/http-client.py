from http.client import HTTPConnection #Importando modulo http e classe httpconnection.

conexao = HTTPConnection('localhost:5000') #Variavel recebendo classe e criando conexão ip na porta 5000.
conexao.request("GET", "/") #Solicitando na raiz.
resposta = conexao.getresponse() #Objeto recebendo dados.
pagina = resposta.read() #Recebendo respostas do objeto.

print(pagina) #Exibindo resultado.