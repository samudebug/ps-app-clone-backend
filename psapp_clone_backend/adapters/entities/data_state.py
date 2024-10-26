from typing import Optional


class DataState[T]:
    data: Optional[T] = None
    error: Optional[Exception] = None

    def __init__(self, data: Optional[T] = None, error: Optional[Exception] = None) -> None:
        self.data = data
        self.error = error
    

