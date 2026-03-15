grammar Expr2;

expr: sumExpr ('*' sumExpr)* ;

sumExpr: atom ('+' atom)* ;

atom: NUM ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
