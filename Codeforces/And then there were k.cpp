#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<long long> vl;
typedef pair<int,int> pi;
#define push_back PB
#define make_pair MP
#define forsn(i,a,b) for(int i=a;i<b;++i)
#define fast_io() ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)

void inline Online(){
#ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
#endif
}
bool comp(ll &a,ll &b){
	if(a>b)
		return true;
	return false;
}
void swap(ll &a,ll &b){
	ll c;
	c=a;
	a=b;
	b=c;
}

void solve(){
	int t;
	cin>>t;
	while(t--){
		ll r,k,i=1;
		cin>>r;
		k=r;
		while(k!=0){
			i*=2;
			k/=2;
 
		}
		i/=2;
		cout<<i-1<<"\n";
 
	}
	
 
}

void check(){
	int t=86;
	forsn(i,1,10){
		forsn(j,1,6){
			forsn(k,0,6){
				t--;
				if(t==0){
					cout<<i<<j<<k;
					break;
				}
			}
		}
	}
}
int main(){
	
	fast_io();
	Online();
	solve();
	//check();
	return 0;

}