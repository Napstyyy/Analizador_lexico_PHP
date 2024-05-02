from re import VERBOSE
import ply.yacc as yacc
from php_lexer import tokens
import php_lexer
import sys

VERBOSE = 1


def p_script(p):
    '''script                           :   script_section
                                        |   script script_section'''

def p_script_section(p):
    '''script_section                   :   start_tag statement_list end_tag
                                        |   start_tag end_tag
                                        |   start_tag statement_list
                                        |   start_tag'''

def p_start_tag(p):
    '''start_tag                        :   OPEN_TAG
                                        |   OPEN_TAG_WITH_ECHO'''

def p_end_tag(p): 
    '''end_tag                          :   CLOSE_TAG'''

def p_function_static_declaration(p):
    '''function_static_declaration      :   STATIC static_variable_name_list ENDLINE''' 

def p_static_variable_name_list(p):
    '''static_variable_name_list        :   static_variable_declaration
                                        |   static_variable_name_list COMMA static_variable_declaration'''

def p_static_variable_declaration(p):
    '''static_variable_declaration      :   VARIABLE function_static_initializer
                                        |   VARIABLE'''

def p_function_static_initializer(p):
    '''function_static_initializer      :   ASSIGN constant_expression'''

def p_global_declaration(p):
    '''global_declaration               :   GLOBAL variable_name_list ENDLINE'''

def p_variable_name_list(p):
    '''variable_name_list               :   simple_variable
                                        |   variable_name_list COMMA simple_variable'''

def p_primary_expression(p):
    '''primary_expression               :   variable
                                        |   class_constant_access_expression
                                        |   constant_access_expression
                                        |   literal
                                        |   array_creation_expression
                                        |   intrinsic
                                        |   anonymous_function_creation_expression
                                        |   object_creation_expression
                                        |   postfix_increment_expression
                                        |   postfix_decrement_expression
                                        |   prefix_increment_expression
                                        |   prefix_decrement_expression
                                        |   byref_assignment_expression
                                        |   shell_command_expression
                                        |   OPAR expression CPAR'''

def p_simple_variable(p):
    '''simple_variable                  :   variable_name
                                        |   DOLLAR simple_variable
                                        |   DOLLAR OBRA expression CBRA'''

def p_dereferencable_expression(p):
    '''dereferencable_expression        :   VARIABLE
                                        |   OBRA expression CBRA
                                        |   array_creation_expression
                                        |   string_literal'''
def p_callable_expression(p):
    '''callable_expression              :   callable_variable
                                        |   OPAR expression CPAR
                                        |   array_creation_expression
                                        |   string_literal'''
def p_callable_variable(p):
    '''callable_variable                :   simple_variable
                                        |   subscript_expression
                                        |   member_call_expression
                                        |   scoped_call_expression
                                        |   function_call_expression'''
def p_variable(p):
    '''variable                         :   callable_variable
                                        |   scoped_property_access_expression
                                        |   member_access_expression'''

def p_constant_access_expression(p):
    '''constant_access_expression       :   qualified_name'''

def p_literal(p):
    '''literal                          :   integer_literal
                                        |   floating_literal
                                        |   string_literal'''

def p_intrinsic(p):
    '''intrinsic                        :   empty_intrinsic
                                        |   eval_intrinsic
                                        |   exit_intrinsic
                                        |   isset_intrinsic'''

def p_empty_intrinsic(p):
    '''empty_intrinsic                  :   EMPTY OPAR expression CPAR'''

def p_eval_intrinsic(p):
    '''eval_intrinsic                   :   EVAL OPAR expression CPAR'''

def p_exit_intrinsic(p):
    '''exit_intrinsic                   :   EXIT
                                        |   EXIT OPAR expression CPAR
                                        |   DIE
                                        |   DIE OPAR expression CPAR'''
def p_isset_intrinsic(p):
    '''isset_intrinsic                  :   ISSET OPAR variable_list CPAR'''

def p_variable_list(p):
    '''variable_list                    :   variable
                                        |   variable_list COMMA variable'''

