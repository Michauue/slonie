from sys import maxsize

def readFile(filename):
    tab = []
    with open(filename) as f:
        for line in f:
            tab.append(list(map(int,line.split())))
    return tab

def main(filename):
    max_value = maxsize
    result = 0
    tab = readFile(filename)
    n = tab[0][0]
    weights = tab[1]
    min_weight = min(weights)
    original = [tab[2][i]-1 for i in range(len(tab[2]))]
    perm = [_ for _ in range(len(tab[3]))]
    nr = [tab[3][i] - 1 for i in range(len(tab[3]))]
    for i in range(len(perm)):
        perm[nr[i]] = original[i]
    temp = [False for _ in range(n)]

    for i in range(n):
        if(temp[i] is not True):
            min_cycle = max_value
            summary = 0
            current = i
            length = 0
            while(True):
                min_cycle = min(min_cycle, weights[current])
                summary += weights[current]
                current = perm[current]
                temp[current] = True
                length += 1
                if(current == i):
                    break
            result += min(summary+(length-2)*min_cycle, summary+min_cycle+(length+1)*min_weight)
    return print(result)


main(input())