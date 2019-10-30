# Antlr4 Solidity Parser Generator Grammar

## Creating Lexical Analyzer and Parser

### Antlr4 Parser Generator in Java
```antlr4 Solidity.g4```

```javac Solidity*.java```

### Antlr4 Parser Generator in Python
```antlr4 -Dlanguage=Python3 Solidity.g4```

## Parsing a Solidity smart contract using the antlr4 parser generator

### Python execution
```python3 parser.py test.sol```

### Java execution using GUI to visualize the AST (Abstract Syntax Tree)
```grun Solidity parts -gui```

```paste smart contract source code, press ENTER and then CTRL + D```
