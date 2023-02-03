from process import Process

class Memory():

    def __init__(self, process: Process) -> None:
        memory = [process.get_pid()]

    def insert_in_memory(self, pid, qty_blocks_alloc):
        while qty_blocks_alloc:
            if len(self.memory) < 1024:
                self.memory.insert(0, pid)
            else:
                raise RuntimeError("Memory queue is full")
            qty_blocks_alloc-=1