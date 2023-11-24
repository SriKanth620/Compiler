%{
int pos=0, neg=0;
%}
%%
[0-9]+ { pos++;
printf("Pos nos= %s\n", yytext);}

^[-][0-9]+ { neg++;
printf("neg nos= %s\n", yytext);}
%%










int yywrap(void){}
int main(){
printf("enter: ");
yylex();
printf("pos no= %d & neg no = %d", pos, neg);
return 0;
}

