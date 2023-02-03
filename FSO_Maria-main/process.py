

class Process():
    """
    Implements a process, with it's relevant information and necessary methods.

    attributes:
    ---------------
    pid: int = the process PID,
    state: string = the running state of the process, can be 'running', 'ready' or 'blocked

    """

    def __init__(self,
                 pid: int, 
                 state: str, 
                 priority: int, 
                 age: int, 
                 offset: int, 
                 qty_blocks_alloc: int, 
                 has_printer: bool, 
                 has_scanner: bool, 
                 has_driver: bool,
                 duration: int) -> None:
        self.pid = pid
        self.state = state
        self.priority = priority
        self.age = age
        self.offset = offset
        self.qty_blocks_alloc = qty_blocks_alloc
        self.has_printer = has_printer
        self.has_scanner = has_scanner
        self.has_driver = has_driver
        self.duration = duration
        self.has_yielded = False
        self.next_state = "ready" 

    def get_pid(self) -> int:
        return self.pid
    
    def get_state(self) -> str:
        return self.state

    def set_state(self, state) -> None:
        self.state = state

    def get_priority(self) -> int:
        return self.priority

    def get_age(self) -> int:
        return self.age

    def increment_age(self) -> None:
        self.age += 1

    def get_offset(self) -> int:
        return self.offset

    def get_qty_blocks_alloc(self) -> int:
        return self.qty_blocks_alloc

    def set_qty_blocks_alloc(self, qty_blocks_alloc) -> None:
        self.qty_blocks_alloc = qty_blocks_alloc

    def get_printer_status(self) -> bool:
        return self.has_printer

    def set_printer_status(self, has_printer) -> bool:
        self.has_printer = has_printer

    def get_scanner_status(self) -> bool:
        return self.has_scanner

    def set_scanner_status(self, scanner_status) -> None:
        self.scanner_status = scanner_status

    def get_driver_status(self) -> bool:
        return self.has_driver

    def set_driver_status(self, driver_status) -> None:
        self.driver_status = driver_status

    def get_duration(self) -> int:
        return self.duration
    
    def decrement_duration(self) -> None:
        self.duration -= 1

    def get_has_yielded(self) -> bool:
        return self.has_yielded

    def swap_yield(self) -> None:
        self.has_yielded = not self.has_yielded

    def get_next_state(self) -> str:
        return self.next_state

    def set_next_state(self, next_state) -> None:
        self.next_state = next_state

    def spawn_process(self,
                      pid: int, 
                      state: str, 
                      priority: int, 
                      age: int, 
                      offset: int, 
                      qty_blocks_alloc: int, 
                      has_printer: bool, 
                      has_scanner: bool, 
                      has_driver: bool,
                      duration: int) -> None:
        if self.pid == 0:
            raise RuntimeError("Cannot recreate main process.")
        else:
            return Process(pid,
                           state, 
                           priority, 
                           age, 
                           offset, 
                           qty_blocks_alloc, 
                           has_printer, 
                           has_scanner, 
                           has_driver,
                           duration)
            