def p_anonymous_function_creation_expression(p):
    '''anonymous_function_creation_expression :   STATIC FUNCTION AMPERSAND OPAR parameter_declaration_list CPAR return_type compund_statement
                                        |   FUNCTION OPAR CPAR compound_statement
                                        |   FUNCTION OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   FUNCTION AMPERSAND OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   STATIC FUNCTION OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   STATIC FUNCTION OPAR CPAR return_type compound_statement
                                        |   STATIC FUNCTION AMPERSAND OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   STATIC FUNCTION AMPERSAND OPAR CPAR return_type compound_statement
                                        '''

def p_object_creation_expression(p):
    '''object_creation_expression       :   NEW class_type_designator OPAR argument_expression_list
                                        |   NEW class_type_designator OPAR CPAR
                                        |   NEW class_type_designator OPAR argument_expression_list COMMA CPAR
                                        |   NEW class_type_designator
                                        |   NEW CLASS OPAR argument_expression_list CPAR class_base_clause class_interface_clause OBRA class_member_declaration CBRA
                                        |   NEW CLASS OPAR CPAR OBRA CBRA
                                        |   NEW CLASS OPAR argument_expression_list CPAR class_base_clause OBRA class_member_declaration CBRA
                                        |   NEW CLASS OPAR argument_expression_list CPAR class_interface_clause OBRA class_member_declaration CBRA
                                        |   NEW CLASS OPAR argument_expression_list CPAR class_base_clause OBRA CBRA
                                        |   NEW CLASS OPAR CPAR class_interface_clause OBRA CBRA
                                    '''

def p_class_type_designator(p):
    '''class_type_designator            :   qualified_name
                                        |   new_variable
    '''

def p_new_variable(p):
    '''new_variable                     :   simple_variable
                                        |   new_variable OBRACK expression CBRACK
                                        |   new_variable OBRACK CBRACK
                                        |   new_variable OBRA expression CBRA
                                        |   new_variable OBJECT_OPERATOR member_name
                                        |   qualified_name DOUBLE_COLON simple_variable
                                        |   relative_scope DOUBLE_COLON simple_variable
                                        |   new_variable DOUBLE_COLON simple_variable'''

def p_array_creation_expression(p):
    '''array_creation_expression        :   ARRAY OBRA array_initializer CBRA
                                        |   ARRAY OBRA CBRA
                                        |   OBRACK array_initializer CBRACK
                                        |   OBRACK CBRACK'''

def p_array_initilizer(p):
    '''array_initializer                :   array_initializer_list COMMA
                                        |   array_initializer_list'''

def p_array_initializer_list(p):
    '''array_initializer_list           :   array_element_initializer
                                        |   array_element_initializer COMMA array_initializer_list'''

def p_array_element_initializer(p):
    '''array_element_initializer        :   DOLLAR element_value
                                        |   element_value
                                        |   element_key DOUBLE_ARROW DOLLAR element_value
                                        |   element_key DOUBLE_ARROW element_value'''

def p_element_key(p):
    '''element_key                      :   expression'''

def p_element_value(p):
    '''element_value                    :   expression'''

def p_subscript_expression(p):
    '''subscript_expression             :   dereferencable_expression OBRACK expression CBRACK
                                        |   dereferencable_expression OBRACK CBRACK
                                        |   dereferencable_expression OBRA expression CBRA
                                        '''

def p_function_call_expression(p):
    '''function_call_expression         :   qualified_name OPAR argument_expression_list CPAR
                                        |   qualified_name OPAR CPAR
                                        |   qualified_name OPAR argument_expression_list COMMA CPAR
                                        |   callable_expression OPAR argument_expression_list CPAR
                                        |   callable_expression OPAR CPAR
                                        |   callable_expression OPAR argument_expression_list COMMA CPAR'''

def p_argument_expression_list(p):
    '''argument_expression_list         :   argument_expression
                                        |   argument_expression_list COMMA argument_expression'''

def p_argument_expression(p):
    '''argument_expression              :   variadic_unpacking
                                        |   expression'''

