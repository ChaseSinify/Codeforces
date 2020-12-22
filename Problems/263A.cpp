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
vector<vector<int>> matrix;

int d;
vector<int> temp;
int x=0, y=0;

int main(){

    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            scanf("%d", &d);
            temp.push_back(d);
        }
        matrix.push_back(temp);
        temp.clear();
    }

    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            if(matrix[i][j] == 1){
                x=i;
                y=j;
                break;
            }
        }
    }
    printf("%d", (abs(2-x) + abs(2-y)));
}