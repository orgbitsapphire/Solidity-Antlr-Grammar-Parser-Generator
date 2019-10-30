grammar Solidity;

parts
: (pragmaPart | contractPart | libraryPart | importPart)* EOF;

// PRAGMA

pragmaPart
: 'pragma' pragmaIdentifier pragmaVersionOperator? pragmaVersionNumber ';';

pragmaIdentifier
: StringIdentifier;

pragmaVersionOperator
: '^' | '~' | '>=' | '>' | '<' | '<=' | '=' ;

pragmaVersionNumber
: PragmaVersion;

PragmaVersion
: [0-9]+ '.' [0-9]+ '.' [0-9]+ ;


// IMPORT 

importPart
: 'import' importOption ';';

importOption
: QuotedSentence importAs
| '{' StringIdentifier importAs ( ',' StringIdentifier importAs )* '}' 'from' QuotedSentence
| (StringIdentifier | '*') importAs 'from' QuotedSentence;

importAs
: ('as' StringIdentifier)?;

// LIBRARY

libraryPart
: 'library' libraryIdentifier '{' libraryCodeBlock '}';

libraryCodeBlock
: (statement)*;

libraryIdentifier
: StringIdentifier;

// CONTRACT

contractPart
: 'contract' contractIdentifier contractIs? '{' contractCodeBlock '}';

contractIs
: 'is' contractIsIdentifier (',' contractIsIdentifier)*;

contractIsIdentifier
: StringIdentifier;

contractIdentifier
: StringIdentifier;

contractCodeBlock
: (usingPart | constructorPart | functionPart | functionModifierPart | enumPart | eventPart | structPart | variablePart | mappingPart)*;

// USING 

usingPart
: 'using' usingLibrary 'for' forType ';';

usingLibrary
: StringIdentifier;

forType
: (stateVariableType | '*');

constructorPart
: 'constructor(' functionParams (');' | ')') functionType? functionRestriction? functionPayable? functionConstant? functionReturns? functionBody? (';')?;

variablePart
: stateVariable ';';

// MAPPING

mappingPart
: mapping stateVariableKeyword? stateVariableIdentifier ';';

mapping
: 'mapping' '(' mappingFrom '=>' mappingTo ')';

mappingFrom
: stateVariableType;

mappingTo
: stateVariableType | mapping;

// STRUCT

structPart
: 'struct' structIdentifier '{' structParams '}';

structIdentifier
: StringIdentifier;

structParams
: (stateVariable ';')*;

// EVENT

eventPart
: 'event' eventIdentifier '(' eventParams ');';

eventIdentifier
: StringIdentifier;

eventParams
: (stateVariable)*;

// FUNCTION

functionModifierPart 
: 'modifier' functionIdentifier '(' functionParams (');' | ')') functionBody? (';')?;

functionPart
: 'function' functionIdentifier '(' functionParams (');' | ')') functionType? functionRestriction? functionPayable? functionConstant? functionReturns? functionBody? (';')?;

functionBody
: '{' (statement)* '}';

statement
: ifStatement | forStatement | whileStatement | doWhileStatement | continueStatement | breakStatement | throwStatement | emitStatement | functionStatement | functionReturnStatement | errorHandlerStatement | otherStatement;

errorHandlerStatement
: errorHandlerIdentifier token;

errorHandlerIdentifier
: 'assert' | 'require' | 'revert';

otherStatement
: token ';';

functionReturnStatement
: 'return' statement;

functionIdentifier
: StringIdentifier;

functionParams
: stateVariable? ( ',' stateVariable )* ;

functionType
: ('external' | 'public' | 'internal' | 'private');

functionPayable
: 'payable';

functionConstant
: 'constant';

functionRestriction
: ('view' | 'pure');

functionReturns
: 'returns' '(' stateVariableType stateVariableIdentifier? ')';

// EMIT 

emitStatement
: 'emit' emitIdentifier statement; 

emitIdentifier
: StringIdentifier;

// ENUM

enumPart
: 'enum' enumIdentifier '{' enumValues '}';

enumIdentifier
: StringIdentifier;

enumValues
: (enumValue)*;

enumValue
: token;

// CONTROL FLOW

functionStatement
: functionStatementIdentifier '(' token? (',' token)* ');';

functionStatementIdentifier
: token;

ifStatement
: 'if' '(' ifCondition ')' ifStatementBody elseIfStatement? elseStatement?;

ifStatementBody
: ('{')? (statement)* ('}')?;

