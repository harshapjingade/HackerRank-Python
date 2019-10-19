def swap_case(s):
    new=""
    for i in s:
        if (i.isupper()):
            new += i.lower()
        else:
            new += i.upper() 
    return new
