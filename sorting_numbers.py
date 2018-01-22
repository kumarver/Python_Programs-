'''
ls = ['1','4','6','2','0']
ls = [int(i) for i in ls]
ls.sort()
print ls
'''
ls = ['1','4','6','2','0']
ls1 = sorted([int(i) for i in ls],reverse=True)
#ls1 = sorted(ls,reverse=True)
print ls1
