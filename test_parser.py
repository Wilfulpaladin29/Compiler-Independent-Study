from lexer import MyLexer
from parser import MyParser
from pprint import pprint

lexer = MyLexer()
parser = MyParser()

source = """
int age <> 18;
bool isStudent <> true;
char grade <> 'A';

op("Enter your age: ");
ip(age);

int nextAge <> age + 1;
bool isAdult <> age >= 18;

char ageAsChar <> (char) age;
int gradeCode <> (int) grade;

nextAge <> 21;
isStudent <> false;

if (age >= 18) {
    op("You are an adult.");
    op(age);
}

if (isStudent = true) {
    op("You are a student.");
}

if (grade = 'A') {
    op("Excellent grade!");
}

int negNum <> -15;
op("negative number");
ip(negNum);
"""


print("\n=== AST ===")
ast = parser.parse(lexer.tokenize(source))

print("Program:", type(ast).__name__)

for statement in ast.statements:
    print(type(statement).__name__, vars(statement))

print("\n=== PARSING COMPLETE ===")

