import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import Tree
from SolidityLexer import SolidityLexer
from SolidityParser import SolidityParser
from SolidityListener import SolidityListener

class SolidityPrintListener(SolidityListener):
    def enterFunctionPart(self, ctx):
        print(ctx.getText())

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SolidityLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SolidityParser(stream)
    tree = parser.parts()
    #printer = SolidityPrintListener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)
    print(Trees.toStringTree(tree, None, parser).replace("(","\n(").replace(")",")   "))
if __name__ == '__main__':
    main(sys.argv)
