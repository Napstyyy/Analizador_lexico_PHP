import ply.lex as lex
import sys

tokens = (
    'ABSTRACT',
    'AMPERSAND',
    'AND_EQUAL',
    'ARRAY',
    'ARRAY_CAST',
    'AS',
    'ATTRIBUTE',
    'BOOLEAN_AND',
    'BOOLEAN_OR',
    'BOOL_CAST',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLASS_C',
    'CLONE',
    'CLOSE_TAG',
    'COALESCE',
    'COALESCE_EQUAL',
    'COMMENT',
    'CONCAT_EQUAL',
    'CONST',
    'CONSTANT_ENCAPSED_STRING',
    'CONTINUE',
    # 'CURLY_OPEN',
    'DEC',
    'DECLARE',
    'DEFAULT',
    'DIR',
    'DIV_EQUAL',
    'DNUMBER',
    'DO',
    'DOC_COMMENT',
    # 'DOLLAR_OPEN_CURLY_BRACES',
    'DOUBLE_ARROW',
    'DOUBLE_CAST',
    'DOUBLE_COLON',
    'ECHO',
    'ELLIPSIS',
    'ELSE',
    'ELSEIF',
    'EMPTY',
    'ENCAPSED_AND_WHITESPACE',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'ENUM',
    'EVAL',
    'EXIT',
    'EXTENDS',
    'FILE',
    'FINAL',
    'FINALLY',
    'FN',
    'FOR',
    'FOREACH',
    'FUNCTION',
    'FUNC_C',
    'GLOBAL',
    'GOTO',
    'HALT_COMPILER',
    'IF',
    'IMPLEMENTS',
    'INC',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCE_OF',
    'INSTEADOF',
    'INTERFACE',
    'INT_CAST',
    'ISSET',
    'IS_EQUAL',
    'IS_GREATER_OR_EQUAL',
    'IS_IDENTICAL',
    'IS_NOT_EQUAL',
    'IS_NOT_IDENTICAL',
    'IS_SMALLER_OR_EQUAL',
    'LINE',
    'LIST',
    'LNUMBER',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_XOR',
    'MATCH',
    'METHOD_C',
    'MINUS_EQUAL',
    'NAMESPACE',
    'NAME_FULLY_QUALIFIED',
    'NAME_QUALIFIED',
    'NEW',
    'NS_C',
    'NS_SEPARATOR',
    'NUM_STRING',
    'OBJECT_CAST',
    'OBJECT_OPERATOR',
    'NULLSAFE_OBJECT_OPERATOR',
    'OPEN_TAG',
    'OPEN_TAG_WITH_ECHO',
    'OR_EQUAL',
    'PLUS_EQUAL',
    'POW',
    'POW_EQUAL',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'READONLY',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'SL',
    'SL_EQUAL',
    'SPACESHIP',
    'SR',
    'SR_EQUAL',
    'HEREDOC',
    'STATIC',
    'STRING',
    'STRING_CAST',
    'STRING_VARNAME',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRAIT_C',
    'TRY',
    'UNSET',
    'UNSET_CAST',
    'USE',
    'VAR',
    'VARIABLE',
    'WHILE',
    'WHITESPACE',
    'XOR_EQUAL',
    'YIELD',
    'YIELD_FROM',
    'OPAR',
    'CPAR',
    'ENDLINE',
    'ASSIGN',
    'OBRA',
    'CBRA',
    'CONCAT',
    'COMMA',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'MAP_ITEM',
    'LT',
    'GT',
    'DOLLAR',
    'OBRACK',
    'CBRACK',
    'BACKQUOTE',
    'SELF',
    'PARENT',
    'NEG',
    'AT',
    'BINARY',
    'BOOL',
    'BOOLEAN',
    'DOUBLE',
    'INT',
    'INTEGER',
    'FLOAT',
    'OBJECT',
    'REAL',
    'STRINGKW',
    'NOT',
    'MOD',
    'BITWISE_XOR',
    'BITWISE_OR',
    'CONDITIONAL',
    'COLON',
    'TICKS',
    'ENCODING',
    'STRICT_TYPES'
    
)

