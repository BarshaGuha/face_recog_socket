import socket
import logging
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9010))    
    s.listen(1)
    print("binded")
    while True:
        conn, addr = s.accept() 
        data = conn.recv(1024)
        if data:
            logging.debug('Data received over socket')
            print(data)
except socket.error as err: 
    print("socket creation failed with error %s" %(err)) 
  
