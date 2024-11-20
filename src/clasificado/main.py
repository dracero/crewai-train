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
    Train the crew for exactly 6 iterations.
    """
    import sys  # Import sys in case it's needed for other functionality
    try:
        # Solicitar al usuario la consulta
        input_data = input("Ingrese su consulta de la opción TRAIN: ")
        inputs = {
            "topico": input_data 
        }
        
        # Configurar el entrenamiento con 6 iteraciones
        Clasificado().crew().train(n_iterations=6, filename=sys.argv[2], inputs=inputs)

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
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Clasificado().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

