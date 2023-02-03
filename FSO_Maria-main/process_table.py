from process import Process

class Process_table():

    """
    Implements a process table as a dictionary
    """

    def __init__(self, process: Process) -> None:
        self.process_table = {process.get_pid(): process}

    def get_table_processes(self):
        return list(self.process_table.keys())

    def kill_process(self, pid):
        self.process_table.pop(pid)

    def change_priority(self, pid, priority):
        self.process_table[pid].set_priority(priority)

    #def change_process_state(self, pid, state):
    #    self.process_table[pid].set_state(state)

    def insert_process(self, process):
        self.process_table[process.get_pid()] = process
    
    