
from sly import Lexer


class MyLexer(Lexer):

    # All token types our language recognizes
    tokens = {
        INT, BOOL, CHAR, IF, IP, OP,
        TRUE, FALSE,
        ID, NUMBER, CHAR_LITERAL, STRING_LITERAL,
        ASSIGN, EQUALS, NOT_EQUALS,
        PLUS, MINUS, TIMES, DIVIDE,
        LESS, GREATER, LESS_EQUAL, GREATER_EQUAL,
        AND, OR,
        LPAREN, RPAREN, LBRACE, RBRACE, SEMICOLON
    }

    # Ignore spaces and tabs
    ignore = ' \t'

    # Ignore single-line comments
    ignore_comment = r'//[^\n]*'

    # Assignment and comparison operators
    ASSIGN = r'<>'
    NOT_EQUALS = r'!='
    LESS_EQUAL = r'<='
    GREATER_EQUAL = r'>='
    EQUALS = r'='
    LESS = r'<'
    GREATER = r'>'

    # Arithmetic operators
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'

    # Logical operators
    AND = r'&&'
    OR = r'\|\|'

    # Punctuation
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    SEMICOLON = r';'

    # Literals and identifiers
    STRING_LITERAL = r'"([^"\\]|\\.)*"'
    CHAR_LITERAL = r"'([^'\\]|\\.)'"

    # Convert number tokens to integers
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Keywords
    ID['int'] = INT
    ID['bool'] = BOOL
    ID['char'] = CHAR
    ID['if'] = IF
    ID['ip'] = IP
    ID['op'] = OP
    ID['true'] = TRUE
    ID['false'] = FALSE

    # Track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Invalid character detection
    def error(self, t):
        print(
            f"Illegal character {t.value[0]!r} "
            f"at line {self.lineno}"
        )
        self.index += 1


# Run the lexer independently
if __name__ == "__main__":

    lexer = MyLexer()

    with open("test.lang", "r") as file:
        source_code = file.read()

    for token in lexer.tokenize(source_code):
        print(token.type, token.value)
