#!/usr/bin/env python
import sys
import warnings
from clasificado.crew import Clasificado

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def procesar_topicos(topicos):
    """
    Procesa una lista de tópicos y devuelve los resultados.
    """
    clasificado = Clasificado()
    return clasificado.procesar_topicos(topicos)

def run():
    """
    Run the crew with user input.
    """
    input_data = input("Ingrese su consulta de la opción run: ")
    topicos_ejemplo = [input_data]

    print("\nProcesando los tópicos...")
    resultados = procesar_topicos(topicos_ejemplo)
    
    print("\nResultados del procesamiento:")
    for resultado in resultados:
        print(resultado)

def train():
    """
    Train the crew with user-specified parameters.
    """
    try:
        inputs = {
            "topico": input("Ingrese el tema para entrenamiento: ")
        }
        clasificado = Clasificado()
        clasificado.train(inputs=inputs)
    except Exception as e:
        print(f"Error durante el entrenamiento: {e}")

def replay():
    """
    Replay the crew execution for a specific task ID.
    """
    try:
        task_id = input("Ingrese el ID de la tarea para reproducir: ")
        clasificado = Clasificado()
        clasificado.replay(task_id=task_id)
    except Exception as e:
        print(f"Error durante la reproducción: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "topic": input("Ingrese el tema para pruebas: ")
    }
    try:
        Clasificado().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

