from re import VERBOSE
import ply.yacc as yacc
from php_lexer import tokens
import php_lexer
import sys

VERBOSE = 1
has_errors = False

def p_script(p):
    '''script                           :   script_section
                                        |   script script_section'''

def p_string_literal(p):
    '''string_literal                   :   CONSTANT_ENCAPSED_STRING
                                        |   HEREDOC'''

def p_namespace_name(p):
    '''namespace_name                   :   STRING
                                        |   namespace_name NS_SEPARATOR STRING'''

def p_namespace_name_as_a_prefix(p):
    '''namespace_name_as_a_prefix       :   NS_SEPARATOR
                                        |   NS_SEPARATOR namespace_name NS_SEPARATOR
                                        |   namespace_name NS_SEPARATOR
                                        |   NAMESPACE NS_SEPARATOR
                                        |   NAMESPACE NS_SEPARATOR namespace_name NS_SEPARATOR
                                        '''

def p_qualified_name(p):
    '''qualified_name                   :   namespace_name_as_a_prefix STRING
                                        |   STRING'''

def p_integer_literal(p):
    '''integer_literal                  :   LNUMBER'''

def p_floating_literal(p):
    '''floating_literal                 :   DNUMBER'''

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
                                        |   OPAR expression CPAR'''

def p_simple_variable(p):
    '''simple_variable                  :   VARIABLE
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
                                        |   EXIT OPAR CPAR
                                        |   DIE
                                        |   DIE OPAR expression CPAR
                                        |   DIE OPAR CPAR'''
def p_isset_intrinsic(p):
    '''isset_intrinsic                  :   ISSET OPAR variable_list CPAR'''

def p_variable_list(p):
    '''variable_list                    :   variable
                                        |   variable_list COMMA variable'''

def p_anonymous_function_creation_expression(p):
    '''anonymous_function_creation_expression :   STATIC FUNCTION AMPERSAND OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   FUNCTION OPAR CPAR compound_statement
                                        |   FUNCTION OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   FUNCTION AMPERSAND OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   STATIC FUNCTION OPAR parameter_declaration_list CPAR return_type compound_statement
                                        |   STATIC FUNCTION OPAR CPAR return_type compound_statement
                                        |   STATIC FUNCTION AMPERSAND OPAR CPAR return_type compound_statement
                                        '''

def p_object_creation_expression(p):
    '''object_creation_expression       :   NEW class_type_designator OPAR argument_expression_list CPAR
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
    '''array_creation_expression        :   ARRAY OPAR array_initializer CPAR
                                        |   ARRAY OPAR CPAR
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
    '''postfix_decrement_expression     :   variable DEC'''

def p_prefix_increment_expression(p):
    '''prefix_increment_expression      :    INC variable '''

def p_prefix_decrement_expression(p):
    '''prefix_decrement_expression      :    DEC variable'''

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
                                        |   instanceof_subject INSTANCE_OF class_type_designator'''
def p_instanceof_subject(p):
    '''instanceof_subject               :   instanceof_expression'''

def p_logical_not_expression(p):
    '''logical_not_expression           :   instanceof_expression
                                        |   NOT instanceof_expression'''

def p_multiplicative_expression(p):
    '''multiplicative_expression        :   logical_not_expression
                                        |   multiplicative_expression MUL logical_not_expression
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
    '''list_intrinsic                   :   LIST OPAR list_expression_list CPAR
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
    '''compound_assignment_expression   :   variable compound_assignment_operator assignment_expression
                                        '''

def p_compound_assignment_operator(p):
    '''compound_assignment_operator     :   POW_EQUAL
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
                                        |   CONCAT_EQUAL
                                        '''

