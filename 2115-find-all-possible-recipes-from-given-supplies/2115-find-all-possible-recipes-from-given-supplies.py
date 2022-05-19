class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        neighbours, indegree = defaultdict(list), defaultdict(int)
        for i in range(len(ingredients)):
            ing = ingredients[i]
            for j in range(len(ing)):
                neighbours[ing[j]].append(recipes[i])
                indegree[recipes[i]]+=1
        
        for i in range(len(supplies)):
            for recipe in neighbours[supplies[i]]:
                indegree[recipe]-=1
        queue = deque()
        for k in indegree.keys():
            if indegree[k] == 0: queue.append(k)
                
        res = []
        while queue:
            curr = queue.popleft()
            for recipe in neighbours[curr]:
                indegree[recipe]-=1
                if indegree[recipe] == 0: queue.append(recipe)
            res.append(curr)
        
        return res
                