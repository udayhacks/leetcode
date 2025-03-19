import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    
    def dijkstra(self, V: int, adj, S: int) :
        
        
        # here dis array store shortest distance from source to each index in dis 
        
        dis = []
        for i in range(V):
            dis.append(1e9)
            
        dis[S] = 0
   
        hd = []
        heapq.heappush(hd,[0,S])
        
        
        while hd :
            #here d is the shortest distance to reach the n node 
            d,n = heapq.heappop(hd)
            
            for an ,ad in adj[n] :
                #here d+ad is the distance required to reach an node from n -->> an (adjacent node)
                if dis[an] > d+ad :
                    dis[an] = d+ad
                    heapq.heappush(hd,[dis[an],an])
                    
                    
        for v in range(V):
            if dis[v] == 1e9:
                dis[v] =-1
                
                
        return dis
            
            
        
        
        