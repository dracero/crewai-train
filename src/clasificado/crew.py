from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from clasificado.tools.custom_tool import ProcesarAdministrativoTool, ProcesarTecnicoTool
import json

@CrewBase
class Clasificado:
    """Clasificado crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def clasificador_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['clasificador_agent'],
            verbose=True
        )

    @agent
    def administrativo_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['administrativo_agent'],
            verbose=True,
            tools=[ProcesarAdministrativoTool]
        )

    @agent
    def tecnico_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tecnico_agent'],
            verbose=True,
            tools=[ProcesarTecnicoTool]
        )

    @task
    def clasificacion_task(self) -> Task:
        return Task(
            config=self.tasks_config['clasificacion_task'],
        )

    @task
    def administrativo_task(self) -> Task:
        return Task(
            config=self.tasks_config['administrativo_task'],
        )

    @task
    def tecnico_task(self) -> Task:
        return Task(
            config=self.tasks_config['tecnico_task'],
        )

    def procesar_topicos(self, topicos: list[str]):
        """Clasifica y procesa una lista de tópicos."""
        resultados = []

        for topico in topicos:
            # Clasificación del tópico
            clasificacion_task = Task(
                description=f"""Clasifica el siguiente tópico: '{topico}'
                Responde EXACTAMENTE con una palabra:
                'administrativo' o 'no administrativo'.""",
                agent=self.clasificador_agent(),
                expected_output="Clasificación del tópico como 'administrativo' o 'no administrativo'"
            )

            clasificacion_crew = Crew(
                agents=[self.clasificador_agent()],
                tasks=[clasificacion_task],
                process=Process.sequential
            )

            clasificacion_result = clasificacion_crew.kickoff()
            clasificacion = clasificacion_result.get("result", "").lower().strip() if isinstance(clasificacion_result, dict) else str(clasificacion_result).lower().strip()

            # Procesamiento según clasificación
            if clasificacion == "administrativo":
                admin_task = Task(
                    description=f"Procesa el tópico administrativo: {topico}",
                    agent=self.administrativo_agent(),
                    expected_output="Confirmación del procesamiento administrativo con la salida del tópico"
                )
                admin_crew = Crew(
                    agents=[self.administrativo_agent()],
                    tasks=[admin_task],
                    process=Process.sequential
                )
                admin_result = admin_crew.kickoff()
                resultados.append(admin_result)

            elif clasificacion == "no administrativo":
                tech_task = Task(
                    description=f"Procesa el tópico no administrativo: {topico}",
                    agent=self.tecnico_agent(),
                    expected_output="Confirmación del procesamiento no administrativo con la salida del tópico"
                )
                tech_crew = Crew(
                    agents=[self.tecnico_agent()],
                    tasks=[tech_task],
                    process=Process.sequential
                )
                tech_result = tech_crew.kickoff()
                resultados.append(tech_result)

            else:
                resultados.append(f"Error en la clasificación del tópico: {topico}")

        return resultados
    
    def train(self,inputs: dict):
        print("Tareas disponibles:", self.tasks_config.keys())  # Depuración

        resultados_entrenamiento = []
        print(f"Iniciando iteración")
        result = self.crew().kickoff(inputs=inputs)
        resultados_entrenamiento.append(result)


    def replay(self, task_id: str):
        """
        Reproduce la ejecución de una tarea específica por su ID.
        """
        # Asegurarse de tener un mecanismo para guardar y recuperar ejecuciones
        log_file = "execution_log.json"
        if not os.path.exists(log_file):
            print("No se encontró un archivo de registro de ejecuciones.")
            return

        with open(log_file, 'r') as file:
            execution_logs = json.load(file)

        task_execution = next((log for log in execution_logs if log.get("task_id") == task_id), None)
        if not task_execution:
            print(f"No se encontró una tarea con ID {task_id}.")
            return

        # Reproducir la tarea (esto es conceptual y depende de cómo se manejan los logs)
        print(f"Reproduciendo tarea con ID {task_id}: {task_execution}")
        return task_execution

    def test(self, n_iterations: int, openai_model_name: str, inputs: dict):
        """
        Prueba la ejecución del crew con los parámetros dados.
        """
        print(f"Probando el crew con {n_iterations} iteraciones y modelo {openai_model_name}...")
        for i in range(n_iterations):
            print(f"Iniciando prueba {i + 1}...")
            result = self.crew().kickoff(inputs=inputs)
            print(f"Resultado de la prueba {i + 1}: {result}")
    
    @crew
    def crew(self) -> Crew:
        """Creates the Clasificado crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
