import math

global l, r, s, sstr

def exist(str1, str2):
    a = set(map(lambda x: int(x), set(str2)))
    a = list(a)
    for i in range(len(a)):
        if str1.count(str(a[i])) < str2.count(str(a[i])):
            return 0
    return 1
def func(str1, str2, flag):
    global l, r, s
    if flag == 0:
        for i in range(2, 30):
            if r / 2 ** (i - 1) < 1:
                flag = 1
                str1 = sstr
                break
            if exist(str1[:math.ceil(r * (1 - 1 / 2 ** (i - 1)))], str2):
                r = math.ceil(r * (1 - 1 / 2 ** (i - 1)))
                if r+1 == len(str2):
                    flag = 1
                    str1 = sstr
                    break
                func(str1[:r], str2, flag)
            else:
                continue
    for n in range(2, 30):
        if (r - l) / 2 ** (n - 1) < 1 and exist(sstr[l:r-1],str2)==0 and exist(sstr[l+1:r],str2)==0:
            if l > r and s == 0:
                print(0, r +1,22)
                s = 1
            elif l - 1 < 0 and s == 0:
                print(0, r +1,33)
                s = 1
            elif s == 0:
                print(l, r +1,44)
                s = 1
            return
        if exist(str1[math.floor((r - l) * 1 / 2 ** (n - 1)):], str2):
            l = math.floor(l + (r - l) * 1 / 2 ** (n - 1))
            a=l
            if r - l == len(str2) and s==0:
                print(l+1,r)
                s = 1
                return
            func(str1[math.floor((r - a) * 1 / 2 ** (n - 1)):], str2, flag)
        else:
            continue
if __name__ == "__main__":
    num = input()
    for i in range(int(num)):
        str1 = input()
        str2 = input()
        global l, r, sstr
        sstr = str1
        r = len(str1)
        print(r)
        l = 0
        s=0
        if exist(str1, str2):
            func(str1, str2, 0)
        else:
            print("-1 -1")