def p_variadic_unpacking(p):
    '''variadic_unpacking               :   ELLIPSIS expression'''

def p_member_access_expression(p):
    '''member_access_expression         :   dereferencable_expression OBJECT_OPERATOR member_name'''

def p_member_name(p):
    '''member_name                      :   STRING
                                        |   simple_variable
                                        |   OBRA expression CBRA'''

def p_member_call_expresion(p):
    '''member_call_expression           :   dereferencable_expression OBJECT_OPERATOR member_name OPAR argument_expression_list CPAR
                                        |   dereferencable_expression OBJECT_OPERATOR member_name OPAR CPAR
                                        |   dereferencable_expression OBJECT_OPERATOR member_name OPAR argument_expression_list COMMA CPAR'''

def p_postfix_increment_expression(p):
    '''postfix_increment_expression     :   variable INC'''

def p_postfix_decrement_expression(p):
    '''postfix_increment_expression     :   variable DEC'''

def p_prefix_increment_expression(p):
    '''prefix_increment_expression      :    INC variable '''

def p_prefix_decrement_expression(p):
    '''prefix_decrement_expression      :    DEC variable'''

def p_shell_command_expression(p):
    '''shell_command_expression         :   BACKQUOTE TEXT BACKQUOTE'''

def p_scoped_property_access_expression(p):
    '''scoped_property_access_expression :   scope_resolution_qualifier DOUBLE_COLON simple_variable'''

def p_scoped_call_expression(p):
    '''scoped_call_expression           :   scope_resolution_qualifier DOUBLE_COLON member_name OPAR argument_expression_list CPAR
                                        |   scope_resolution_qualifier DOUBLE_COLON member_name OPAR CPAR
                                        |   scope_resolution_qualifier DOUBLE_COLON member_name OPAR argument_expression_list COMMA CPAR'''

def p_class_constant_access_expression(p):
    '''class_constant_access_expression :   scope_resolution_qualifier DOUBLE_COLON STRING'''

def p_scope_resolution_qualifier(p):
    '''scope_resolution_qualifier       :   relative_scope
                                        |   qualified_name
                                        |   dereferencable_expression'''

def p_relative_scope(p):
    '''relative_scope                   :   SELF
                                        |   PARENT
                                        |   STATIC'''

def p_clone_expresion(p):
    '''clone_expression                 :   primary_expression
                                        |   CLONE primary_expression'''

def p_exponentiation_expression(p):
    '''exponentiation_expression        :   clone_expression
                                        |   clone_expression POW exponentiation_expression'''

def p_unary_expression(p):
    '''unary_expression                 :   exponentiation_expression
                                        |   unary_op_expression
                                        |   error_control_expression
                                        |   cast_expression'''

def p_unary_op_expression(p):
    '''unary_op_expression              :   ADD
                                        |   SUB
                                        |   NEG'''

def p_error_control_expression(p):
    '''error_control_expression         :   AT unary_expression'''

def p_cast_expression(p):
    '''cast_expression                  :   OPAR cast_type CPAR unary_expression'''

def p_cast_type(p):
    '''cast_type                        :   ARRAY
                                        |   BINARY
                                        |   BOOL
                                        |   BOOLEAN
                                        |   DOUBLE
                                        |   INT
                                        |   INTEGER
                                        |   FLOAT
                                        |   OBJECT
                                        |   REAL 
                                        |   STRINGKW 
                                        |   UNSET'''

def p_instanceof_expression(p):
    '''instanceof_expression            :   unary_expression
                                        |   instanceof_subject INSTANCEOF class_type_designator'''
def p_instanceof_subject(p):
    '''instanceof_subject               :   instanceof_expression'''

def p_logical_not_expression(p):
    '''logical_not_expression           :   instanceof_expression
                                        |   NOT instanceof_expression'''

def p_multiplicative_expression(p):
    '''multiplicative_expression        :   logical_not_expression
                                        |   multiplicative_expression MULT logical_not_expression
                                        |   multiplicative_expression DIV logical_not_expression
                                        |   multiplicative_expression MOD logical_not_expression
                                        '''