#Regular expression rules for simple tokens
t_AMPERSAND = r'\&'
t_OPAR = r'\('
t_CPAR = r'\)'
t_ENDLINE = r'\;'
t_ASSIGN = r'='
t_OBRA = r'\{'
t_CBRA = r'\}'
t_CONCAT = r'\.'
t_COMMA = r'\,'
t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_LT = r'\<'
t_GT = r'\>'
t_DOLLAR = r'\$'
t_OBRACK = r'\['
t_CBRACK = r'\]'
t_NEG = r'\~'
t_AT = r'\@'
t_NOT = r'!'
t_BITWISE_XOR = r'\^'
t_BITWISE_OR = r'\|'
t_CONDITIONAL = r'\?'
t_COLON = r'\:'

def t_AND_EQUAL(t):
    r'\&='
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_ARRAY_CAST(t):
    r'\(array\)'
    return t

def t_AS(t):
    r'as'
    return t

def t_ATTRIBUTE(t):
    r'\#\['
    return t

def t_BOOLEAN_AND(t):
    r'\&\&'
    return t

def t_BOOLEAN_OR(t):
    r'\|\|'
    return t

def t_BOOL_CAST(t):
    r'\(bool\)'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLASS_C(t):
    r'\_\_CLASS\_\_'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CLOSE_TAG(t):
    r'\?\>'
    return t

def t_COALESCE(t):
    r'\?\?'
    return t

def t_COALESCE_EQUAL(t):
    r'\?\?='
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONCAT_EQUAL(t):
    r'\.='
    return t

def t_CONSTANT_ENCAPSED_STRING(t):
    r'("[^"]*")|(\'.*\')|(\`.*\`)'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

# def t_CURLY_OPEN(t):
#     r'\{\$'
#     return t

def t_DEC(t):
    r'--'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DIR(t):
    r'\_\_DIR\_\_'
    return t

def t_DNUMBER(t):
    r'\d+(\.\d+)?(e(\-)?\d+(.\d+)?)?'
    return t

def t_DO(t):
    r'do'
    return t

# def t_DOLLAR_OPEN_CURLY_BRACES(t):
#     r'\$\{'
#     return t

def t_DOUBLE_ARROW(t):
    r'=\>'
    return t

def t_DOUBLE_CAST(t):
    r'\(double\)'
    return t

def t_DOUBLE_COLON(t):
    r'\:\:'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELLIPSIS(t):
    r'\.\.\.'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_ENCAPSED_AND_WHITESPACE(t):
    r'\".*\$.*\"'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_ENUM(t):
    r'enum'
    return t

def t_EVAL(t):
    r'eval\(\)'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FILE(t):
    r'\_\_FILE\_\_'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FN(t):
    r'fn'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_FUNC_C(t):
    r'\_\_FUNCTION\_\_'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_HALT_COMPILER(t):
    r'\_\_halt\_compiler\(\)'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INC(t):
    r'\+\+'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INCLUDE_ONCE(t):
    r'include\_once'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INSTEADOF(t):
    r'insteadof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_INT_CAST(t):
    r'\(int\)'
    return t

def t_ISSET(t):
    r'isset\(\)'
    return t

def t_IS_EQUAL(t):
    r'=='
    return t

def t_IS_GREATER_OR_EQUAL(t):
    r'\>='
    return t

def t_IS_IDENTICAL(t):
    r'==='
    return t

def t_IS_NOT_EQUAL(t):
    r'\!='
    return t

def t_IS_NOT_IDENTICAL(t):
    r'\!=='
    return t

def t_IS_SMALLER_OR_EQUAL(t):
    r'\<='
    return t

def t_LINE(t):
    r'\_\_LINE\_\_'
    return t

def t_LIST(t):
    r'list'
    return t

