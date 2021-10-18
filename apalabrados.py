import pandas as pd
import numpy as np



def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def add_numeros(ingreso, df):
    acumulado = df['número'].sum() + float(ingreso)
    nueva_fila = {'número': float(ingreso), 'acumulado': acumulado}
    df = df.append(nueva_fila, ignore_index = True)
    return df


def add_texto(ingreso, df):
    nueva_fila = {'texto': ingreso, 'inicial': ingreso[0], 'final': ingreso[len(ingreso)-1]}
    df = df.append(nueva_fila, ignore_index = True)
    return df


def add_caracter(ingreso, df):
    c = ['&', '/', '(', '!', '#',';',':','.',';', '_', '-',',','?','¿','¡']   
    n = 0

    for j in range(len(c)):
        for i in range(len(ingreso)):
            if c[j] == ingreso[i]:
                nueva_fila = {'caracter': c[j]}
                df = df.append(nueva_fila, ignore_index = True)
                n += 1
            
    return df, n



if __name__ == '__main__':

    numeros = pd.DataFrame()
    numeros['número'] = None
    numeros['acumulado'] = None

    texto = pd.DataFrame()
    texto['texto'] = None
    texto['inicial'] = None
    texto['final'] = None

    caracteres = pd.DataFrame()
    caracteres['caracter'] = None


    ingreso_usuario = int(input('''
                                [1] Nuevo ingreso
                                [2] Salir
                                '''
    ))

    while ingreso_usuario != 2:
        
        ingreso_usuario_2 = input()
        
        
        caracteres, n = add_caracter(ingreso_usuario_2, caracteres)
                    

        if n == 0:

            if ingreso_usuario_2.isalpha():
                
                texto = add_texto(ingreso_usuario_2, texto)
                print(texto)

            
            if is_number(ingreso_usuario_2):
                numeros = add_numeros(ingreso_usuario_2, numeros)
                print(numeros)    
        

        ingreso_usuario = int(input('''
                                [1] Nuevo ingreso
                                [2] Salir y ver bases de datos
                                '''
                              ))
    
    if ingreso_usuario == 2:
        print(caracteres)
        print(numeros)
        print(texto)