def p_additive_expression(p):
    '''additive_expression        :   multiplicative_expression
                                        |   additive_expression ADD multiplicative_expression
                                        |   additive_expression SUB multiplicative_expression
                                        |   additive_expression CONCAT multiplicative_expression
                                        '''

def p_shift_expression(p):
    '''shift_expression        :   additive_expression
                                        |   shift_expression SR additive_expression
                                        |   shift_expression SL additive_expression
                                        '''

def p_relational_expression(p):
    '''relational_expression        :   shift_expression
                                        |   relational_expression LT shift_expression
                                        |   relational_expression GT shift_expression
                                        |   relational_expression IS_SMALLER_OR_EQUAL shift_expression
                                        |   relational_expression IS_GREATER_OR_EQUAL shift_expression
                                        |   relational_expression SPACESHIP shift_expression
                                        '''

def p_equality_expression(p):
    '''equality_expression        :   relational_expression
                                        |   equality_expression IS_EQUAL relational_expression
                                        |   equality_expression IS_NOT_EQUAL relational_expression
                                        |   equality_expression IS_IDENTICAL relational_expression
                                        |   equality_expression IS_NOT_IDENTICAL relational_expression
                                        '''

def p_bitwise_AND_expression(p):
    '''bitwise_AND_expression        :   equality_expression
                                        |   bitwise_AND_expression AMPERSAND equality_expression
                                        '''

def p_bitwise_exc_OR_expression(p):
    '''bitwise_exc_OR_expression        :   bitwise_AND_expression
                                        |   bitwise_exc_OR_expression BITWISE_XOR bitwise_AND_expression
                                        '''

def p_bitwise_inc_OR_expression(p):
    '''bitwise_inc_OR_expression        :   bitwise_exc_OR_expression
                                        |   bitwise_inc_OR_expression BITWISE_OR bitwise_exc_OR_expression
                                        '''

def p_logical_AND_expression_1(p):
    '''logical_AND_expression_1         :   bitwise_inc_OR_expression
                                        |   logical_AND_expression_1 BOOLEAN_AND bitwise_inc_OR_expression
                                        '''

def p_logical_inc_OR_expression_1(p):
    '''logical_inc_OR_expression_1      :   logical_AND_expression_1
                                        |   logical_inc_OR_expression_1 BOOLEAN_OR logical_AND_expression_1
                                        '''

def p_coalesce_expression(p):
    '''coalesce_expression              :   logical_inc_OR_expression_1
                                        |   logical_inc_OR_expression_1 COALESCE coalesce_expression
                                        '''

def p_conditional_expression(p):
    '''conditional_expression           :   coalesce_expression
                                        |   conditional_expression CONDITIONAL expression COLON coalesce_expression
                                        |   conditional_expression CONDITIONAL COLON coalesce_expression
                                        '''

def p_assignment_expression(p):
    '''assignment_expression            :   conditional_expression
                                        |   simple_assignment_expression
                                        |   compound_assignment_expression
                                        '''

def p_simple_assignment_expression(p):
    '''simple_assignment_expression     :   variable ASSIGN assignment_expression
                                        |   list_intrinsic ASSIGN assignment_expression
                                        '''

def p_list_intrinsic(p):
    '''simple_assignment_expression     :   LIST OPAR list_expression_list CPAR
                                        '''

def p_list_expression_list(p):
    '''list_expression_list             :   unkeyed_list_expression_list
                                        |   keyed_list_expression_list COMMA
                                        |   keyed_list_expression_list 
                                        '''

def p_unkeyed_list_expression_list(p):
    '''unkeyed_list_expression_list     :   list_or_variable
                                        |   COMMA
                                        |   unkeyed_list_expression_list COMMA list_or_variable
                                        |   unkeyed_list_expression_list COMMA 
                                        '''

def p_keyed_list_expression_list(p):
    '''keyed_list_expression_list       :   expression DOUBLE_ARROW list_or_variable
                                        |   COMMA
                                        |   keyed_list_expression_list COMMA expression DOUBLE_ARROW list_or_variable
                                        '''

