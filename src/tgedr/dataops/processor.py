import abc
from typing import Any, Dict, Optional


class ProcessorException(Exception):
    pass


class ProcessorInterface(metaclass=abc.ABCMeta):
    """
    def process(self, context: Optional[Dict[str, Any]] = None) -> Any:
        raise NotImplementedError()
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "process") and callable(subclass.process) or NotImplemented


@ProcessorInterface.register
class Processor(abc.ABC):

    @abc.abstractmethod
    def process(self, context: Optional[Dict[str, Any]] = None) -> Any:
        raise NotImplementedError()
