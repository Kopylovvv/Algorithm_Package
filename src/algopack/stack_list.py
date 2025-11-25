class Stack:
    """
    Стек на базе list с поддержкой получения минимума за O(1).
    Некорректные операции (pop/peek/min на пустом стеке) выбрасывают IndexError.[attached_file:1]
    """

    def __init__(self) -> None:
        self._data: list[int] = []
        self._mins: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty stack")
        value = self._data.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def min(self) -> int:
        if not self._mins:
            raise IndexError("min from empty stack")
        return self._mins[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)