def p_list_or_variable(p):
    '''list_or_variable                 :   list_intrinsic
                                        |   variable
                                        |   DOLLAR variable
                                        '''

def p_byref_assignment_expression(p):
    '''byref_assignment_expression      :   variable ASSIGN AMPERSAND variable
                                        '''

def p_compound_assignment_expression(p):
    '''compount_assignment_expression   :   variable compund_assignment_operator assignment_expression
                                        '''

def p_compound_assignment_operator(p):
    '''compount_assignment_operator     :   POW_EQUAL
                                        |   MUL_EQUAL 
                                        |   DIV_EQUAL
                                        |   MOD_EQUAL
                                        |   PLUS_EQUAL
                                        |   MINUS_EQUAL
                                        |   SL_EQUAL
                                        |   SR_EQUAL
                                        |   AND_EQUAL
                                        |   XOR_EQUAL
                                        |   OR_EQUAL
                                        '''

def p_yield_from_expression(p):
    '''yield_from_expression            :   YIELD_FROM assigment_expression'''

def p_yield_expression(p):
    '''yield_expression                 :   YIELD
                                        |   yield_from_expression
                                        |   YIELD yield_expression
                                        |   YIELD yield_from_expression DOUBLE_ARROW yield_expression'''

def p_print_expression(p):
    '''print_expression                 :   yield_expression
                                        |   PRINT print_expression'''

def p_logical_AND_expression_2(p):
    '''logical_AND_expression_2         :   print_expression
                                        |   logical_AND_expression_2 LOGICAL_AND yield_expression
                                        '''

def p_logical_exc_OR_expression(p):
    '''logical_exc_OR_expression        :   logical_AND_expression_2
                                        |   logical_exc_OR_expression LOGICAL_XOR LOGICAL_AND_expression_2
                                        '''

def p_logical_inc_OR_expression_2(p):
    '''logical_inc_OR_expression_2      :   logical_exc_OR_expression
                                        |   logical_inc_OR_expression_2 LOGICAL_OR LOGICAL_exc_OR_expression_2
                                        '''

def p_expression(p):
    '''expression                       :   logical_inc_OR_expression_2
                                        |   include_expression
                                        |   include_once_expression
                                        |   require_expression
                                        |   require_once_expression
                                        '''

def p_include_expression(p):
    '''include_expression               :   INCLUDE expression
                                        '''

def p_include_once_expression(p):
    '''include_expression               :   INCLUDE_ONCE expression
                                        '''

def p_require_expression(p):
    '''require_expression               :   REQUIRE expression
                                        '''

def p_require_once_expression(p):
    '''require_expression               :   REQUIRE_ONCE expression
                                        '''

def p_constant_expression(p):
    '''constant_expression              :   expression'''

def p_statement(p):
    '''statement                        :   compound_statement
                                        |   named_label_statement
                                        |   expression_statement
                                        |   selection_statement
                                        |   iteration_statement
                                        |   jump_statement
                                        |   try_statement
                                        |   declare_statement
                                        |   echo_statement
                                        |   unset_statement
                                        |   const_declaration
                                        |   function_definition
                                        |   class_declaration
                                        |   interface_declaration
                                        |   trait_declaration
                                        |   namespace_definition
                                        |   global_declaration
                                        |   function_static_declaration
                                        '''

def p_compound_statement(p):
    '''compound_statement               :   OBRA statement_list CBRA
                                        |   OBRA CBRA'''

def p_statement_list(p): 
    '''statement_list                   :   statement
                                        |   statement_list statement'''

def p_named_label_statement(p): 
    '''named_label_statement            :   STRING COLON'''

def p_expression_statement(p): 
    '''expression_statement             :   expression ENDLINE
                                        |   ENDLINE'''

def p_selection_statement(p): 
    '''selection_statement              :   if_statement
                                        |   switch_statement'''

