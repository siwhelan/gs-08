from lib.todo_list import *


# test that the initial todo list is empty
def test_initial_completed_state_is_an_empty_list():
    tdl = TodoList()
    assert tdl.complete() == []
    assert tdl.incomplete() == []


# test adding a todo - can get that todo back
def test_add_and_recall_todo():
    tdl = TodoList()
    tdl.add("Water Plants")
    assert tdl.incomplete() == ["Water Plants"]
