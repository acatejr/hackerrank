def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return(string)

if __name__ == '__main__':
    string = "abracadabra"
    postion = 5
    character = "k"

    print(mutate_string(string, postion, character))