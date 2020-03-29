#include<stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

  char *run= "python3 tracon.py ";

 for(int i= 1; i < argc; i++){
  char *tmp= (char*) malloc((strlen(run)+1)*sizeof(char));
  strcpy(tmp,run);
  run= (char*) malloc((strlen(argv[i])+strlen(tmp)+2)*sizeof(char));
  strcpy(run,tmp);
  strcat(run," ");
  strcat(run,argv[i]);
 }

 system (run); 
 return 0;

}
