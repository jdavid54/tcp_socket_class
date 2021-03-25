import socket
# test avec node-red tcp_test
# node_red renvoie 'hi, beauty' quand on lui envoie 'hello, world'

HOST = '192.168.1.61'
PORT = 6789

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print ('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

message = 'Hello, world'
print ('Envoi de :' + message)
n = client.send(bytes(message,'utf8'))
if (n != len(message)):
        print ('Erreur envoi.')
else:
        print ('Envoi ok.')

print ('Reception...')
donnees = client.recv(1024)
print ('Recu :', str(donnees,'utf8'))

print ('Deconnexion.')
client.close()