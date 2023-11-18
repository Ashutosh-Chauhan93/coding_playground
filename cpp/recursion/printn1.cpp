#include<iostream>
using namespace std;

void printn1(int n){
	//base
	if (n==1){
	  cout << n;
	  return;
	}
	cout << n;
	printn1(n-1);
}


int main(){
printn1(7);
return 0;
}
