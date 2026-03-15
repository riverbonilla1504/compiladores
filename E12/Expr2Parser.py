# Generated from Expr2.g4 by ANTLR 4.13.2
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
        4,1,4,25,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,0,0,
        3,0,2,4,0,0,23,0,6,1,0,0,0,2,14,1,0,0,0,4,22,1,0,0,0,6,11,3,2,1,
        0,7,8,5,1,0,0,8,10,3,2,1,0,9,7,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,19,3,4,2,0,15,16,5,
        2,0,0,16,18,3,4,2,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,
        20,1,0,0,0,20,3,1,0,0,0,21,19,1,0,0,0,22,23,5,3,0,0,23,5,1,0,0,0,
        2,11,19
    ]

class Expr2Parser ( Parser ):

    grammarFileName = "Expr2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_expr = 0
    RULE_sumExpr = 1
    RULE_atom = 2

    ruleNames =  [ "expr", "sumExpr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUM=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sumExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr2Parser.SumExprContext)
            else:
                return self.getTypedRuleContext(Expr2Parser.SumExprContext,i)


        def getRuleIndex(self):
            return Expr2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Expr2Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.sumExpr()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 7
                self.match(Expr2Parser.T__0)
                self.state = 8
                self.sumExpr()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr2Parser.AtomContext)
            else:
                return self.getTypedRuleContext(Expr2Parser.AtomContext,i)


        def getRuleIndex(self):
            return Expr2Parser.RULE_sumExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumExpr" ):
                listener.enterSumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumExpr" ):
                listener.exitSumExpr(self)




    def sumExpr(self):

        localctx = Expr2Parser.SumExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sumExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.atom()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 15
                self.match(Expr2Parser.T__1)
                self.state = 16
                self.atom()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(Expr2Parser.NUM, 0)

        def getRuleIndex(self):
            return Expr2Parser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = Expr2Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(Expr2Parser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





