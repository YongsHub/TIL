from collections import defaultdict


def solution(tickets):

    def init_graph(tickets):
        routes = defaultdict(list)

        for ticket in tickets:
            routes[ticket[0]].append(ticket[1])

        return routes

    def dfs(routes):
        stack = ['ICN']
        path = []

        while len(stack) > 0:
            top = stack[-1]

            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))

        return path

    routes = init_graph(tickets)
    for route in routes:
        routes[route].sort()

    answer = dfs(routes)
    answer.reverse()

    return answer
