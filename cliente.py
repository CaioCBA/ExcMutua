import Pyro4

def main():
    name = input('Qual seu nome? ').strip()
    server = Pyro4.Proxy('PYRONAME:server')
    print(server.welcomeMessage(name))

    print('''Lista de serviços do barbeiro:\n
    1. Cortar Barba\n
    2. Cortar Cabelo\n
    3. Cortar bigode\n
    4. Nada
    ''')

    while True:
        command = input('Que serviço deseja no barbeiro?\n>>>').strip().upper()
        if command == 'CABELO':
            server.cortaCabelo()
            print("Cabelo cortado")

        if command == 'BARBA':
            server.cortaBarba()
            print("Barba cortada")

        if command == 'BIGODE':
            server.cortaBigode()
            print("Bigode cortado")

        if command == 'NADA':
            print('Venha novamente!')
            break


if __name__ == '__main__':
    main()