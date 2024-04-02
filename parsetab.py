
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DOCTYPE HTML_CONTENT HTML_TAG PHP_CODEstart : PHP_CODE\n    start : HTML_TAG\n          | HTML_CONTENT\n          | DOCTYPE\n    '
    
_lr_action_items = {'PHP_CODE':([0,],[2,]),'HTML_TAG':([0,],[3,]),'HTML_CONTENT':([0,],[4,]),'DOCTYPE':([0,],[5,]),'$end':([1,2,3,4,5,],[0,-1,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> PHP_CODE','start',1,'p_php_code','main.py',47),
  ('start -> HTML_TAG','start',1,'p_html_code','main.py',52),
  ('start -> HTML_CONTENT','start',1,'p_html_code','main.py',53),
  ('start -> DOCTYPE','start',1,'p_html_code','main.py',54),
]
