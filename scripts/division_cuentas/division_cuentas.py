# Cantidad de personas
n_personas = int(input('Cantidad de personas: '))
print('')
nombres = []
i = 1
for persona in range(n_personas):
    persona = input('Nombre {}: '.format(i))
    i +=1
    nombres.append(persona)
print('')
    
long_nom = []
for i in nombres:
    long_nom.append(len(i))

aporte = []
for p in nombres:
    plata = float(input('Cantidad aportada por {}: '. format(p)))
    aporte.append(plata)
print('')

total = 0
for i in aporte:
    total += i
print('Total: {} $'.format(round(total,1)))
print('')

aporte_individual = total/n_personas
print('A pagar c/u: {} $ '.format(round(aporte_individual,1)))
print('')
    
# aporte final por persona
afpp = []
vfpp = []
for n in range(len(aporte)):
    final_pagar = aporte_individual-aporte[n]
    if final_pagar < 0:
        vfpp.append(abs(round(final_pagar,1)))
        afpp.append(float(0))
    else:
        afpp.append(round(final_pagar,1))
        vfpp.append(float(0))

amigos = list(zip(nombres,aporte,afpp,vfpp))
print((('+--'+('-'*max(long_nom))+'--')*4)+'+')

print('| '+'NOMBRE'+(' '*(max(long_nom)-(len('NOMBRE'))+3))+'|'+
        ' '+'APORTADO'+(' '*(max(long_nom)-(len('APORTADO'))+3))+'|'+
        ' '+'PAGAR'+(' '*(max(long_nom)-(len('PAGAR'))+3))+'|'+
        ' '+'VUELTO'+(' '*(max(long_nom)-(len('VUELTO'))+3))+'|')

print((('+--'+('-'*max(long_nom))+'--')*4)+'+')

for i in amigos:
    print('| '+(i[0])+(' '*(max(long_nom)-(len(i[0]))+3))+'|' +
        ' '+(str(i[1]))+(' '*(max(long_nom)-(len(str(i[1])))+3))+'|'+
        ' '+(str(i[2]))+(' '*(max(long_nom)-(len(str(i[2])))+3))+'|'+
        ' '+(str(i[3]))+(' '*(max(long_nom)-(len(str(i[3])))+3))+'|')

print((('+--'+('-'*max(long_nom))+'--')*4)+'+')