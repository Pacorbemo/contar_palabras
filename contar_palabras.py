cuenta = {}
for i in range (97,123):
    j = chr(i)
    cuenta.update({j : 0})
    if i == 110:
        cuenta.update({"ñ":0})
cuenta.update({' ' : 0})

def contar_palabras(texto):
    for char in texto.lower():
        if char not in cuenta:
            continue
        j = cuenta.get(char) + 1 
        cuenta.update({char : j})
    
    cuenta_num=[]
    for i in range(10):
        cuenta_num.append([i,0])
    for numero in texto:
        try:
            cuenta_num[int(numero)][1] += 1
        except:
            continue

    salto = 0
    for char in cuenta:
        if char == ' ':
            break
        print('Hay', cuenta.get(char), char.upper(), end="    ")
        salto +=1
        if salto == 10:
            print() ; salto=0

    if cuenta.get(' ') != 1:
        print('Hay', cuenta.get(' ') ,'espacios', end='\n\n')
    else:
        print('Hay 1 espacio', end='\n\n')

    for i in range(10):
        print('Hay', cuenta_num[i][1], cuenta_num[i][0], end="    ")

contar_palabras('')