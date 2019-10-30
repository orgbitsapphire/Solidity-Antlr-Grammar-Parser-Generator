# Generated from Solidity.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete listener for a parse tree produced by SolidityParser.
class SolidityListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityParser#parts.
    def enterParts(self, ctx:SolidityParser.PartsContext):
        pass

    # Exit a parse tree produced by SolidityParser#parts.
    def exitParts(self, ctx:SolidityParser.PartsContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaPart.
    def enterPragmaPart(self, ctx:SolidityParser.PragmaPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaPart.
    def exitPragmaPart(self, ctx:SolidityParser.PragmaPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaIdentifier.
    def enterPragmaIdentifier(self, ctx:SolidityParser.PragmaIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaIdentifier.
    def exitPragmaIdentifier(self, ctx:SolidityParser.PragmaIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaVersionOperator.
    def enterPragmaVersionOperator(self, ctx:SolidityParser.PragmaVersionOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaVersionOperator.
    def exitPragmaVersionOperator(self, ctx:SolidityParser.PragmaVersionOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaVersionNumber.
    def enterPragmaVersionNumber(self, ctx:SolidityParser.PragmaVersionNumberContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaVersionNumber.
    def exitPragmaVersionNumber(self, ctx:SolidityParser.PragmaVersionNumberContext):
        pass


    # Enter a parse tree produced by SolidityParser#importPart.
    def enterImportPart(self, ctx:SolidityParser.ImportPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#importPart.
    def exitImportPart(self, ctx:SolidityParser.ImportPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#importOption.
    def enterImportOption(self, ctx:SolidityParser.ImportOptionContext):
        pass

    # Exit a parse tree produced by SolidityParser#importOption.
    def exitImportOption(self, ctx:SolidityParser.ImportOptionContext):
        pass


    # Enter a parse tree produced by SolidityParser#importAs.
    def enterImportAs(self, ctx:SolidityParser.ImportAsContext):
        pass

    # Exit a parse tree produced by SolidityParser#importAs.
    def exitImportAs(self, ctx:SolidityParser.ImportAsContext):
        pass


    # Enter a parse tree produced by SolidityParser#libraryPart.
    def enterLibraryPart(self, ctx:SolidityParser.LibraryPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#libraryPart.
    def exitLibraryPart(self, ctx:SolidityParser.LibraryPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#libraryCodeBlock.
    def enterLibraryCodeBlock(self, ctx:SolidityParser.LibraryCodeBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#libraryCodeBlock.
    def exitLibraryCodeBlock(self, ctx:SolidityParser.LibraryCodeBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#libraryIdentifier.
    def enterLibraryIdentifier(self, ctx:SolidityParser.LibraryIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#libraryIdentifier.
    def exitLibraryIdentifier(self, ctx:SolidityParser.LibraryIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractPart.
    def enterContractPart(self, ctx:SolidityParser.ContractPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractPart.
    def exitContractPart(self, ctx:SolidityParser.ContractPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractIs.
    def enterContractIs(self, ctx:SolidityParser.ContractIsContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractIs.
    def exitContractIs(self, ctx:SolidityParser.ContractIsContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractIsIdentifier.
    def enterContractIsIdentifier(self, ctx:SolidityParser.ContractIsIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractIsIdentifier.
    def exitContractIsIdentifier(self, ctx:SolidityParser.ContractIsIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractIdentifier.
    def enterContractIdentifier(self, ctx:SolidityParser.ContractIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractIdentifier.
    def exitContractIdentifier(self, ctx:SolidityParser.ContractIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractCodeBlock.
    def enterContractCodeBlock(self, ctx:SolidityParser.ContractCodeBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractCodeBlock.
    def exitContractCodeBlock(self, ctx:SolidityParser.ContractCodeBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#usingPart.
    def enterUsingPart(self, ctx:SolidityParser.UsingPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#usingPart.
    def exitUsingPart(self, ctx:SolidityParser.UsingPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#usingLibrary.
    def enterUsingLibrary(self, ctx:SolidityParser.UsingLibraryContext):
        pass

    # Exit a parse tree produced by SolidityParser#usingLibrary.
    def exitUsingLibrary(self, ctx:SolidityParser.UsingLibraryContext):
        pass


    # Enter a parse tree produced by SolidityParser#forType.
    def enterForType(self, ctx:SolidityParser.ForTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#forType.
    def exitForType(self, ctx:SolidityParser.ForTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#constructorPart.
    def enterConstructorPart(self, ctx:SolidityParser.ConstructorPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#constructorPart.
    def exitConstructorPart(self, ctx:SolidityParser.ConstructorPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#variablePart.
    def enterVariablePart(self, ctx:SolidityParser.VariablePartContext):
        pass

    # Exit a parse tree produced by SolidityParser#variablePart.
    def exitVariablePart(self, ctx:SolidityParser.VariablePartContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingPart.
    def enterMappingPart(self, ctx:SolidityParser.MappingPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingPart.
    def exitMappingPart(self, ctx:SolidityParser.MappingPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#mapping.
    def enterMapping(self, ctx:SolidityParser.MappingContext):
        pass

    # Exit a parse tree produced by SolidityParser#mapping.
    def exitMapping(self, ctx:SolidityParser.MappingContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingFrom.
    def enterMappingFrom(self, ctx:SolidityParser.MappingFromContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingFrom.
    def exitMappingFrom(self, ctx:SolidityParser.MappingFromContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingTo.
    def enterMappingTo(self, ctx:SolidityParser.MappingToContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingTo.
    def exitMappingTo(self, ctx:SolidityParser.MappingToContext):
        pass


    # Enter a parse tree produced by SolidityParser#structPart.
    def enterStructPart(self, ctx:SolidityParser.StructPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#structPart.
    def exitStructPart(self, ctx:SolidityParser.StructPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#structIdentifier.
    def enterStructIdentifier(self, ctx:SolidityParser.StructIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#structIdentifier.
    def exitStructIdentifier(self, ctx:SolidityParser.StructIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#structParams.
    def enterStructParams(self, ctx:SolidityParser.StructParamsContext):
        pass

    # Exit a parse tree produced by SolidityParser#structParams.
    def exitStructParams(self, ctx:SolidityParser.StructParamsContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventPart.
    def enterEventPart(self, ctx:SolidityParser.EventPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventPart.
    def exitEventPart(self, ctx:SolidityParser.EventPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventIdentifier.
    def enterEventIdentifier(self, ctx:SolidityParser.EventIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventIdentifier.
    def exitEventIdentifier(self, ctx:SolidityParser.EventIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventParams.
    def enterEventParams(self, ctx:SolidityParser.EventParamsContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventParams.
    def exitEventParams(self, ctx:SolidityParser.EventParamsContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionModifierPart.
    def enterFunctionModifierPart(self, ctx:SolidityParser.FunctionModifierPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionModifierPart.
    def exitFunctionModifierPart(self, ctx:SolidityParser.FunctionModifierPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionPart.
    def enterFunctionPart(self, ctx:SolidityParser.FunctionPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionPart.
    def exitFunctionPart(self, ctx:SolidityParser.FunctionPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionBody.
    def enterFunctionBody(self, ctx:SolidityParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionBody.
    def exitFunctionBody(self, ctx:SolidityParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by SolidityParser#statement.
    def enterStatement(self, ctx:SolidityParser.StatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#statement.
    def exitStatement(self, ctx:SolidityParser.StatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#errorHandlerStatement.
    def enterErrorHandlerStatement(self, ctx:SolidityParser.ErrorHandlerStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#errorHandlerStatement.
    def exitErrorHandlerStatement(self, ctx:SolidityParser.ErrorHandlerStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#errorHandlerIdentifier.
    def enterErrorHandlerIdentifier(self, ctx:SolidityParser.ErrorHandlerIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#errorHandlerIdentifier.
    def exitErrorHandlerIdentifier(self, ctx:SolidityParser.ErrorHandlerIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#otherStatement.
    def enterOtherStatement(self, ctx:SolidityParser.OtherStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#otherStatement.
    def exitOtherStatement(self, ctx:SolidityParser.OtherStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionReturnStatement.
    def enterFunctionReturnStatement(self, ctx:SolidityParser.FunctionReturnStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionReturnStatement.
    def exitFunctionReturnStatement(self, ctx:SolidityParser.FunctionReturnStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:SolidityParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:SolidityParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionParams.
    def enterFunctionParams(self, ctx:SolidityParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionParams.
    def exitFunctionParams(self, ctx:SolidityParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionType.
    def enterFunctionType(self, ctx:SolidityParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionType.
    def exitFunctionType(self, ctx:SolidityParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionPayable.
    def enterFunctionPayable(self, ctx:SolidityParser.FunctionPayableContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionPayable.
    def exitFunctionPayable(self, ctx:SolidityParser.FunctionPayableContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionConstant.
    def enterFunctionConstant(self, ctx:SolidityParser.FunctionConstantContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionConstant.
    def exitFunctionConstant(self, ctx:SolidityParser.FunctionConstantContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionRestriction.
    def enterFunctionRestriction(self, ctx:SolidityParser.FunctionRestrictionContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionRestriction.
    def exitFunctionRestriction(self, ctx:SolidityParser.FunctionRestrictionContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionReturns.
    def enterFunctionReturns(self, ctx:SolidityParser.FunctionReturnsContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionReturns.
    def exitFunctionReturns(self, ctx:SolidityParser.FunctionReturnsContext):
        pass


    # Enter a parse tree produced by SolidityParser#emitStatement.
    def enterEmitStatement(self, ctx:SolidityParser.EmitStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#emitStatement.
    def exitEmitStatement(self, ctx:SolidityParser.EmitStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#emitIdentifier.
    def enterEmitIdentifier(self, ctx:SolidityParser.EmitIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#emitIdentifier.
    def exitEmitIdentifier(self, ctx:SolidityParser.EmitIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumPart.
    def enterEnumPart(self, ctx:SolidityParser.EnumPartContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumPart.
    def exitEnumPart(self, ctx:SolidityParser.EnumPartContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumIdentifier.
    def enterEnumIdentifier(self, ctx:SolidityParser.EnumIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumIdentifier.
    def exitEnumIdentifier(self, ctx:SolidityParser.EnumIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumValues.
    def enterEnumValues(self, ctx:SolidityParser.EnumValuesContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumValues.
    def exitEnumValues(self, ctx:SolidityParser.EnumValuesContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumValue.
    def enterEnumValue(self, ctx:SolidityParser.EnumValueContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumValue.
    def exitEnumValue(self, ctx:SolidityParser.EnumValueContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionStatement.
    def enterFunctionStatement(self, ctx:SolidityParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionStatement.
    def exitFunctionStatement(self, ctx:SolidityParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionStatementIdentifier.
    def enterFunctionStatementIdentifier(self, ctx:SolidityParser.FunctionStatementIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionStatementIdentifier.
    def exitFunctionStatementIdentifier(self, ctx:SolidityParser.FunctionStatementIdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#ifStatement.
    def enterIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#ifStatement.
    def exitIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#ifStatementBody.
    def enterIfStatementBody(self, ctx:SolidityParser.IfStatementBodyContext):
        pass

    # Exit a parse tree produced by SolidityParser#ifStatementBody.
    def exitIfStatementBody(self, ctx:SolidityParser.IfStatementBodyContext):
        pass


    # Enter a parse tree produced by SolidityParser#ifCondition.
    def enterIfCondition(self, ctx:SolidityParser.IfConditionContext):
        pass

    # Exit a parse tree produced by SolidityParser#ifCondition.
    def exitIfCondition(self, ctx:SolidityParser.IfConditionContext):
        pass


    # Enter a parse tree produced by SolidityParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:SolidityParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:SolidityParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#elseStatement.
    def enterElseStatement(self, ctx:SolidityParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#elseStatement.
    def exitElseStatement(self, ctx:SolidityParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#forStatement.
    def enterForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#forStatement.
    def exitForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#forStatementBody.
    def enterForStatementBody(self, ctx:SolidityParser.ForStatementBodyContext):
        pass

    # Exit a parse tree produced by SolidityParser#forStatementBody.
    def exitForStatementBody(self, ctx:SolidityParser.ForStatementBodyContext):
        pass


    # Enter a parse tree produced by SolidityParser#whileStatement.
    def enterWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#whileStatement.
    def exitWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#whileStatementBody.
    def enterWhileStatementBody(self, ctx:SolidityParser.WhileStatementBodyContext):
        pass

    # Exit a parse tree produced by SolidityParser#whileStatementBody.
    def exitWhileStatementBody(self, ctx:SolidityParser.WhileStatementBodyContext):
        pass


    # Enter a parse tree produced by SolidityParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#doWhileStatementBody.
    def enterDoWhileStatementBody(self, ctx:SolidityParser.DoWhileStatementBodyContext):
        pass

    # Exit a parse tree produced by SolidityParser#doWhileStatementBody.
    def exitDoWhileStatementBody(self, ctx:SolidityParser.DoWhileStatementBodyContext):
        pass


    # Enter a parse tree produced by SolidityParser#continueStatement.
    def enterContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#continueStatement.
    def exitContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#breakStatement.
    def enterBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#breakStatement.
    def exitBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#throwStatement.
    def enterThrowStatement(self, ctx:SolidityParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#throwStatement.
    def exitThrowStatement(self, ctx:SolidityParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#etherUnit.
    def enterEtherUnit(self, ctx:SolidityParser.EtherUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#etherUnit.
    def exitEtherUnit(self, ctx:SolidityParser.EtherUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#timeUnit.
    def enterTimeUnit(self, ctx:SolidityParser.TimeUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#timeUnit.
    def exitTimeUnit(self, ctx:SolidityParser.TimeUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#token.
    def enterToken(self, ctx:SolidityParser.TokenContext):
        pass

    # Exit a parse tree produced by SolidityParser#token.
    def exitToken(self, ctx:SolidityParser.TokenContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariable.
    def enterStateVariable(self, ctx:SolidityParser.StateVariableContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariable.
    def exitStateVariable(self, ctx:SolidityParser.StateVariableContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariableKeyword.
    def enterStateVariableKeyword(self, ctx:SolidityParser.StateVariableKeywordContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariableKeyword.
    def exitStateVariableKeyword(self, ctx:SolidityParser.StateVariableKeywordContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariableType.
    def enterStateVariableType(self, ctx:SolidityParser.StateVariableTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariableType.
    def exitStateVariableType(self, ctx:SolidityParser.StateVariableTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariableIdentifier.
    def enterStateVariableIdentifier(self, ctx:SolidityParser.StateVariableIdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariableIdentifier.
    def exitStateVariableIdentifier(self, ctx:SolidityParser.StateVariableIdentifierContext):
        pass


