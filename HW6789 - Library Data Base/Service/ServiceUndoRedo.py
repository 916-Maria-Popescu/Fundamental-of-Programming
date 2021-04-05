from Domain.UndoRedo import UndoOperation, RedoOperation
from Validator.myvalidators import ServiceException


class UndoService:
    __undo_operations = []

    @staticmethod
    def store_operation(service, handler, *parameters):
        UndoService.__undo_operations.append(UndoOperation(service, handler, parameters))

    @staticmethod
    def do_undo():
        if len(UndoService.__undo_operations) == 0:
            raise ServiceException("There is nothing to undo")
        undo_operation = UndoService.__undo_operations.pop()
        print(undo_operation)
        undo_operation.handler(undo_operation.service, *undo_operation.parameters)



class RedoService:
    __redo_operation = []

    @staticmethod
    def store_operation(service, handler, *parameters):
        RedoService.__redo_operation.append(RedoOperation(service, handler, parameters))

    @staticmethod
    def do_redo():
        if len(RedoService.__redo_operation) == 0:
            raise ServiceException("There is nothing to redo")
        redo_operation = RedoService.__redo_operation.pop()
        redo_operation.handler(redo_operation.service, *redo_operation.parameters)

    @staticmethod
    def clear_all_redo():
        RedoService.__redo_operation.clear()


