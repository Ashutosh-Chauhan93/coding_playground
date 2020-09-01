#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char **loadLarge(const char* filePath)
{
	FILE *fPtr = NULL;
	fPtr = fopen(filePath, "r");
	char **lines = (char **)malloc(10);

	if(!fPtr)
	{
	  return NULL;
	}
	return lines;
}
int main()
{
	char** lines = NULL;
	char* filePath = "example.txt";
	printf("%s\n",filePath);
	lines = loadLarge(filePath);
	if (!lines)
	{
		fprintf(stderr, "cant open file at %s\n",filePath);
		exit(1);
	}
	return 0;
}

