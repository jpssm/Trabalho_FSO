from process import Process
from process_table import Process_table
from process_queues import Queues

class Process_manager():
    """
    Implements a simplified process manager, with a process table and related utilities.
    """
    def __init__(self) -> None:
        self.main_process = Process(0, "running", 0, 128, 16, 0, 0, 0)
        self.process_table = Process_table(self.main_process)
        self.queues = Queues(self.main_process)
        self.currently_running = self.main_process.pid

    def create_process(self, 
                       parent_pid, 
                       pid, 
                       state, 
                       priority, 
                       offset, 
                       qty_blocks_alloc, 
                       has_printer, 
                       has_scanner, 
                       has_driver):
        """
        Creates a process using the "parent_pid" code to call upon a process 
        to spawn a child.
        """
        if pid in self.process_table.get_keys():    
            raise RuntimeError("PID code already in use")
        
        else:
            new_proc = self.process_table[parent_pid].spawn_process(pid, 
                                                                    state, 
                                                                    priority, 
                                                                    offset, 
                                                                    qty_blocks_alloc, 
                                                                    has_printer, 
                                                                    has_scanner, 
                                                                    has_driver)
            self.process_table.insert_process(new_proc)
        
            self.queues.insert_process(pid, priority)

    def kill_process(self, pid):
        pass

    def check_yield(self):
        return self.process_table[self.currently_running].has_yielded()

    def preempt(self):
        if self.process_table[self.currently_running].get_priority() != 0:
            raise RuntimeError("Priority-0 processes cannot be preempted")
        else:
            next_state = self.process_table[self.currently_running].get_next_state()
            self.process_table[self.currently_running].set_state(next_state)

    def update_running_proces(self, pid):
        old_process_pid = self.currently_running
        self.currently_running = pid
        old_process_next_state = self.process_table[old_process_pid].get_next_state()
        self.process_table[old_process_pid].set_state(old_process_next_state)
        self.process_table[pid].set_state("running")
