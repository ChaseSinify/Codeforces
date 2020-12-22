#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define F first
#define S second
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007

#define YES printf("YES")
#define NO printf("NO")

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef long double ld;

const int nax = 101;
char s[nax];

int main(){
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
       scanf("%s", s);
       int n = strlen(s);
       if(n>10){printf("%c%d%c\n", s[0], n-2, s[n-1]);}
       else{printf("%s\n", s);}
    }
}