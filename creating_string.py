my_string = input()
my_string.split(" ")
for i in range(len(my_string)):
    my_string[i] = ord(my_string[i]) - ord("a")
is_included = [False] * len(my_string)

def get_perm(single_string, current_string, is_included):
    single_string = sorted(single_string)
    if len(current_string) == len(single_string):
        print(current_string)
    else:
        for i in range(len(single_string)):
            if is_included[i] == False:
                if i > 0 and single_string[i] == single_string[i-1] and not is_included[i-1]:
                    i += 1
                    continue 

                current_string.append(single_string[i])
                is_included[i] = True
                get_perm(single_string, current_string, is_included)

                current_string.pop(-1)
                is_included[i] = False
           
            else:
                pass

get_perm(my_string, [], is_included)