def print_formatted(number):
    w = len(str(bin(number)).split('b')[1])
    for i in range(1,int(number)+1):
        dec= str(i)
        oc = str(oct(i).split('o')[1])
        he=str(hex(i).split('x')[1]).upper()
        bi=str(bin(i).split('b')[1])

        print(dec.rjust(w),oc.rjust(w), he.rjust(w), bi.rjust(w))
