def judging_two_lists(plain_cow_group, spotty_cow_group):
    #A and G show spotty, C shows plain
    #Only A and G is 1, Only C is 0, Both is 2
    plain_cow_result = None
    spotty_cow_result = None
    if len(plain_cow_group) == len(spotty_cow_group):
        for i in plain_cow_group:
            if ("A" or "G") in i:
                plain_cow_result = 1
                if ("A" or "G" and "C") in i:
                    plain_cow_result = 2
            else:
                plain_cow_result = 0
        for i in spotty_cow_group:
            if ("A" or "G") in i:
                spotty_cow_result = 1
                if ("A" or "G" and "C") in i:
                    spotty_cow_result = 2
            else:
                spotty_cow_result = 0
    
    if plain_cow_result == 1 and spotty_cow_result == 0:
        return True
    else:
        return False

def main():
    with open("cownomics.in", 'r') as f:
        N, M = list(map(int, f.readline().split()))
        plain_cow_genomes = []
        spotty_cow_genomes = []
        for _ in range(N):
            plain_cow_genomes.append(f.readline().strip("\n"))
        for _ in range(N):
            spotty_cow_genomes.append(f.readline().strip("\n"))
        ans = 0
        
    print(plain_cow_genomes, spotty_cow_genomes)

    for i in range(M):
        plainGroup = ""
        spottyGroup = ""
        for j in range(N):
            plainGroup = plainGroup + plain_cow_genomes[j][i]
            spottyGroup = spottyGroup + spotty_cow_genomes[j][i]
        if judging_two_lists(plainGroup, spottyGroup):
            ans += 1
        else:
            ans += 0
    
    return ans

print(main())