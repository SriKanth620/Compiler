%%












^[aA].* {printf("true %s\n", yytext);}


^[^aA].* {printf("false\n");}

\n; 
[' '] ;
%%
int yywrap(void){}
int main(){
yylex();
return 0;




}   
