grammar Calculadora;

prog: expresion EOF ;

expresion : termino (('+'|'-') termino)* ;

termino : factor (('*'|'/') factor)* ;

factor : '(' expresion ')'
       | NUMBER
       ;

NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;