def p_yield_from_expression(p):
    '''yield_from_expression            :   YIELD_FROM assignment_expression'''

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
                                        |   logical_exc_OR_expression LOGICAL_XOR logical_AND_expression_2
                                        '''

def p_logical_inc_OR_expression_2(p):
    '''logical_inc_OR_expression_2      :   logical_exc_OR_expression
                                        |   logical_inc_OR_expression_2 LOGICAL_OR logical_exc_OR_expression
                                        '''

def p_expression(p):
    '''expression                       :   logical_inc_OR_expression_2
                                        |   include_expression
                                        |   include_once_expression
                                        |   require_expression
                                        |   require_once_expression
                                        |   assignment_expression
                                        '''

def p_include_expression(p):
    '''include_expression               :   INCLUDE expression
                                        '''

def p_include_once_expression(p):
    '''include_once_expression          :   INCLUDE_ONCE expression
                                        '''

def p_require_expression(p):
    '''require_expression               :   REQUIRE expression
                                        '''

def p_require_once_expression(p):
    '''require_once_expression          :   REQUIRE_ONCE expression
                                        '''

def p_constant_expression(p):
    '''constant_expression              :   expression
                                        |   string_literal
                                        |   integer_literal
                                        |   floating_literal'''

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
                                        |   namespace_use_declaration
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
                                        |   elseif_clauses_1 elseif_clause_1
                                        '''

def p_elseif_clause_1(p):
    '''elseif_clause_1                  :   ELSEIF OPAR expression CPAR statement
                                        '''

def p_else_clause_1(p):
    '''else_clause_1                    :   ELSE statement
                                        '''

def p_elseif_clauses_2(p):
    '''elseif_clauses_2                 :   elseif_clause_2
                                        |   elseif_clauses_2 elseif_clause_2
                                        '''

def p_elseif_clause_2(p):
    '''elseif_clause_2                  :   ELSEIF OPAR expression CPAR COLON statement_list
                                        '''

def p_else_clause_2(p):
    '''else_clause_2                    :   ELSE COLON statement_list
                                        '''

def p_switch_statement(p):
    '''switch_statement                 :   SWITCH OPAR expression CPAR OBRA case_statements CBRA
                                        |   SWITCH OPAR expression CPAR OBRA CBRA
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
                                        |   FOR OPAR ENDLINE ENDLINE CPAR statement 
                                        |   FOR OPAR ENDLINE for_control ENDLINE CPAR statement 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR statement 
                                        |   FOR OPAR for_initializer ENDLINE ENDLINE CPAR statement 
                                        |   FOR OPAR for_initializer ENDLINE for_control ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE for_control ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE ENDLINE for_end_of_loop CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE ENDLINE CPAR COLON statement_list ENDFOR ENDLINE 
                                        |   FOR OPAR ENDLINE for_control ENDLINE CPAR COLON statement_list ENDFOR ENDLINE 
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
    '''catch_clause                     :   CATCH OPAR catch_name_list VARIABLE CPAR compound_statement
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
    '''function_definition_header       :   FUNCTION AMPERSAND STRING OPAR parameter_declaration_list CPAR return_type
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
                                        |   parameter_declaration
                                        |   parameter_declaration_list COMMA parameter_declaration
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
    '''class_declaration                :   class_modifier CLASS STRING class_base_clause class_interface_clause OBRA class_member_declarations CBRA
                                        |   class_modifier CLASS STRING class_base_clause class_interface_clause OBRA CBRA
                                        |   class_modifier CLASS STRING class_base_clause OBRA CBRA
                                        |   class_modifier CLASS STRING OBRA CBRA
                                        |   CLASS STRING OBRA CBRA
                                        |   class_modifier CLASS STRING class_base_clause OBRA class_member_declarations CBRA
                                        |   class_modifier CLASS STRING OBRA class_member_declarations CBRA
                                        |   CLASS STRING OBRA class_member_declarations CBRA
                                        |   class_modifier CLASS STRING class_interface_clause OBRA class_member_declarations CBRA
                                        |    CLASS STRING class_interface_clause OBRA class_member_declarations CBRA
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

def p_class_member_declarations(p):
    '''class_member_declarations        :   class_member_declaration
                                        |   class_member_declarations class_member_declaration
    '''

def p_class_member_declaration(p):
    '''class_member_declaration         :   class_const_declaration
                                        |   property_declaration
                                        |   method_declaration
                                        |   constructor_declaration
                                        |   destructor_declaration
                                        |   trait_use_clause
    '''

def p_const_declaration(p):
    '''const_declaration                :   CONST const_elements ENDLINE'''

def p_class_const_declaration(p):
    '''class_const_declaration          :   visibility_modifier CONST const_elements ENDLINE
                                        |   CONST const_elements ENDLINE
    '''

