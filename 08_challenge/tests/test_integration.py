from lib.todo import *
from lib.todo_list import *


# Test adding todos - initial state is 'incomplete'
def test_adding_todo():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    assert tdl.incomplete() == [todo1, todo2]


# test marking todo as complete, second todo should remain incomplete
def test_mark_todo_as_complete():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    todo1.mark_complete()
    assert tdl.complete() == [todo1]
    assert tdl.incomplete() == [todo2]


# test marking all as complete - i.e. 'give up'
# incomplete should now be empty
def test_mark_all_as_complete():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    tdl.give_up()
    assert tdl.complete() == [todo1, todo2]
    assert tdl.incomplete() == []
