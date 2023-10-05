def judging_two_sequences(plain_cow_seq, spotty_cow_seq):
    status = []
    return_status = None
    for i in spotty_cow_seq:
        if (i in plain_cow_seq) == True:
            status.append(True)
        else:
            status.append(False)
    
    for i in range(len(status)):
        if status[i] == False:
            return_status = False
        else:
            return_status = True
            break
    
    return return_status

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
    plain_group = []
    spotty_group = [] 
    for colunm in range(M):
        plain_group = []
        spotty_group = []
        for row in range(N):
            plain_group.append(plain_cow_genomes[row][colunm])
            spotty_group.append(spotty_cow_genomes[row][colunm])
        if judging_two_sequences(plain_group, spotty_group) == False:
            ans += 1

    with open('cownomics.out', 'w') as f:
        f.write(str(ans))
    
if __name__ == "__main__":
    main()