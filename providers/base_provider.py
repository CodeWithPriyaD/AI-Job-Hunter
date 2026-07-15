from abc import ABC, abstractmethod
from models.job import Job

class BaseProvider(ABC):    
    """ Every job provider must inherit from this class and implement the get_jobs method. """

    @abstractmethod
    def get_jobs(self) -> list[Job]:
        """ This method should return a list of Job objects.   """
        pass
