
import socket
def client(jogador, localizacao_cedula, linha_destino, coluna_destino, host = '127.0.0.1', port=5000): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port)
    sock.connect(server_address) 
    jogador = str(jogador)
    linha_originaria = str(localizacao_cedula[0])
    coluna_originaria = str(localizacao_cedula[1])
    linha_destino = str(linha_destino)
    coluna_destino = str(coluna_destino)
    try: 
        mensagem = jogador + '' + linha_originaria + '' +coluna_originaria + '' + linha_destino + '' + coluna_destino
        sock.sendall(mensagem.encode('utf-8'))
        print(mensagem)
        amount_received = 0 
        amount_expected = len(mensagem)
        #while amount_received < amount_expected: 
        #    data = sock.recv(16) 
         #   amount_received += len(data) 
         #   print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 