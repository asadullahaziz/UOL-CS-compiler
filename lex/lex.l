%{
#include<stdio.h>
%}

%%

"CONST"|"FLOAT"|"INT"|"BREAK"|"CONTINUE"|"ELSE"|"FOR"|"SWITCH"|"VOID"|"CASE"|"MINE"|"CS"|"CHAR"|"DO"|"IF"|"RETURN"|"WHILE"|"UOL"|"DEAN"|"HOD" {printf("\nReserve Word");}

"#DEFINE"|"#INCLUDE" {printf("\nReserved Keyword.");}

["_"0-9a-zA-Z]+[0-9]+[a-zA-Z0-9"_"]* {printf("\nIdentifier.");}

[0-9]+[0-9"."]* {printf("\nNumber.");}

"<"|">"|"="|"<>"|":="|"=="|"*"|"+"|"/"|"-"|">>>"|"<<<"|"++"|"+="|"-="|"--" {printf("\nOperator.");}

"Input>>>" {printf("\nInput Operator.");}

"Output<<<" {printf("\nOutput Operator.");}

"["|"{"|"("|")"|"}"|"]"|"'" {printf("\nPunctuation.");}

[//]+[a-zA-Z0-9" "]* {printf("\nComment.");}

"/*"+[a-zA-Z0-9" "]+"*/" {printf("\nComment.");}

[a-zA-Z0-9]* {printf("\nInvalid Input!!");}

%%

int yywrap()
{
	return 1;
}
main()
{
	
	printf("Enter some string: ");
	yylex();

}