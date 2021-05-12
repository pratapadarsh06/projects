#include<fcntl.h> //header file for copy command
#include<stdio.h>
#include<stdlib.h>
main(int argc,char*argv[])
{
if(argc!=3){ //checks whether 3 arguments are given
printf("\nSyntax error");
printf("\nThe syntax is as follows");
printf("\ncommandname filetocopy filetorename");
exit(1);
}
int fdold,fdnew,count;
char buffer[2048]; //character buffer to store content
fdold=open(argv[1], O_RDONLY);
if(fdold==-1)
{
	printf("cannot open file");
}
fdnew=creat(argv[2],0666);
if(fdnew==-1)
{
printf("cannot create file");
}
while((count=read(fdold,buffer,sizeof(buffer)))>0)
{
write(fdnew,buffer,count); //to copy the content
}
exit(0);
}

