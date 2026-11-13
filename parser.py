
from sly import Parser
from lexer import MyLexer
from ast_nodes import (
    Number, Bool, BinaryOp, Character, String,
    Variable, UnaryOp, Cast, Declaration,
    Assignment, Input, Output, IfStatement,
    Block, Program
)


class MyParser(Parser):

    tokens = MyLexer.tokens
    start = 'program'

    # Operator precedence (lowest to highest)
    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('nonassoc', 'EQUALS', 'NOT_EQUALS'),
        ('nonassoc', 'LESS', 'GREATER',
         'LESS_EQUAL', 'GREATER_EQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UNARY'),
    )

    # PROGRAM

    @_('statements')
    def program(self, p):
        return Program(p.statements)

    @_('')
    def program(self, p):
        return Program([])

    # STATEMENT LISTS

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    # DECLARATIONS

    @_('INT ID ASSIGN expression SEMICOLON')
    def declaration(self, p):
        return Declaration('int', p.ID, p.expression)

    @_('BOOL ID ASSIGN expression SEMICOLON')
    def declaration(self, p):
        return Declaration('bool', p.ID, p.expression)

    @_('CHAR ID ASSIGN expression SEMICOLON')
    def declaration(self, p):
        return Declaration('char', p.ID, p.expression)

    # ASSIGNMENTS

    @_('ID ASSIGN expression SEMICOLON')
    def assignment(self, p):
        return Assignment(p.ID, p.expression)

    # INPUT / OUTPUT

    @_('IP LPAREN ID RPAREN SEMICOLON')
    def input_statement(self, p):
        return Input(p.ID)

    @_('OP LPAREN expression RPAREN SEMICOLON')
    def output_statement(self, p):
        return Output(p.expression)

    # STATEMENTS

    @_('declaration')
    def statement(self, p):
        return p.declaration

    @_('assignment')
    def statement(self, p):
        return p.assignment

    @_('input_statement')
    def statement(self, p):
        return p.input_statement

    @_('output_statement')
    def statement(self, p):
        return p.output_statement

    @_('if_statement')
    def statement(self, p):
        return p.if_statement

    # IF STATEMENTS

    @_('IF LPAREN expression RPAREN block')
    def if_statement(self, p):
        return IfStatement(p.expression, p.block)

    # BLOCKS

    @_('LBRACE statements RBRACE')
    def block(self, p):
        return Block(p.statements)

    @_('LBRACE RBRACE')
    def block(self, p):
        return Block([])

    # LITERALS

    @_('NUMBER')
    def expression(self, p):
        return Number(p.NUMBER)

    @_('TRUE')
    def expression(self, p):
        return Bool(True)

    @_('FALSE')
    def expression(self, p):
        return Bool(False)

    @_('CHAR_LITERAL')
    def expression(self, p):
        return Character(p.CHAR_LITERAL)

    @_('STRING_LITERAL')
    def expression(self, p):
        return String(p.STRING_LITERAL)

    # VARIABLES

    @_('ID')
    def expression(self, p):
        return Variable(p.ID)

    # ARITHMETIC

    @_('expression PLUS expression')
    def expression(self, p):
        return BinaryOp(
            'PLUS', p.expression0, p.expression1
        )

    @_('expression MINUS expression')
    def expression(self, p):
        return BinaryOp(
            'MINUS', p.expression0, p.expression1
        )

    @_('expression TIMES expression')
    def expression(self, p):
        return BinaryOp(
            'TIMES', p.expression0, p.expression1
        )

    @_('expression DIVIDE expression')
    def expression(self, p):
        return BinaryOp(
            'DIVIDE', p.expression0, p.expression1
        )

    # COMPARISONS

    @_('expression GREATER expression')
    def expression(self, p):
        return BinaryOp(
            'GREATER', p.expression0, p.expression1
        )

    @_('expression LESS expression')
    def expression(self, p):
        return BinaryOp(
            'LESS', p.expression0, p.expression1
        )

    @_('expression GREATER_EQUAL expression')
    def expression(self, p):
        return BinaryOp(
            'GREATER_EQUAL', p.expression0, p.expression1
        )

    @_('expression LESS_EQUAL expression')
    def expression(self, p):
        return BinaryOp(
            'LESS_EQUAL', p.expression0, p.expression1
        )

    @_('expression EQUALS expression')
    def expression(self, p):
        return BinaryOp(
            'EQUALS', p.expression0, p.expression1
        )

    @_('expression NOT_EQUALS expression')
    def expression(self, p):
        return BinaryOp(
            'NOT_EQUALS', p.expression0, p.expression1
        )

    # BOOLEAN OPERATORS

    @_('expression AND expression')
    def expression(self, p):
        return BinaryOp(
            'AND', p.expression0, p.expression1
        )

    @_('expression OR expression')
    def expression(self, p):
        return BinaryOp(
            'OR', p.expression0, p.expression1
        )

    # NEGATIVE NUMBERS

    @_('MINUS expression %prec UNARY')
    def expression(self, p):
        return UnaryOp('MINUS', p.expression)

    # TYPE CASTING

    @_('LPAREN INT RPAREN expression %prec UNARY')
    def expression(self, p):
        return Cast('int', p.expression)

    @_('LPAREN CHAR RPAREN expression %prec UNARY')
    def expression(self, p):
        return Cast('char', p.expression)

    @_('LPAREN BOOL RPAREN expression %prec UNARY')
    def expression(self, p):
        return Cast('bool', p.expression)

    # PARENTHESES

    @_('LPAREN expression RPAREN')
    def expression(self, p):
        return p.expression

    # ERROR HANDLING

    def error(self, token):
        if token:
            raise SyntaxError(
                f"Unexpected token {token.type} "
                f"({token.value!r}) at line {token.lineno}"
            )

        raise SyntaxError("Unexpected end of input")
