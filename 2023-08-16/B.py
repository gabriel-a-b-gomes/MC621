def main():
    n, m, s, t = map(int, input().split())

    E = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())

        E[u].append(v)
        E[v].append(u)

    infected = {}
    infected[s] = 1

    for i in range(t):
        infected_new = {}
        for key in infected.keys():
            q = infected[key]
            for v in E[key]:
                if v not in infected_new.keys():
                    infected_new[v] = q
                else:
                    infected_new[v] += q

        infected = infected_new

    total = 0
    for key in infected.keys():
        total += infected[key]
    
    print(total)

main()