def p_if_statement(p):
    '''if_statement                     :   IF OPAR expression CPAR statement elseif_clauses_1 else_clause_1
                                        |   IF OPAR expression CPAR statement
                                        |   IF OPAR expression CPAR statement elseif_clauses_1
                                        |   IF OPAR expression CPAR statement else_clause_1
                                        |   IF OPAR expression CPAR COLON statement_list elseif_clauses_2 else_clause_2 ENDIF ENDLINE
                                        |   IF OPAR expression CPAR COLON statement_list else_clause_2 ENDIF ENDLINE
                                        |   IF OPAR expression CPAR COLON statement_list elseif_clauses_2 ENDIF ENDLINE
                                        '''

def p_elseif_clauses_1(p):
    '''elseif_clauses_1                 :   elseif_clause_1
                                        |   esleif_clauses_1 elseif_clause_1
                                        '''

def p_elseif_clause_1(p):
    '''elseif_clause_1                  :   ELSEIF OPAR expression CPAR statement
                                        '''

def p_else_clause_1(p):
    '''else_clause_1                    :   ELSE statement
                                        '''

def p_elseif_clauses_2(p):
    '''elseif_clauses_2                 :   elseif_clause_2
                                        |   esleif_clauses_2 elseif_clause_2
                                        '''

def p_elseif_clause_2(p):
    '''elseif_clause_2                  :   ELSEIF OPAR expression CPAR COLON statement_list
                                        '''

def p_else_clause_2(p):
    '''else_clause_2                    :   ELSE COLON statement_list
                                        '''

def p_switch_statement(p):
    '''switch_statement                 :   SWITCH OPAR expression CPAR OBAR case_statements CBAR
                                        |   SWITCH OPAR expression CPAR OBAR CBAR
                                        |   SWITCH OPAR expression CPAR COLON case_statements ENDSWITCH ENDLINE
                                        '''

def p_case_statements(p):
    '''case_statements                  :   case_statement case_statements
                                        |   case_statement
                                        |   default_statement case_statements
                                        |   default_statement 
                                        '''

def p_case_statement(p):
    '''case_statement                   :   CASE expression case_default_label_terminator statement_list
                                        |   CASE expression case_default_label_terminator
                                        '''

def p_default_statement(p):
    '''default_statement                :   DEFAULT case_default_label_terminator statement_list
                                        |   DEFAULT case_default_label_terminator
                                        '''

def p_case_default_label_terminator(p):
    '''case_default_label_terminator    :   ENDLINE
                                        |   COLON
                                        '''

def p_iteration_statement(p):
    '''iteration_statement              :   while_statement
                                        |   do_statement
                                        |   for_statement
                                        |   foreach_statement
                                        '''

def p_while_statement(p):
    '''while_statement                  :   WHILE OPAR expression CPAR statement
                                        |   WHILE OPAR expression CPAR COLON statement_list ENDWHILE ENDLINE'''

def p_do_statement(p):
    '''do_statement                     :   DO statement WHILE OPAR expression CPAR ENDLINE'''

def p_for_statement(p):
    '''for_statement                    :   FOR OPAR for_initializer ENDLINE for_control ENDLINE for_end_of_loop CPAR statement  
                                        |   FOR OPAR ENDLINE for_control ENDLINE for_end_of_loop CPAR statement 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR statement 
                                        |   FOR OPAR ENDLINE ENDLINE CPAR statement 
                                        |   FOR OPAR ENDLINE for_control ENDLINE CPAR statement 
                                        |   FOR OPAR ENDLINE for_control ENDLINE for_end_of_loop CPAR statement 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR statement 
                                        |   FOR OPAR for_initializer ENDLINE ENDLINE CPAR statement 
                                        |   FOR OPAR for_initializer ENDLINE for_control ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE for_control ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE ENDLINE CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE for_control ENDLINE CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE for_control ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR for_initializer ENDLINE ENDLINE CPAR COLON statement_list ENDFOR ENDLINE 
                                        '''

def p_for_initializer(p):
    '''for_initializer                  :   for_expression_group
    '''
    
def p_for_control(p):
    '''for_control                      :   for_expression_group
    '''

