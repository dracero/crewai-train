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
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": input("Ingrese el tema para entrenamiento: ")
    }
    try:
        Clasificado().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Clasificado().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

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

