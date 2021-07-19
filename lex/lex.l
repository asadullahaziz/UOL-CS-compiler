%{ 
#include<stdio.h>
%}

/* Rules Section/
%%
[0-9][.][0-9]+ {printf("Number\n");}
[0-9]*          {printf("Number\n");}
"CONST"|"FLOAT"|"INT"|"BREAK"|"CONTINUE"|"ELSE"|"FOR"|"SWITCH"|"VOID"|"CASE"|"MINE"|"CS"|"CHAR"|"DO"|"IF"|"RETURN"|"WHILE"|"UOL"|"DEAN"|"HOD"|"#DEFINE"|"#INCLUDE"            {printf("Reserver Words\n");}
[0-9][a-zA-z|0-9|]*[a-zA-z|0-9]                       {printf("identifier\n");}
[a-zA-z|]+[0-9]                                         {printf("identifier\n");}
[a-zA-z|]+[0-9][a-zA-z|0-9|][a-zA-z|0-9]         {printf("identifier\n");}
"Input>>>"                                       {printf("User Input\n");}
"Output<<<"                                       {printf("User output\n");}
"/"[a-zA-z|0-9]+"/"                                    {printf("Comments\n");}
"<"|">"|"="|"<>"|":="|"=="|""|"+"|"/"|"-"|">>>"|"<<<"|"++"|"+="|"-="|"--"    {printf("Operater\n");}
"["|"{"|"("|")"|"}"|"]"|"”"|"”"  {printf("Punctuator\n");}
"//"[a-zA-Z|0-9]+                                          {printf("Comments\n");}
%% 

int yywrap(void)
{
    return 1;
} 

int main() 
{
    // The function that starts the analysis 
    printf("Enter a string :");
    yylex(); 
    return 0; 
}