def p_for_end_of_loop(p):
    '''for_end_of_loop                  :   for_expression_group
    '''
    
def p_for_expression_group(p):
    '''for_expression_group             :   expression
                                        |   for_expression_group COMMA expression
    '''

def p_foreach_statement(p):
    '''foreach_statement                :   FOREACH OPAR foreach_collection_name AS foreach_key foreach_value CPAR statement
                                        |   FOREACH OPAR foreach_collection_name AS foreach_key foreach_value CPAR COLON statement_list ENDFOREACH ENDLINE
                                        |   FOREACH OPAR foreach_collection_name AS foreach_value CPAR statement
                                        |   FOREACH OPAR foreach_collection_name AS foreach_key CPAR COLON statement_list ENDFOREACH ENDLINE
    '''
    
def p_foreach_collection_name(p):
    '''foreach_collection_name          :   expression
    '''
    
def p_foreach_key(p):
    '''foreach_key                      :   expression DOUBLE_ARROW
    '''

def p_foreach_value(p):
    '''foreach_value                    :   AMPERSAND expression
                                        |   expression
                                        |   list_intrinsic
    '''

def p_jump_statement(p):
    '''jump_statement                   :   goto_statement
                                        |   continue_statement
                                        |   break_statement
                                        |   return_statement
                                        |   throw_statement
    '''

def p_goto_statement(p):
    '''goto_statement                   : GOTO STRING ENDLINE
    '''

def p_continue_statement(p):
    '''continue_statement                   : CONTINUE ENDLINE
                                            | CONTINUE breakout_level ENDLINE
    '''
    
def p_breakout_level(p):
    '''breakout_level                       : integer_literal
                                            | OPAR breakout_level CPAR
    '''
    
def p_break_statement(p):
    '''break_statement                      : BREAK ENDLINE
                                            | BREAK breakout_level ENDLINE
    '''

def p_return_statement(p):
    '''return_statement                     : RETURN ENDLINE
                                            | RETURN expression ENDLINE
    '''

def p_throw_statement(p):
    '''throw_statement                     :  THROW expression ENDLINE
    '''
    
def p_try_statement(p):
    '''try_statement                    :   TRY compound_statement catch_clauses
                                        |   TRY compound_statement finally_clause
                                        |   TRY compound_statement catch_clauses finally_clause
    '''

def p_catch_clauses(p):
    '''catch_clauses                    :   catch_clause
                                        |   catch_clauses catch_clause
    '''

def p_catch_clause(p):
    '''catch_clause                     :   CATCH OPAR catch_name_list variable_name CPAR compound_statement
    '''

def p_catch_name_list(p):
    '''catch_name_list                  :   qualified_name
                                        |   catch_name_list BITWISE_OR qualified_name
    '''

def p_finally_clause(p):
    '''finally_clause                   :   FINALLY compound_statement
    '''
    
def p_declare_statement(p):
    '''declare_statement                :   DECLARE OPAR declare_directive CPAR statement
                                        |   DECLARE OPAR declare_directive CPAR COLON statement_list ENDDECLARE ENDLINE
                                        |   DECLARE OPAR declare_directive CPAR ENDLINE
    '''

def p_declare_directive(p):
    '''declare_directive                :   TICKS ASSIGN literal
                                        |   ENCODING ASSIGN literal
                                        |   STRICT_TYPES ASSIGN literal
    '''

def p_echo_statement(p):
    '''echo_statement                   :   ECHO expression_list ENDLINE
    '''

def p_expression_list(p):
    '''expression_list                  :   expression
                                        |   expression_list COMMA expression
    '''
    
def p_unset_statement(p):
    '''unset_statement                  :   UNSET OPAR variable_list CPAR ENDLINE
                                        |   UNSET OPAR variable_list COMMA CPAR ENDLINE
    '''

def p_function_definition(p):
    '''function_definition              :   function_definition_header compound_statement
    '''

