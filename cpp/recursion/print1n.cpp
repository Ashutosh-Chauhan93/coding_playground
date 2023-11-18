#include<iostream>
using namespace std;

void print1n(int n){
	//base
	if (n==1){
	  cout << n;
	  return;
	}
	print1n(n-1);
	cout << n;
}


int main(){
print1n(7);
return 0;
}
