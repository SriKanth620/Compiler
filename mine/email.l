%{



int flag=0;

%}
%%





[0-9a-z\.]+@[a-z]{5,8}\.[a-z]{2,9} {flag=1;} 
%%
int yywrap(void){}
int main(){
printf("enter: ");
yylex();
if(flag==1){
printf("valid\n");
}
else{
printf("Invalid\n");
}
return 0;
}













