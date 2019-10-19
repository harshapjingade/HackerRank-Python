def mutate_string(string, position, character):
    #string=string[:5] + "k" + string[6:]
    l = list(string)
    l[position]=character
    string=''.join(l)
    return string
