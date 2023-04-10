import time
import Pyro4

class Server(object):

    @Pyro4.expose
    def welcomeMessage(self, name):
        return ('Olá, Bem vindo ao barbeiro! ' + str(name))
    
    @Pyro4.expose
    def cortaCabelo(self):
        print("Cortando cabelo...")
        for i in range(1,3+1):
            print(i)
            time.sleep(1)
        print("Corte de cabelo realizado.")
    
    @Pyro4.expose
    def cortaBarba(self):
        print("Cortando barba...")
        for i in range(1,4+1):
            print(i)
            time.sleep(1)
        print("Corte de barba realizado.")
    
    @Pyro4.expose
    def cortaBigode(self):
        print("Cortando bigode...")
        for i in range(1,5+1):
            print(i)
            time.sleep(1)
        print("Corte de bigode realizado.")
        

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register('server', uri)
    print(f'Ready. object uri = {uri}')
    daemon.requestLoop()

if __name__ == '__main__':
    startServer()