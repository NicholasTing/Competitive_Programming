# std::vector<int>conj[maxn];
# int n,k,u,v,depth[maxn]={0},size[maxn]={0},det[maxn];
# long long ans=0;

from collections import defaultdict
import resource, sys

try:

    conj = defaultdict(list)
    depth = defaultdict(int)
    size = defaultdict(int)
    det = defaultdict(int)

    ans = 0

    # int dfs(int u,int f){
    #  depth[u]=depth[f]+1;size[u]=1;
    # 	for (int i=0;i<conj[u].size();++i){
    # 		if ((v=conj[u][i])==f)continue;
    # 		size[u]+=dfs(v,u);
    # 	}det[u]=size[u]-depth[u];return size[u];
    # }

    def dfs(u,f):
        depth[u] = depth[f] + 1
        size[u] = 1
        for i in range(len(conj[u])):
            v = conj[u][i]
            if v == f:
                pass
            else:
                size[u] += dfs(v,u)
        
            det[u] = size[u] - depth[u]
            
        return size[u]

    n, k = map(int,input().split())
    N = n

    # int main(){
    # 	scanf("%d%d",&n,&k);
    # 	for (int i=1;i<n;++i){
    # 		scanf("%d%d",&u,&v);conj[u].push_back(v);conj[v].push_back(u);
    # 	}dfs(1,0);
    # 	std::nth_element(det+1,det+n-k,det+n+1,cmp);
    # 	for (int i=1;i<=n-k;++i)ans+=det[i];std::cout<<ans;
    # 	return 0;
    # }

    while N > 1:
        u,v = map(int,input().split())
        conj[u].append(v)
        conj[v].append(u)
        N -= 1

    dfs(1,0)

    answer = 0

    det_sorted = sorted(det.values(),reverse=True) 

    if det_sorted == []:
        pass

    else:
        count = n-k
        for i in range(len(det_sorted)):
            if count != 0:
                answer += det_sorted[i]
            elif count == 0:
                break
            count -=1

    print(answer)

except:
    print("Unexpected error:", sys.exc_info()[0])