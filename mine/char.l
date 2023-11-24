%{
int har=0;
int word=0;
int line=0;
%}
%%
[' '] {word++; har++;}
\n { word++; line++;}
[a-zA-Z] {har++;}
%%
int yywrap(void){}
int main(){

printf("enter a string: \n");
yylex();
printf("line= %d, word=%d, char=%d \n",line,word, har);
return 0;
}

 
















