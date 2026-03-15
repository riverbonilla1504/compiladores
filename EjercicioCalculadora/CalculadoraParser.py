# Generated from Calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,1,3,1,3,1,3,1,3,3,3,33,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,1,2,
        1,0,3,4,33,0,8,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,6,32,1,0,0,0,8,
        9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,16,3,4,2,0,12,13,7,0,0,0,
        13,15,3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,
        0,0,0,17,3,1,0,0,0,18,16,1,0,0,0,19,24,3,6,3,0,20,21,7,1,0,0,21,
        23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,5,1,0,0,0,26,24,1,0,0,0,27,28,5,5,0,0,28,29,3,2,1,0,29,30,5,
        6,0,0,30,33,1,0,0,0,31,33,5,7,0,0,32,27,1,0,0,0,32,31,1,0,0,0,33,
        7,1,0,0,0,3,16,24,32
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_termino = 2
    RULE_factor = 3

    ruleNames =  [ "prog", "expresion", "termino", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expresion()
            self.state = 9
            self.match(CalculadoraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.TerminoContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.TerminoContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.termino()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.termino()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.FactorContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.FactorContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = CalculadoraParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.factor()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.factor()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = CalculadoraParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(CalculadoraParser.T__4)
                self.state = 28
                self.expresion()
                self.state = 29
                self.match(CalculadoraParser.T__5)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(CalculadoraParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





