import random


def choice(list_words):
    return random.choice(list_words)


def spaces(word):
    return ['_']*len(word)


def show(list_words):
    print (' '.join(list_words))

   
def guess(word,list_words):
    global attemps
    letter = input('Ingrese una letra: ').lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                list_words[i] = letter
    else:
        attemps += 1
        print('Te quedan {} intentos'.format(6 - attemps))


def check_continuity(list_words):
    return "_" in list_words


# variable with number of player attempts
attemps = 0


def main():
    with open('bag_of_words.txt') as file:
        words = file.read()
    
    bag_of_words = words.split(',')
    
    word = choice(bag_of_words)
    
    lines = spaces(word)
    
    player = input('Ingrese su nombre: ')
    print (f'¡Bienvenido/a {player} al juego del ahorcado! Usted tendrá 10 intentos para adivinar la palabra correcta.\n¿Esta preparado/a? ¡A jugar!\nSu palabra es: ')
    show(lines)
    
    while check_continuity(lines):
        global attemps
        guess(word,lines)
        show(lines)
        
        if attemps < 6 and '_' not in lines:
            print(f'¡Felicidades {player} has ganado!')

        elif attemps == 6 and '_' in lines:
            print('Usted ya alcanzó la máxima cantidad de intentos.')
            last_chance = input('¿Desea arriesgar una palabra? Si o No => ')
            if last_chance.lower() == 'si':
                attemps = input('Ingrese palabra: ')
                if attemps == word:
                     print(f'¡Felicidades {player} has ganado!')
                     break
                else:
                  print('Lo siento, ha perdido.')
                  print(f'La palabra era: {word}')
                  break 
            else:
                print('Lo siento, ha perdido.')
                print(f'La palabra era: {word}')
                break 
                     
main()