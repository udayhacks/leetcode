# Last updated: 04/04/2026, 13:11:36
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        lone_node_count = sum(1 for node in range(n) if node not in graph)
        candidates = [tuple(sorted([node] + graph[node])) for node in graph]
        return lone_node_count + sum(1 for component, count in Counter(candidates).items() if len(component) == count)