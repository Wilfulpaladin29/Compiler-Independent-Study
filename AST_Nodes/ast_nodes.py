class Number:
    def __init__(self, value):
        self.value = value


class Bool:
    def __init__(self, value):
        self.value = value


class BinaryOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class Character:
    def __init__(self, character):
        self.character = character


class String:
    def __init__(self, string):
        self.string = string


class Variable:
    def __init__(self, identity):
        self.identity = identity


class UnaryOp:
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression


class Cast:
    def __init__(self, target_type, expression):
        self.target_type = target_type
        self.expression = expression


class Declaration:
    def __init__(self, variable_type, name, expression):
        self.variable_type = variable_type
        self.name = name
        self.expression = expression


class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression


class Input:
    def __init__(self, name):
        self.name = name


class Output:
    def __init__(self, expression):
        self.expression = expression


class IfStatement:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class Block:
    def __init__(self, statements):
        self.statements = statements


class Program:
    def __init__(self, statements):
        self.statements = statements
class Number:
    def __init__(self, value):
        self.value = value

class Bool:
    def __init__(self, value):
        self.value = value

class BinaryOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class Character:
    def __init__(self, character):
        self.character = character

class String:
    def __init__(self, string):
        self.string = string

class Variable:
    def __init__(self, identity):
        self.identity = identity
