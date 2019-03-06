def perm(lis, x):
    if x==1:
        return lis
    y = len(lis)
    liz =[]
    for i in range(int(lis[0]),y):
        for  j in range(int(lis[0]),int(lis[len(lis)-1][0])+1):
            liz.append("{}{}".format(int(lis[i]),j))
    return perm(liz,x-1)