def t_LNUMBER(t):
    r'\d+'
    return t

def t_LOGICAL_AND(t):
    r'and'
    return t

def t_LOGICAL_OR(t):
    r'or'
    return t

def t_LOGICAL_XOR(t):
    r'xor'
    return t

def t_MATCH(t):
    r'match'
    return t

def t_METHOD_C(t):
    r'\_\_METHOD\_\_'
    return t

def t_MINUS_EQUAL(t):
    r'-='
    return t

def t_MOD_EQUAL(t):
    r'\%='
    return t

def t_MUL_EQUAL(t):
    r'\*='
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NAME_FULLY_QUALIFIED(t):
    r'\\\w+\\w+'
    return t

def t_NAME_QUALIFIED(t):
    r'\w+\\w+'
    return t

def t_NEW(t):
    r'new'
    return t

def t_NS_C(t):
    r'\_\_NAMESPACE\_\_'
    return t

def t_NS_SEPARATOR(t):
    r'\\'
    return t

def t_OBJECT_CAST(t):
    r'\(object\)'
    return t

def t_OBJECT_OPERATOR(t):
    r'-\>'
    return t

def t_NULLSAFE_OBJECT_OPERATOR(t):
    r'\?-\>'
    return t

def t_OPEN_TAG(t):
    r'\<\?php'
    return t

def t_OPEN_TAG_WITH_ECHO(t):
    r'\<\?='
    return t

def t_OR_EQUAL(t):
    r'\|='
    return t

def t_PLUS_EQUAL(t):
    r'\+='
    return t

def t_DOC_COMMENT(t):
    r'/\*\*(.|\n)*\*/'
    pass

def t_POW(t):
    r'\*\*'
    return t

def t_POW_EQUAL(t):
    r'\*\*='
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_READONLY(t):
    r'readonly'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require\_once'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_HEREDOC(t):
    r'\<\<\<EOD[\S\s]*EOD'
    return t

def t_SL(t):
    r'\<\<'
    return t

def t_SL_EQUAL(t):
    r'\<\<='
    return t

def t_SPACESHIP(t):
    r'\<=\>'
    return t

def t_SR(t):
    r'\>\>'
    return t

def t_SR_EQUAL(t):
    r'\>\>='
    return t


def t_STATIC(t):
    r'static'
    return t


def t_STRING_CAST(t):
    r'\(string\)'
    return t

def t_STRING_VARNAME(t):
    r'\"\$\{[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*\}'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRAIT(t):
    r'trait'
    return t

def t_TRAIT_C(t):
    r'\_\_TRAIT\_\_'
    return t

def t_TRY(t):
    r'try'
    return t

def t_UNSET_CAST(t):
    r'\(unset\)'
    return t

def t_USE(t):
    r'use'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_WHITESPACE(t):
    r'\t \r\n'
    return t

def t_XOR_EQUAL(t):
    r'\^='
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_YIELD_FROM(t):
    r'yield from'
    return t

def t_BINARY(t):
    r'binary'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_INT(t):
    r'int'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_REAL(t):
    r'real'
    return t

def t_STRINGKW(t):
    r'string'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t_STRING(t):
    r'[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    return t

def t_NUM_STRING(t):
    r'\"\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*(\[\d+\])+\"'
    return t

def t_MAP_ITEM(t):
    r'\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*((\[\d+\])|(\[(\"|\').*(\"|\')\]))+'
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    return t

def t_SELF(t):
    r'self'
    return t

def t_PARENT(t):
    r'parent'
    return t

def t_COMMENT(t):
    r'//.*\n'
    pass

def t_TICKS(t):
    r'ticks'
    return t

def t_ENCODING(t):
    r'encoding'
    return t

def t_STRICT_TYPES(t):
    r'strict_types'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Error léxico: Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        file = sys.argv[1]
    else:
        file = 'index.php'
    f = open(file, 'r')
    data = f.read()
    lexer.input(data)
    test(data, lexer)

