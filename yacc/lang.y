%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
int yyerror(char *s);

#define YYDEBUG 1
%}

%token DEF
%token STRING
%token INT
%token SPACE
%token BACK_TICK
%token READ
%token PRINT
%token IF
%token ELSE
%token WHILE
%token EXIT
%token GO
%token BYE

%token IDENTIFIER
%token INT_CONSTANT
%token STRING_CONSTANT

%token EQ
%token NE
%token LE
%token GE
%token LT
%token GT
%token DBLEQ

%left '+' '-' '*' '/'

%token PLUS
%token MINUS
%token DIV
%token MOD
%token MUL
%token POWER

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET

%token SEMI_COLON
%token COLON

%token TRUE
%token FALSE

%start program

%%
program : GO tempDecl BYE ;
tempDecl : /*Empty*/ | declList tempDecl | stmtList tempDecl ;
declList : declaration | declaration declList ;
declaration :  DEF IDENTIFIER COLON type SEMI_COLON | DEF IDENTIFIER COLON type EQ expression SEMI_COLON ;
type1 : STRING | INT ;
arraydecl : OPEN_RIGHT_BRACKET type1 CLOSED_RIGHT_BRACKET ;
type :  type1 | arraydecl ;
stmtList : stmt | stmt stmtList ;
stmt : simplstmt | structstmt ;
simplstmt : assignstmt | iostmt ;
assignstmt : IDENTIFIER EQ expression SEMI_COLON ;
expression : number_expression | string_expression ;
number_expression : number_expression PLUS term | number_expression MINUS term | term ;
term : term MUL factor | term DIV factor | term MOD factor | term POWER factor | factor ;
factor : OPEN_ROUND_BRACKET number_expression CLOSED_ROUND_BRACKET | IDENTIFIER | INT_CONSTANT {printf("at int\n");}  ;
string_expression : STRING_CONSTANT | IDENTIFIER;
iostmt : READ OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET SEMI_COLON| PRINT OPEN_ROUND_BRACKET string_expression CLOSED_ROUND_BRACKET SEMI_COLON ;
structstmt : ifstmt | whilestmt | exitstmt ;
body : OPEN_CURLY_BRACKET stmtList CLOSED_CURLY_BRACKET | stmt ;
ifstmt : IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET body | OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET body ELSE body ;
whilestmt : WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET body ;
exitstmt : EXIT expression SEMI_COLON ;
condition : expression relation expression ;
relation : LT | LE | DBLEQ | GE | GT | NE ;

%%
yyerror(char *s)
{
	printf("err: %s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
    if (argc > 1)
        yyin = fopen(argv[1], "r");
    if (!yyparse())
        fprintf(stderr, "\tOK\n");
}
