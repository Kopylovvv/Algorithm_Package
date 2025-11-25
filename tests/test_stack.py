import pytest
from algopack.stack_list import Stack


def test_stack_push_pop_lifo() -> None:
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert len(s) == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_stack_peek_does_not_remove() -> None:
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert len(s) == 2
    assert not s.is_empty()


def test_stack_pop_on_empty_raises() -> None:
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_stack_peek_on_empty_raises() -> None:
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_stack_min_tracks_current_minimum() -> None:
    s = Stack()
    s.push(5)
    assert s.min() == 5
    s.push(3)
    assert s.min() == 3
    s.push(7)
    assert s.min() == 3
    s.push(2)
    assert s.min() == 2

    assert s.pop() == 2
    assert s.min() == 3

    assert s.pop() == 7
    assert s.min() == 3

    assert s.pop() == 3
    assert s.min() == 5


def test_stack_min_on_empty_raises() -> None:
    s = Stack()
    with pytest.raises(IndexError):
        s.min()
