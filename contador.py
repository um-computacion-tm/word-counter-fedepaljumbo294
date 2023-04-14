import unittest

def contadorDePalabras(frase : str):
    result = {}
    lista = frase.split()
    for i in lista:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

if __name__ == '__main__':
    unittest.main()
