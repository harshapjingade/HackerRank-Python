import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    # without textwrap code
    #for i in range(0,len(string),max_width):
     #   string=string.strip()
     #   print (string[i:i+max_width])
