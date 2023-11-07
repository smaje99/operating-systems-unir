"""Algoritmos de Planificación FCFS"""

from dataclasses import dataclass


@dataclass()
class Process:
    """Clase que representa un proceso en un algoritmo de planificación.

    Attributes:
        name (str): El nombre único del proceso.
        execution_time (int): El tiempo necesario para que
            el proceso se ejecute.
        waiting_time (int, opcional): El tiempo de espera
            del proceso (calculado).
        turnaround_time (int, opcional): El tiempo de retorno
            del proceso (calculado).
    """

    name: str
    execution_time: int
    waiting_time: int = 0
    turnaround_time: int = 0

    def __str__(self):
        return (
            f"Proceso {self.name}: "
            + f"Ejecución={self.execution_time}, "
            + f"Tiempo de Espera={self.waiting_time}, "
            + f"Tiempo de Retorno={self.turnaround_time}"
        )


class FCFSAlgorithm:
    """Clase que implementa el algoritmo FCFS (First-Come, First-Served)
    de planificación de procesos.

    El algoritmo FCFS asigna la CPU al primer proceso en llegar y
    continúa ejecutando los procesos en el orden de llegada.

    Attributes:
        processes (list): Una lista de objetos de clase Process
                que representan los procesos a planificar.
    """

    def __init__(self, processes: list[Process]):
        self.processes = processes

    def __call__(self):
        """Ejecuta la simulación del algoritmo FCFS y calcula los
        tiempos de espera y de retorno para cada proceso.

        Este método simula la ejecución de los procesos de
        acuerdo con el algoritmo FCFS (Primero en llegar,
        primero en servir). Calcula los tiempos de espera y
        de retorno para cada proceso y los almacena en los
        objetos de proceso correspondientes.
        """
        current_time = 0
        for process in self.processes:
            process.waiting_time = current_time
            process.turnaround_time = current_time + process.execution_time
            current_time += process.execution_time

    def visualize(self):
        """Visualiza el resultado de la simulación del algoritmo FCFS
        en la consola.
        """
        for process in self.processes:
            print(process)


if __name__ == "__main__":
    processes_in = [
        Process("P1", 6),
        Process("P2", 8),
        Process("P3", 9),
        Process("P4", 3),
        Process("P5", 5),
    ]

    fcfs_algorithm = FCFSAlgorithm(processes_in)
    fcfs_algorithm()
    fcfs_algorithm.visualize()
