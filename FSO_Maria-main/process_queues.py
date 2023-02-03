from process import Process
from typing import List

class Queues():
    """
    Implements 4 priority queues, one for real time processes, 3 for different
    priority tiers of user processes.
    """

    def __init__(self, process: Process) -> None:
        self.real_time_queue = [process.get_pid()]
        priority_1 = []
        priority_2 = []
        priority_3 = []
        self.user_process_queue = {1: priority_1, 
                                   2: priority_2,
                                   3: priority_3}
        self.next_queue = 1

    def insert_in_real_time(self, pid: int) -> None:
        """Inserts process PID into real-time queue"""
        if len(self.real_time_queue) < 1000:
            self.real_time_queue.insert(0, pid)
        else:
            raise RuntimeError("Real time queue is full")

    def get_real_time_process(self) -> int:
        """Returns PID of first-in-line process in real-time queue"""
        return self.real_time_queue.pop()

    def insert_in_user_time(self, pid: int, priority: int) -> None:
        """Inserts process PID into appropriate user-time queue, according to its priority"""
        if len(self.user_process_queue[priority]) < 1000:
            self.user_process_queue[priority].insert(0, pid)
        else:
            raise RuntimeError("Priority" + str(priority) +" queue is full")

    def insert_process(self, pid: int, priority: int) -> None:
        """Inserts a process PID in the appropriate queue, according to its priority"""
        if priority == 0:
            self.insert_in_real_time(pid)
        
        else:
            self.insert_in_user_time(pid, priority)      

    def locate_pid_in_queues(self, pid: int) -> int:
        """Returns the queue number where a given PID is"""
        if pid in self.real_time_queue:
            return 0
        elif pid in self.user_process_queue[1]:
            return 1
        elif pid in self.user_process_queue[2]:
            return 2
        elif pid in self.user_process_queue[3]:
            return 3

    def remove_process(self, pid: int):
        """Removes a process from it's queue"""
        current_loc = self.locate_pid_in_queues(pid)

        if current_loc == 0:
            self.real_time_queue.remove(pid)
        else:
            self.user_process_queue[current_loc].remove(pid)

#    def change_queues(self, pid, priority):
#        current_loc = self.locate_pid_in_queues(pid)
#
#        if priority == current_loc:
#            raise RuntimeError("Process already in the queue")
#        
#        self.remove_process(pid)
#
#        self.insert_process(pid, priority)

    def get_next_queue(self) -> int:
        """Returns from what queue the next process should be taken"""
        return self.next_queue

    def set_next_queue(self, last_queues: List[int]) -> None:
        """Sets what queue shall produce the next process"""
        if last_queues == [1, 2, 1]:
            self.next_queue = 3
        elif last_queues == [2, 1, 3]:
            self.next_queue = 1
        elif last_queues == [1, 3, 1]:
            self.next_queue = 2
        elif last_queues == [3, 1, 2]:
            self.next_queue = 1
