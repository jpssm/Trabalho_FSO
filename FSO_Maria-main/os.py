from process import Process
from process_table import Process_table
from process_queues import Queues
from process_manager import Process_manager
from time import sleep

class OS():

    def __init__(self) -> None:
        self.process_manager = Process_manager()
        self.time = 0
        self.quantum = 0.001

    def run(self):
        while True:
            sleep(self.quantum)


    