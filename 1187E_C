#include<bits/stdc++.h>
const double ep=1e-7;
const int N=2e5+5000;
int n;
long long ans;
void pf(int a);
namespace Graph{
	struct Edge{
		int nex,pnt;
	}ed[N*2];
	int fir[N],cnt;
	void link(int u,int v){
		++cnt;
		ed[cnt].nex=fir[u],fir[u]=cnt,ed[cnt].pnt=v;
	}
	int siz[N];
	long long dp[N];
	void presiz(int u,int p){
		siz[u]=1;
		for(int e=fir[u];e;e=ed[e].nex){
			int v=ed[e].pnt;
			if(v==p)continue;
			presiz(v,u);
			siz[u]+=siz[v];
		}
	}
	void predp(int u,int p){
		dp[u]=siz[u];
		for(int e=fir[u];e;e=ed[e].nex){
			int v=ed[e].pnt;
			if(v==p)continue;
			predp(v,u);
			dp[u]+=dp[v];
		}
//		pf(dp[u]);
	}
	void rer(int u,int p){
		ans=std::max(ans,dp[u]);
//		pf(dp[u]);
		for(int e=fir[u];e;e=ed[e].nex){
			int v=ed[e].pnt;
			if(v==p)continue;
			long long curs=siz[u],curdp=dp[u],sons=siz[v],sondp=dp[v];
			siz[u]-=siz[v],dp[u]-=dp[v],dp[u]-=siz[v];
			dp[v]+=dp[u],dp[v]+=siz[u],siz[v]+=siz[u];
			rer(v,u);
			siz[u]=curs,dp[u]=curdp,siz[v]=sons,dp[v]=sondp;
		}
	}
}
using namespace Graph;
void pf(int a){printf("%d\n",a);}
int main(){
//#ifdef DEBUG
//	freopen("in.txt","r",stdin);
//#endif
	scanf("%d",&n);
//	pf(n);
	for(int i=1;i<=n-1;++i){
		int u,v;
		scanf("%d%d",&u,&v);
		link(u,v),link(v,u);
//		pf(u);
	}
	presiz(1,0);
	predp(1,0);
	rer(1,0);
	printf("%lld",ans);
	return 0;
}