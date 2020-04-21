#! python3

import logging
import pyinputplus  as pyip

logging.basicConfig(level =logging.DEBUG, format ="%(asctime)s - %(levelname)s -%(message)s")
logging.debug("Comeco do programa")


def fatorial(n):
    logging.debug("Comeco do fatorial (%s)" % (n))

    total = 1

    for i in range(1, n+1):
        total = total * i
        logging.debug("i is "+ str(i) + " and Total is " + str(total))
    logging.debug("fim do fatorial (%s)" % (n))

    return total

print("digite um nuemero para calcular o fatorial:")
numero = pyip.inputInt()
print(fatorial(numero))
logging.debug("Fim do programa")
