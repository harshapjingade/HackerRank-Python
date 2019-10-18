if __name__ == '__main__':
    students=[]
    values=[]
    my=[]
    for _ in range(int(input())):
        name_score=[]
        name = input()
        name_score.append(name)
        score = float(input())
        name_score.append(score)
        students.append(name_score)
    for i in range(len(students)):
        values.append(students[i][1])
    item=min(values)
    while min(values) == item:
        values.remove(item)
    low=min(values)
    for i in range(len(students)):
        if low == students[i][1]:
            my.append(students[i][0])
            #print(my)
    for i in sorted(my):
        print(i)

