import socket
import common_ports

def get_open_ports(target, port_range, words = None):
    open_ports = []
    for port in range(port_range[0], port_range[1]+1):
      #print(port)
      try:
      #print(sock)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if(result == 0):
          open_ports.append(port)
        sock.close()
      except Exception:
        ip = target.split(".")
        if(ip[0].isdigit()):
          return 'Error: Invalid IP address'
        else:
          return 'Error: Invalid hostname'
    if(words):
      ip = target.split(".")
      if(ip[0].isdigit()):
        try:
          url = socket.gethostbyaddr(target)
          #print(url)
          string = "Open ports for "+ url[0] +" (" +target+")\nPORT     SERVICE\n"
        except Exception:
          string = "Open ports for "+target+"\nPORT     SERVICE\n"
        
      else:
        string = "Open ports for "+target+ " (" + socket.gethostbyname(target)+")\nPORT     SERVICE\n"
      for i in open_ports:
        if(i in common_ports.ports_and_services.keys()):
          string = string + str(i) + " "*(9 -len(str(i))) + common_ports.ports_and_services[i] + "\n"
      return(string[:-1])
    return(open_ports)