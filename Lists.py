if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        value = input().split()
        if 'insert' in value:
            list.insert(int(value[1]),int(value[2]))
        elif 'print' in value:
            print(list)
        elif 'remove' in value:
            list.remove(int(value[1]))
        elif 'append' in value:
            list.append(int(value[1]))
        elif 'sort' in value:
            list.sort()
        elif 'pop' in value:
            list.pop()
        elif 'reverse' in value:
            list.reverse()
