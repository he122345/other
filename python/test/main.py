if __name__ == '__main__':
    print('程序自身在运行')
    f=open("test.txt","r+")
    str=f.read()
    print(str)
    f.write("xddx")
    f.close()

    a=1
    b=2
    a,b=b,a
    print(a,b)
    for i in range(1,5):
        print(i,end="")
else:
    print('我来自另一模块')
