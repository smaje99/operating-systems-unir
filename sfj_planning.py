"""Algoritmos de Planificación SJF"""

from dataclasses import dataclass


@dataclass()
class Process:
    """Clase que representa un proceso en un algoritmo de planificación.

    Attributes:
        name (str): El nombre único del proceso.
        arrival_time (int): El tiempo en el que el proceso
            llega al sistema.
        execution_time (int): El tiempo necesario para que
            el proceso se ejecute.
        waiting_time (int, opcional): El tiempo de espera
            del proceso (calculado).
        turnaround_time (int, opcional): El tiempo de retorno
            del proceso (calculado).
    """

    name: str
    arrival_time: int
    execution_time: int
    waiting_time: int = 0
    turnaround_time: int = 0

    def __str__(self):
        return (
            f"Proceso {self.name}: "
            + f"Llegada={self.arrival_time}, "
            + f"Ejecución={self.execution_time}, "
            + f"Tiempo de Espera={self.waiting_time}, "
            + f"Tiempo de Retorno={self.turnaround_time}"
        )


class SJFAlgorithm:
    """Clase que implementa el algoritmo Shortest Job First (SJF).

    El algoritmo SJF ordena los procesos en función de su tiempo de ejecución
    más corto y los ejecuta en ese orden.

    Attributes:
        processes (List[Process]): Una lista de objetos Process que representan
        los procesos a planificar.
    """

    def __init__(self, processes: list[Process]):
        self.processes = processes

    def __call__(self):
        """Ejecuta el algoritmo SJF.

        Este método ordena los procesos en función de su tiempo de ejecución
        más corto y luego calcula el tiempo de espera y el tiempo de retorno
        de cada proceso.
        """

        # Ordenar por tiempo de ejecución
        self.processes.sort(key=lambda process: process.execution_time)

        current_time = 0
        total_waiting_time = 0
        total_turnaround_time = 0

        for process in self.processes:
            process.waiting_time = current_time
            process.turnaround_time = current_time + process.execution_time
            total_waiting_time += current_time
            total_turnaround_time += process.turnaround_time
            current_time += process.execution_time

        average_waiting_time = total_waiting_time / len(self.processes)
        average_turnaround_time = total_turnaround_time / len(self.processes)

        return average_waiting_time, average_turnaround_time

    def visualize(self):
        """Visualiza el resultado de la simulación del algoritmo SJF
        en la consola.
        """
        for process in self.processes:
            print(process)


if __name__ == "__main__":
    processes_in = [
        Process("P1", 0, 6),
        Process("P2", 1, 8),
        Process("P3", 2, 7),
        Process("P4", 3, 3),
        Process("P5", 4, 5),
    ]

    sjf = SJFAlgorithm(processes_in)
    sjf()
    sjf.visualize()