def p_function_definition_header(p):
    '''function_definitio_header        :   FUNCTION AMPERSAND STRING OPAR parameter_declaration_list CPAR return_type
                                        |   FUNCTION STRING OPAR parameter_declaration_list CPAR return_type
                                        |   FUNCTION STRING OPAR parameter_declaration_list CPAR
                                        |   FUNCTION STRING OPAR CPAR return_type
                                        |   FUNCTION STRING OPAR CPAR
                                        |   FUNCTION AMPERSAND STRING OPAR CPAR return_type
                                        |   FUNCTION AMPERSAND STRING OPAR CPAR
                                        |   FUNCTION AMPERSAND STRING OPAR parameter_declaration_list CPAR
    '''

def p_parameter_declaration_list(p):
    '''parameter_declaration_list       :   simple_parameter_declaration_list
                                        |   variadic_parameter_declaration_list
    '''


def p_simple_parameter_declaration_list(p):
    '''simple_parameter_declaration_list :   parameter_declaration
                                        |   parameter_declaration_list COMMA parameter_declaration
    '''

def p_variadic_parameter_declaration_list(p):
    '''variadic_parameter_declaration_list :   simple_parameter_declaration_list COMMA variadic_parameter
                                        |   variadic_parameter
    '''

def p_parameter_declaration(p):
    '''parameter_declaration            :   type_declaration AMPERSAND VARIABLE default_argument_specifier
                                        |   AMPERSAND VARIABLE default_argument_specifier
                                        |   VARIABLE default_argument_specifier
                                        |   VARIABLE 
                                        |   AMPERSAND VARIABLE 
                                        |   type_declaration AMPERSAND VARIABLE 
                                        |   type_declaration VARIABLE 
                                        |   type_declaration VARIABLE default_argument_specifier 
    '''

def p_variadic_parameter(p):
    '''variadic_parameter               :   type_declaration AMPERSAND  ELLIPSIS VARIABLE
                                        |   type_declaration ELLIPSIS VARIABLE
                                        |   ELLIPSIS VARIABLE
                                        |   type_declaration VARIABLE
    '''

def p_return_type(p):
    '''return_type                      :   COLON type_declaration
                                        |   VOID
    '''

def p_type_declaration(p):
    '''type_declaration                 :   CONDITIONAL base_type_declaration 
                                        |   base_type_declaration
    '''

def p_base_type_declaration(p):
    '''base_type_declaration            :   ARRAY
                                        |   CALLABLE
                                        |   ITERABLE
                                        |   scalar_type
                                        |   qualified_name
    '''

def p_scalar_type(p):
    '''scalar_type                      :   BOOL
                                        |   FLOAT
                                        |   INT
                                        |   STRINGKW
    '''
    
def p_default_argument_specifier(p):
    '''default_argument_specifier       :   ASSIGN constant_expression
    '''

def p_class_declaration(p):
    '''class_declaration                :   class_modifier CLASS STRING class_base_clause class_interface_clause OBRA class_member_declaration CBRA
                                        |   class_modifier CLASS STRING class_base_clause class_interface_clause OBRACBRA
                                        |   class_modifier CLASS STRING class_base_clause OBRACBRA
                                        |   class_modifier CLASS STRING OBRACBRA
                                        |   CLASS STRING OBRACBRA
                                        |   class_modifier CLASS STRING class_base_clause OBRA class_member_declaration CBRA
                                        |   class_modifier CLASS STRING OBRA class_member_declaration CBRA
                                        |   CLASS STRING OBRA class_member_declaration CBRA
                                        |   class_modifier CLASS STRING class_interface_clause OBRA class_member_declaration CBRA
                                        |    CLASS STRING class_interface_clause OBRA class_member_declaration CBRA
    '''

def p_class_modifier(p):
    '''class_modifier                   :   ABSTRACT 
                                        |   FINAL'''

def p_class_base_clause(p):
    '''class_base_clause                :   EXTENDS qualified_name 
    '''

def p_class_interface_clause(p):
    '''class_interface_clause           :   IMPLEMENTS qualified_name
                                        |   class_interface_clause COMMA qualified_name
    '''

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
