grammar Print;

stat: 'print' expr ;

expr: atom ('+' atom)* ;

atom: ID
    | NUM
    ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
