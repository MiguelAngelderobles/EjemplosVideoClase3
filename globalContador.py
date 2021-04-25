import threading

operaciones=[]

class cuenta ():
    def __init__(self):
        self.lock = threading.Lock()
        self.contador = 0

    def funcion(self, contador_total=None, contador=None):
        self.lock.acquire()
        try:
            for i in range(1000000):
                self.contador += 1

        finally:
            self.lock.release()


contador=cuenta()
print("Inicio programa principal")
print("Valor Inicial: ",  contador.contador )
for i in range(3):
    operacion = threading.Thread(target=contador.funcion)
    operacion.start()
    operaciones.append(operacion)

for i in range(3):
    operaciones[i].join()

print("Cuenta:",contador.contador )
