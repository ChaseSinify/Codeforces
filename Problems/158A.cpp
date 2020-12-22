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
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef long double ld;

const int nax = 1e5+1;
char s[nax];

int main(){
    int n, k;
    scanf("%d %d", &n, &k);
    vi nums(n);
    for(int i=0; i<n; i++){
        scanf("%d", &nums[i]);
    }
    int res = 0;
    for(int j=0; j<n; j++){
        if(nums[j] >= nums[k-1] && nums[j] > 0){res++;}
    }
    printf("%d", res);
}