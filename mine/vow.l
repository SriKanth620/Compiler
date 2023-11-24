%{
int vow=0;

int con=0;
%}
%%
[' '] ;
\n ;
[aeiouAEIOU] {vow++;}
[^aeiouAEIOU] {con++;}
%%

int yywrap(void){}
int main(){
printf("enter: ");
yylex();
printf("vow= %d, con=%d \n", vow, con);
return 0;
} 






























