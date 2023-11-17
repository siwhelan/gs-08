class TodoList:
    def __init__(self):
        self.todo_list = []
        self.completed = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return self.todo_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return self.completed

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todo_list:
            todo.complete = True