ifCondition
: token;

elseIfStatement
: 'else if' '(' ifCondition ')' ifStatementBody;

elseStatement
: 'else' ifStatementBody;

forStatement
: 'for' '(' token? ';' token? ';' token? ')' forStatementBody ;

forStatementBody
: ('{')? (statement)* ('}')?;

whileStatement
: 'while' '(' token ')' whileStatementBody;

whileStatementBody
: ('{')? (statement)* ('}')?;

doWhileStatement
: 'do' doWhileStatementBody 'while' '(' token ')' ';';

doWhileStatementBody
: ('{')? (statement)* ('}')?;

continueStatement
 : 'continue' ';';

breakStatement
 : 'break' ';';

throwStatement
 : 'throw' ';';

// COMMON

etherUnit
: 'ether' | 'finney' | 'szabo' | 'wei';

timeUnit
: 'seconds' | 'minutes' | 'hours' | 'days' | 'weeks';

token
: StringIdentifier
| QuotedSentence
| NumberIdentifier (etherUnit | timeUnit)?
| token '(' (token? (',' token)*) ')'
| '(' ( token? ( ',' token? )* ) ')'
| '[' ( token ( ',' token )* )? ']'
| '(' token ')'
| token ('++' | '--' | ('[' token ']') | ('.' StringIdentifier) | ':')
| ('++' | '--' | '!' | '+' | '-' | '~' | 'after' | 'delete') token
| token ('|' | '&' | '&&' | '^'| '||' | '==' | '!=' | '=' | '|=' | '^=' | '&=' | '<<' | '>>' | '<<=' | '>>=' | '+=' | '-=' | '*=' | '/=' | '%=' | '**' | '*' | '/' | '%' | '+' | '-' | '<' | '>' | '<=' | '>=') token
| token '?' token ':' token
| stateVariable
| 'new' stateVariableType;

stateVariable
: stateVariableType stateVariableKeyword? stateVariableIdentifier ('[' ']')?;

stateVariableKeyword
: ('indexed' | 'public' | 'private');

stateVariableType
: ('address' | 'bool' | 'string' | 'var' | 'fixed' | 'ufixed'
| 'bytes1' | 'bytes2' | 'bytes3' | 'bytes4' | 'bytes5' | 'bytes6' | 'bytes7' | 'bytes8' | 'bytes9' | 'bytes10' | 'bytes11' | 'bytes12' | 'bytes13' | 'bytes14' | 'bytes15' | 'bytes16' | 'bytes17' | 'bytes18' | 'bytes19' | 'bytes20'
| 'bytes21' | 'bytes22' | 'bytes23' | 'bytes24' | 'bytes25' | 'bytes26' | 'bytes27' | 'bytes28' | 'bytes29' | 'bytes30' | 'bytes31' | 'bytes32' 
| 'uint' | 'uint8' | 'uint16' | 'uint24' | 'uint32' | 'uint40' | 'uint48' | 'uint56' | 'uint64' | 'uint72' | 'uint80' | 'uint88' | 'uint96' | 'uint104' | 'uint112' | 'uint120' | 'uint128' | 'uint136' | 'uint144' | 'uint152' | 'uint160'
| 'uint168' | 'uint176' | 'uint184' | 'uint192' | 'uint200' | 'uint208' | 'uint216' | 'uint224' | 'uint232' | 'uint240' | 'uint248' | 'uint256'
| 'int' | 'int8' | 'int16' | 'int24' | 'int32' | 'int40' | 'int48' | 'int56' | 'int64' | 'int72' | 'int80' | 'int88' | 'int96' | 'int104' | 'int112' | 'int120' | 'int128' | 'int136' | 'int144' | 'int152' | 'int160'
| 'int168' | 'int176' | 'int184' | 'int192' | 'int200' | 'int208' | 'int216' | 'int224' | 'int232' | 'int240' | 'int248' | 'int256');

stateVariableIdentifier
: StringIdentifier;

StringIdentifier
: [a-zA-Z_$] [a-zA-Z0-9_$]*;

QuotedSentence
: '"' (~["\r\n\\] | ('\\' .))* '"' | '\'' (~['\r\n\\] | ('\\' .))* '\'' ;

NumberIdentifier
: [0-9] ( '_'? [0-9] )*;

WS
: [ \t\r\n]+ -> channel(HIDDEN);

COMMENT
: '/*' .*? '*/' -> skip;

LINE_COMMENT
: '//' ~[\r\n]* -> skip;
