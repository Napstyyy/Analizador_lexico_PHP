import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'PHP_CODE',
    'HTML_TAG',
    'HTML_CONTENT',
    'DOCTYPE'
)

def t_PHP_CODE(t):
    r'\<\?php([\s\S]*?)\?\>'
    return t

def t_HTML_TAG(t):
    r'\<(\/?[a-zA-Z][^\s>\/]*)([^>]*)>'
    return t

def t_DOCTYPE(t):
    r'\<!DOCTYPE[\s\S]*?\>'
    return t

def t_HTML_CONTENT(t):
    r'[^<]+'
    return t

def t_comment(t):
    r'//.*\n'
    pass

t_ignore = ' \t\n'

def t_error(t):
    print("Error léxico: Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_php_code(p):
    'start : PHP_CODE'
    print("El código PHP es válido.")

def p_html_code(p):
    '''
    start : HTML_TAG
          | HTML_CONTENT
          | DOCTYPE
    '''
    print("El código HTML es válido.")

def p_error(p):
    if p:
        print("Error sintáctico en '%s'" % p.value)
    else:
        print("Error sintáctico al final del archivo")

parser = yacc.yacc()

def parse_php_code(php_code):
    parser.parse(php_code)

def read_php_code_from_file(file_path):
    with open(file_path, 'r') as file:
        php_code = file.read()
    return php_code

if __name__ == '__main__':
    file_path = "./index.php"
    php_code = read_php_code_from_file(file_path)
    parse_php_code(php_code)