def p_const_elements(p):
    '''const_elements                   :   const_element
                                        |   const_elements COMMA const_element
    '''

def p_const_element(p):
    '''const_element                    :   STRING ASSIGN constant_expression
    '''

def p_property_declaration(p):
    '''property_declaration             :   property_modifier property_elements ENDLINE
    '''

def p_property_modifier(p):
    '''property_modifier                :   VAR
                                        |   visibility_modifier static_modifier
                                        |   static_modifier visibility_modifier 
                                        |   visibility_modifier 
                                        |   static_modifier 
    '''

def p_visibility_modifier(p):
    '''visibility_modifier              :   PUBLIC
                                        |   PROTECTED
                                        |   PRIVATE
    '''

def p_static_modifier(p):
    '''static_modifier                  :   STATIC
    '''

def p_property_elements(p):
    '''property_elements                :   property_element
                                        |   property_elements property_element
    '''

def p_property_element(p):
    '''property_element                 :   VARIABLE property_initializer ENDLINE
    '''

def p_property_initializer(p):
    '''property_initializer             :   ASSIGN constant_expression
    '''

def p_method_declaration(p):
    '''method_declaration               :   method_modifiers function_definition
                                        |   function_definition 
                                        |   method_modifiers function_definition_header ENDLINE
    '''

def p_method_modifiers(p):
    '''method_modifiers                 :   method_modifier
                                        |   method_modifiers method_modifier 
    '''

def p_method_modifier(p):
    '''method_modifier                  :   visibility_modifier
                                        |   static_modifier
                                        |   class_modifier
    '''

def p_constructor_declaration(p):
    '''constructor_declaration          :   method_modifiers FUNCTION AMPERSAND CONSTRUCT OPAR parameter_declaration_list CPAR compound_statement
                                        |   method_modifiers FUNCTION CONSTRUCT OPAR parameter_declaration_list CPAR compound_statement                                        
                                        |   method_modifiers FUNCTION AMPERSAND CONSTRUCT OPAR CPAR compound_statement                                        
                                        |   method_modifiers FUNCTION CONSTRUCT OPAR CPAR compound_statement                                        
    '''

def p_destructor_declaration(p):
    '''destructor_declaration           :   method_modifiers FUNCTION AMPERSAND DESTRUCT OPAR CPAR compound_statement
                                        |   method_modifiers FUNCTION CONSTRUCT OPAR CPAR compound_statement 
    '''

def p_interface_declaration(p):
    '''interface_declaration            :   INTERFACE STRING interface_base_clause OBRA interface_member_declarations CBRA
                                        |   INTERFACE STRING OBRA interface_member_declarations CBRA
                                        |   INTERFACE STRING interface_base_clause OBRA CBRA
                                        |   INTERFACE STRING OBRA CBRA
    '''

def p_interface_base_clause(p):
    '''interface_base_clause            :   EXTENDS qualified_name
                                        |   interface_base_clause COMMA qualified_name
    '''

def p_interface_member_declarations(p):
    '''interface_member_declarations    :   interface_member_declaration
                                        |   interface_member_declarations interface_member_declaration
    '''

def p_interface_member_declaration(p):
    '''interface_member_declaration     :   class_const_declaration
                                        |   method_declaration
    '''

def p_trait_declaration(p):
    '''trait_declaration                :   TRAIT STRING OBRA CBRA
                                        |   TRAIT STRING OBRA trait_member_declarations CBRA
    '''
    
def p_trait_member_declarations(p):
    '''trait_member_declarations        :   trait_member_declaration
                                        |   trait_member_declarations trait_member_declaration
    '''
    
def p_trait_member_declaration(p):
    '''trait_member_declaration         :   property_declaration
                                        |   method_declaration
                                        |   constructor_declaration
                                        |   destructor_declaration
                                        |   trait_use_clauses
    '''
    
def p_trait_use_clauses(p):
    '''trait_use_clauses                :   trait_use_clause
                                        |   trait_use_clauses trait_use_clause
    '''
    
def p_trait_use_clause(p):
    '''trait_use_clause                 :   USE trait_name_list trait_use_specification
    '''

