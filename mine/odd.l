%{
int i=0;
%}
%%
[0-9]+ {i=atoi(yytext);
if(i%2==0){

printf("even");
}
else{



printf("odd");
}}
%%
int yywrap(void){}
int main(){
printf("enter: ");
yylex();
return 0;
}

