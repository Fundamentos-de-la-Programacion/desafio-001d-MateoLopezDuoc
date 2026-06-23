import random

banco_preguntas = [
    {"pregunta": "Cual es la capital de Chile?", "respuesta": "Santiago"},
    {"pregunta": "Cuanto es 7 por 8?", "respuesta": "56"},
    {"pregunta": "Que palabra clave define una funcion en Python?", "respuesta": "def"},
    {"pregunta": "Cual es el simbolo del resto (modulo) en Python?", "respuesta": "%"},
    {"pregunta": "Que tipo de dato es 3.14?", "respuesta": "float"},
    {"pregunta": "Cuantos colores tiene el arcoiris?", "respuesta": "7"},
    {"pregunta": "Que funcion muestra texto en pantalla en Python?", "respuesta": "print"},
    {"pregunta": "Cual es el oceano que limita con Chile?", "respuesta": "Pacifico"}, 
    ]

def motrar_pregunta(pregunta):
    print (pregunta["pregunta"])
    
def normalizar(texto):
    return texto.strip().lower()

def es_correcta(respuesta_usuario, respuesta_correcta):
    return normalizar(respuesta_usuario:) == normalizar(respuesta_correcta)

def jugar_ronda(jugador, banco, n):
    preguntas = rando.sample(banco, n)
    
    puntaje = 0 
    
    for pregunta in pregunta:
        mostrar_pregunta(pregunta)
        
        respuesta = inpunt("respuesta:  ")
        if es_correcta(respuesta, pregunta["respuesta"]):
            puntaje += 1
        else:
            print("incorrecto")
            
return puntaje

def mostrar_ranking(jugadores):
    
    orden = sorted(
        jugador,
        kay=lombda jugador: jugador["puntaje"],
        reverse=True
        
    )
    
    posicion = 1
    for jugador in ordenados:
        
        porcentaje = (
            jugador["puntaje"] 
            jugador["preguntas"]
        ) * 100
        print 
        f""
        f""
        f""