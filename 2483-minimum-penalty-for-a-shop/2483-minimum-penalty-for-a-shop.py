class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        prefix_y = [0] * N

        number_of_y = 0
        for i in range(N-1,-1,-1):
            if customers[i] == "Y":
                number_of_y += 1
            prefix_y[i] = number_of_y
        prefix_y.append(0)

        prefix_n = []
        number_of_n = 0
        for i in range(N):
            prefix_n.append(number_of_n)
            if customers[i] == "N":
                number_of_n += 1
        prefix_n.append(number_of_n)

        minimum_penality = prefix_n[0] + prefix_y[0]
        hour = 0
        for i in range(1,N+1):
            curr_penality = prefix_n[i] + prefix_y[i]
            if curr_penality < minimum_penality:
                minimum_penality = curr_penality
                hour = i


        return hour