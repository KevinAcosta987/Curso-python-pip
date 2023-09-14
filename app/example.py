#all llamar a la funcion main.py no solo recivo lo que pido del main sino que se ejecuta dicho main:

import main
print('esto es lo que pedi del main =>',main.data)

#como evitar que pase esto
#coloco lo que esta en el main en una funcion def run(): 
main.run()
#para que no de error esto el data tiene que estar fuera del run
print(main.data)

#el problema de esto es que ya no corre el main de forma correcta
#para resolverlo
# if __name__ == '__main__': run()

