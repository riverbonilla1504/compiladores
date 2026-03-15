# Generated from Print.g4 by ANTLR 4.13.2
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
        4,1,5,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,5,1,13,
        8,1,10,1,12,1,16,9,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,3,4,17,0,6,
        1,0,0,0,2,9,1,0,0,0,4,17,1,0,0,0,6,7,5,1,0,0,7,8,3,2,1,0,8,1,1,0,
        0,0,9,14,3,4,2,0,10,11,5,2,0,0,11,13,3,4,2,0,12,10,1,0,0,0,13,16,
        1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,3,1,0,0,0,16,14,1,0,0,0,17,
        18,7,0,0,0,18,5,1,0,0,0,1,14
    ]

class PrintParser ( Parser ):

    grammarFileName = "Print.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "WS" ]

    RULE_stat = 0
    RULE_expr = 1
    RULE_atom = 2

    ruleNames =  [ "stat", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    NUM=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PrintParser.ExprContext,0)


        def getRuleIndex(self):
            return PrintParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = PrintParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(PrintParser.T__0)
            self.state = 7
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrintParser.AtomContext)
            else:
                return self.getTypedRuleContext(PrintParser.AtomContext,i)


        def getRuleIndex(self):
            return PrintParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PrintParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.atom()
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 10
                self.match(PrintParser.T__1)
                self.state = 11
                self.atom()
                self.state = 16
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

        def ID(self):
            return self.getToken(PrintParser.ID, 0)

        def NUM(self):
            return self.getToken(PrintParser.NUM, 0)

        def getRuleIndex(self):
            return PrintParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PrintParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





