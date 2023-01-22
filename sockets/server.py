from shelper import SocketHelper

sockethelper = SocketHelper("localhost",1333)

while True:

 sockethelper.s_appept()
 
 print(sockethelper.read_data(),sockethelper.send_data("nice to meet you"),sockethelper.close_socket)