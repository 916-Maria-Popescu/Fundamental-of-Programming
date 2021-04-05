from dataclasses import dataclass


@dataclass
class UndoOperation:
    """
    Data class for undo operation object
    """
    service: object
    handler: object
    parameters: tuple


@dataclass
class RedoOperation:
    """
    Data class for redo operation object
    """
    service: object
    handler: object
    parameters: tuple
