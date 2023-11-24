%{
int valid=0;

%} 





%%


^[0-9]{10}$ {valid=1;}


%%
int yywrap(void){}
int main(){

yylex();

if(valid==0){
printf("inavlid\n");

}
else{ printf("valid\n");
}
return 0;


}










