import time 
from threading import Thread


def fall(velocidade, objeto):
    queda = 0
    while queda <= 100:
        queda += velocidade 
        time.sleep(2)
        print('Objeto: {} km {}' .format(objeto, queda))

t_objeto = Thread(target=fall, args=[1, "Caindo"])

t_objeto.start()
