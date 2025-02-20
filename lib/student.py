#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize with an empty list

    def learn(self, new_knowledge):
        """Adds a new knowledge string to the student's knowledge list."""
        self.knowledge.append(new_knowledge)
