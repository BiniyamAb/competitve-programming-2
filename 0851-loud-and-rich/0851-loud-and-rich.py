class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        wealth_relation = defaultdict(set)
        
        @cache
        def findQuitestPerson(person):
            quietest_person = person
            least_quiet_value = quiet[person]
            for richer_person in wealth_relation[person]:
                quietest = findQuitestPerson(richer_person)
                if quiet[quietest] < least_quiet_value:
                    least_quiet_value = quiet[quietest]
                    quietest_person = quietest
        
            return quietest_person
            
        
        for person1, person2 in richer:
            wealth_relation[person2].add(person1)
        
        answer = []
        for person in range(len(quiet)):
            curr_quitest = findQuitestPerson(person)
            answer.append(curr_quitest)
        
        return answer
        