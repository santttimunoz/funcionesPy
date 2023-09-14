#funciones sin parametros que no retorna nada

def Saludar():
    print("mira esta nueva weo weon, funciones weon ")

def SaludarName(name):
    print(f"Hola {name}")

def programa(name, nota):
    print(f'Hola {name} tu nota es: {nota}')


#en este caso, cuando se llame la funcion el parametro por defecto se activa
#si no se agreaga un parametro

def valoresPorDefecto(name, nota, programa = "nuevas tecnologias"):    
    print(f"Hola {name}, tu nota de {programa} es: {nota}")

#si el retorno esta entre parentesis devuelve una tupla
#si el retorno esta entre llaves devuelve un diccionario
#si el retorno esta entre corchetes devuelve una lista
def Opereaciones(n1, n2):
    return (n1 + n2, n1 * n2)

#llamar funciones(buenas practicas, hacer las funciones arriba del codigo)

if __name__ == "__main__":
    
    name = "santi"
    SaludarName(name)
    Saludar()
    #los parametro se pueden definir cuando se llama a la funcion
    programa(nota = 4.7, name = "santi")
    #aqui aparece el parametro por defecto
    valoresPorDefecto("santi", 4.6)
    #aqui se le da un parametro
    valoresPorDefecto("santi", 4.5, "programacion avanzada")

    #funcion con retorno de multiples valores
    n1 = 34
    n2 = 3
    resultado = Opereaciones(n1, n2)
    print(f"{n1} + {n2} = {resultado[0]}")
    print(f"{n1} * {n2} = {resultado[1]}")
    

