#include<iostream>
#include <string.h>//given stirng.h...actually string.h
using namespace std;//newly added
int getLIndex(char[],char);//newly added function prototype
int getFindex(char[],char);//"  "
int main()
{
	char str[100];
	char ch; 
	int Lindex,Findex; 
	cin >> str;//semicolon
	cin >> ch;
	Findex = getLIndex(str,ch);//interchanged labels
	Lindex= getFindex(str,ch);//function name was wrong
	if(Lindex!=-1 && Findex!=strlen(str))//added one more condition
		cout<<Findex<<endl<<Lindex;
	else
		cout<<"NOT FOUND"<<endl;
	return 0;	
}
int getLIndex(char string[],char  c)  //changed string to string[]
{
	int size = strlen(string),i=0;//changes to strlen
	while(i<size)
	{
		
		if(string[i]==c){//changed to ==
		   break;
		}	
		i++; 
	}
	return i;//moved return from if to this position
}
int getFindex(char string[],char c)//three changes:added char data type for first arguement,string[] and char for c
{
	int size = strlen(string);//changed to strlen
	int i=size; 
	while( i>=0) //removed unwanted semicolon
{		
		if(string[i]==c){
 break;
		}	
	i--;
	return i;//moved return from if to end
}
		
}
/*total 18 changes as above*/