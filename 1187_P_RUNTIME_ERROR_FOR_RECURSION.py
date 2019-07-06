import sys
sys.setrecursionlimit(int(1e6))
N=int(2e5+5000)
class Edge():
	def __init__(self):
		self.nex=0
		self.pnt=0
ed=[Edge()]
fir=[0]*N
cnt=0
def init():
	ran=N*2
	for i in range(1,ran):
		ed.append(Edge())
def link(u,v):
	global cnt
	cnt+=1
	ed[cnt].nex=fir[u]
	fir[u]=cnt
	ed[cnt].pnt=v
siz,dp=[[0]*N,[0]*N]
def presiz(u,p):
	siz[u]=1
	e=fir[u]
	while(e!=0):
		v=ed[e].pnt
		if v==p:
			e=ed[e].nex
			continue
		presiz(v,u)
		siz[u]+=siz[v]
		e=ed[e].nex
def predp(u,p):
	dp[u]=siz[u]
	e=fir[u]
	while(e!=0):
		v=ed[e].pnt
		if v==p:
			e=ed[e].nex
			continue
		predp(v,u)
		dp[u]+=dp[v]
		e=ed[e].nex
ans=0
def rer(u,p):
#	pr(u)
	global ans
	ans=max(ans,dp[u])
	e=fir[u]
	while(e!=0):
		v=ed[e].pnt
		if v==p:
			e=ed[e].nex
			continue
		curs,curdp,sons,sondp=[siz[u],dp[u],siz[v],dp[v]]
		siz[u]-=siz[v]
		dp[u]=dp[u]-siz[v]-dp[v]
		siz[v]+=siz[u]
		dp[v]=dp[v]+siz[u]+dp[u]
		rer(v,u)
		siz[u],dp[u],siz[v],dp[v]=[curs,curdp,sons,sondp]
		e=ed[e].nex
def pr(n):
	print(n)
if __name__=='__main__':
	init()
	n=int(input())
	for i in range(1,n):
		u,v=list(map(int,input().split(' ')))
		link(u,v),link(v,u)
#	pr(n)
	presiz(1,0)
	predp(1,0)
	rer(1,0)
	print(ans)