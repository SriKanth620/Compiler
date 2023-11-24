%{
int flag=0;
%}
%%


([1-9][0-9]{3})-(0[1-9]|1[1-2])-(0[1-9]|[1-2][0-9]|3[0-1]) {flag=1;} 


%%
int yywrap(void){}
int main(){
printf("Enter [yyyy]-[mm]-[dd]: ");
yylex();
if(flag==1){
printf("valid");}
else{
printf("invalid");
}
return 0;

}

















