def calcula_grado(x):
    if 0.0<=x and x<=1.0:
        if x>0.9:
            a=str('A')
        elif x>0.8:
           a=str('B')
        elif x>0.7:
            a=str('C')
        elif x>0.6:
            a=str('D')
        else:
            a=str('F')
    else:
       a=str('score incorrecto')
    return a 
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
