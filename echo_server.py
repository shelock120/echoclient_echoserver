import socket
import threading
import select
import sys

def manual():
    print(sys.argv[0] + "\n syntax : "+ sys.argv[0] +"<port> [-b] \nsample : echoserver 1234 -b")
    sys.exit(0)

def main():
    if len(sys.argv) == 3 and sys.argv[2] == "-b":
        broad = True
    elif len(sys.argv) != 2:
        manual()
    
    bind_ip = '0.0.0.0'
    port = sys.argv[1]
    bind_port = int(port)
    
    broad = False
    
    
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(10) 
    input_list = [server]
    
    while True:
        input_ready, write_ready, except_ready = select.select(input_list, [], [])
     
        for ir in input_ready:
            if ir == server:
                client, address = server.accept()
                print(address, 'is connected')
                input_list.append(client)
     
            else:
                data = ir.recv(1024)
                if data:
                    print(ir.getpeername(), 'send :', data)
                    ir.send(data)
                elif broad:
                    for sock in input_list:
                        if sock == server:
                            continue
                        else:
                            sock.send(data)
                else:
                    print(ir.getpeername(), 'close')
                    ir.close()
                    input_list.remove(ir)

 
if __name__ == '__main__':
    main()