#!/usr/bin/env python3

import socket
from time import sleep

HOST = '192.168.1.69'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
relay1_on = b'\xA0\x01\x01\xA2'   
relay1_off = b'\xA0\x01\x00\xA1'
relay2_on = b'\xA0\x02\x01\xA3'
relay2_off = b'\xA0\x02\x00\xA2'
relay3_on = b'\xA0\x03\x01\xA4'
relay3_off = b'\xA0\x03\x00\xA3'
relay4_on = b'\xA0\x04\x01\xA5'
relay4_off = b'\xA0\x04\x00\xA4'

dict_relay = {'r1_on':relay1_on,'r1_off':relay1_off,'r2_on':relay2_on,'r2_off':relay2_off,
              'r3_on':relay3_on,'r3_off':relay3_off,'r4_on':relay4_on,'r4_off':relay4_off}

def light_on_all(simultaneous=False):
    delay = 0.1
    print('all lights on')
    client.send(relay1_on)
    if not simultaneous : sleep(delay)
    client.send(relay2_on)
    if not simultaneous : sleep(delay)
    client.send(relay3_on)
    if not simultaneous : sleep(delay)
    client.send(relay4_on)
    if not simultaneous : sleep(delay)


def light_off_all(simultaneous=False):
    print('all lights off')
    delay = 0.1
    client.send(relay4_off)
    if not simultaneous : sleep(delay)
    client.send(relay3_off)
    if not simultaneous : sleep(delay)
    client.send(relay2_off)
    if not simultaneous : sleep(delay)
    client.send(relay1_off)
    if not simultaneous : sleep(delay)

def cmd_relay(relay_number, on=True):
    if on: cmd='on'
    else: cmd='off'
    target = 'r'+str(relay_number)+'_'+cmd
    client.send(dict_relay[target])
  
def connect_client():
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print ('Connexion vers ' + HOST + ':' + str(PORT) + ' réussie.')
    return client
# start
client = connect_client()
loop = 5

while loop:
    print(loop)
    light_off_all()
    light_off_all()
    sleep(1)
    print('flash all relays every 2s')
    client.send(relay1_on)
    sleep(1)
    client.send(relay1_off)
    sleep(1)
    client.send(relay2_on)
    sleep(1)
    client.send(relay2_off)
    sleep(1)
    client.send(relay3_on)
    sleep(1)
    client.send(relay3_off)
    sleep(1)
    client.send(relay4_on)
    sleep(1)
    client.send(relay4_off)
    sleep(1)
    #loop = False
    '''
    cmd_relay(2)   # relay 2 on, on is default for second argument
    sleep(1)
    cmd_relay(2, 0)  # relay 2 off
    sleep(2)
    '''   
    light_on_all()
    light_on_all()
    sleep(2)
    loop -= 1
    
light_off_all()
light_off_all()
print('close_socket')
client.close()
