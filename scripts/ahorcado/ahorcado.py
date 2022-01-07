import random

#luego las funciones a utilizar
def eleccion(lista):
    return random.choice(lista)

def espacios(palabra):
    return ['_']*len(palabra)

def mostrar(lista):
    print (' '.join(lista))
   
def adivinar(palabra,lista):
    global intentos
    letra = input('Ingrese una letra: ').lower()
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                lista[i] = letra
    else:
        intentos += 1
        print('Te quedan {} intentos'.format(6 - intentos))


def verificar_continuidad(lista):
    return "_" in lista

#Esta va a ser la variable con cantidad de intentos del jugador/a
intentos = 0

#creamos otra funcion que incluya todo el programa
def main():
    with open('palabras_ahorcado.txt') as archivo:
        palabras = archivo.read()
    
    lista_palabras = palabras.split(',')
    
    palabra = eleccion(lista_palabras)
    
    lista_ = espacios(palabra)
    
    jugador = input('Ingrese su nombre: ')
    print ('¡Bienvenido/a {} al juego del ahorcado! Usted tendrá 10 intentos para adivinar la palabra correcta.\n¿Esta preparado/a? ¡A jugar!\nSu palabra es: '.format(jugador))
    mostrar(lista_)
    
    while verificar_continuidad(lista_):
        global intentos
        adivinar(palabra,lista_)
        mostrar(lista_)
        

        if intentos < 6 and '_' not in lista_:
            print('¡Felicidades {} has ganado!'.format(jugador))

        elif intentos == 6 and '_' in lista_:
            print('Usted ya alcanzó la máxima cantidad de intentos.')
            ultimo_intento = input('¿Desea arriesgar una palabra? Si o No')
            if ultimo_intento.lower() == 'si':
                arriesgar = input('Ingrese palabra: ')
                if arriesgar == palabra:
                     print('¡Felicidades {} has ganado!'.format(jugador))
                     break
                else:
                  print('Lo siento, ha perdido.')
                  print(f'La palabra era: {palabra}')
                  break 
            else:
                print('Lo siento, ha perdido.')
                print(f'La palabra era: {palabra}')
                break 
                
    

              
main()


