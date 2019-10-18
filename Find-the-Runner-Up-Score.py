if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    item = max(arr)
    while max(arr) == item:
       arr.remove(item)
    print(max(arr))
