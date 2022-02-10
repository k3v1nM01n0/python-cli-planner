from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def is_due(self):
        pass
    

class DeadlinedReminder(Iterable, ABC):

    def __init__(self):
        pass

    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        # super().__init__()
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        if self.date < datetime.now():
            print("due")
    