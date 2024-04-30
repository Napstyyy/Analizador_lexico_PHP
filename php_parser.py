from re import VERBOSE
import ply.yacc as yacc
from php_lexer import tokens
import php_lexer
import sys

VERBOSE = 1


def p_script(p):
    '''script :   script_section
              |   script script_section'''

def p_script_section(p):
    '''script_section :   start_tag
                    |   statement_list
                    |   end_tag'''

def p_start_tag(p):
    '''start_tag :   OPEN_TAG
                    |   OPEN_TAG_WITH_ECHO'''

def p_end_tag(p): 
    '''end_tag :   CLOSE_TAG'''

def p_function_static_declaration(p):
    '''function_static_declaration :   STATIC static_variable_name_list ENDLINE''' 

def p_static_variable_name_list(p):
    '''static_variable_name_list :      static_variable_declaration
                                    |   static_variable_name_list COMMA static_variable_declaration'''

def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA: " + str(p.lexer.lineno) + " NO SE ESPERABA EL TOKEN " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " + str(p.lexer.lineno))
    else:
        raise Exception("syntax", "error")

parser = yacc.yacc()

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = "index.php"
    f = open(fin, "r")
    data = f.read()
    parser.parse(data, tracking = True)
    print("Amigazo, que chimba de parser. Completamente parsero")