def p_trait_name_list(p):
    '''trait_name_list                  :   qualified_name
                                        |   trait_name_list COMMA qualified_name
    '''    

def p_trait_use_specification(p):
    '''trait_use_specification          :   COMMA
                                        |   OBRA CBRA
                                        |   OBRA trait_select_and_alias_clauses CBRA
    '''
    
def p_trait_select_and_alias_clauses(p):
    '''trait_select_and_alias_clauses   :   trait_select_and_alias_clause
                                        |   trait_select_and_alias_clauses trait_select_and_alias_clause
    '''

def p_trait_select_and_alias_clause(p):
    '''trait_select_and_alias_clause    :   trait_select_insteadof_clause ENDLINE
                                        |   trait_alias_as_clause ENDLINE
    '''        

def p_trait_select_insteadof_clause(p):
    '''trait_select_insteadof_clause    :   qualified_name DOUBLE_COLON STRING INSTEADOF trait_name_list
    '''
    
def p_trait_alias_as_clause(p):
    '''trait_alias_as_clause            :   STRING AS STRING
                                        |   STRING AS visibility_modifier STRING
                                        |   STRING AS visibility_modifier
    '''

def p_namespace_definition(p):
    '''namespace_definition             :   NAMESPACE namespace_name ENDLINE
                                        |   NAMESPACE namespace_name compound_statement
                                        |   NAMESPACE compound_statement
    '''
    
def p_namespace_use_declaration(p):
    '''namespace_use_declaration        :   USE namespace_function_or_const namespace_use_clauses ENDLINE
                                        |   USE namespace_use_clauses ENDLINE
                                        |   USE namespace_function_or_const NS_SEPARATOR namespace_name NS_SEPARATOR OBRA namespace_use_group_clauses_1 CBRA ENDLINE
                                        |   USE namespace_function_or_const namespace_name NS_SEPARATOR OBRA namespace_use_group_clauses_1 CBRA ENDLINE
                                        |   USE NS_SEPARATOR NAMESPACE_NAME NS_SEPARATOR OBRA namespace_use_group_clauses_2 CBRA ENDLINE
                                        |   USE NAMESPACE_NAME NS_SEPARATOR OBRA namespace_use_group_clauses_2 CBRA ENDLINE
    '''

def p_namespace_use_clauses(p):
    '''namespace_use_clauses            :   namespace_use_clause
                                        |   namespace_use_clauses COMMA namespace_use_clause
    '''

def p_namespace_use_clause(p):
    '''namespace_use_clause             :   qualified_name namespace_aliasing_clause
                                        |   qualified_name
    '''
    
def p_namespace_aliasing_clause(p):
    '''namespace_aliasing_clause        :   AS STRING
    '''
    
def p_namespace_function_or_const(p):
    '''namespace_function_or_const      :   FUNCTION
                                        |   CONST
    '''
    
def p_namespace_use_group_clauses_1(p):
    '''namespace_use_group_clauses_1    :   namespace_use_group_clause_1
                                        |   namespace_use_group_clauses_1 COMMA namespace_use_group_clause_1
    '''

def p_namespace_use_group_clause_1(p):
    '''namespace_use_group_clause_1     :   namespace_name namespace_aliasing_clause
                                        |   namespace_name
    '''
    
def p_namespace_use_group_clauses_2(p):
    '''namespace_use_group_clauses_2    :   namespace_use_group_clause_2
                                        |   namespace_use_group_clauses_2 COMMA namespace_use_group_clause_2
    '''
    
def p_namespace_use_group_clause_2(p):
    '''namespace_use_group_clause_2     :   namespace_function_or_const namespace_name namespace_aliasing_clause
                                        |   namespace_function_or_const namespace_name
                                        |   namespace_name namespace_aliasing_clause
    '''

def p_error(p):
    global has_errors
    has_errors = True
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO, NO SE ESPERABA EL TOKEN " + str(p.value))
        else:
            print("ERROR SINTACTICO")
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
    parser.parse(data, debug = True)
    if not has_errors:
        print("Amigazo, que chimba de parser. Completamente parsero")
    else:
        print("Amiguito, muy poco parsero. Solucione")
