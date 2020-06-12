for i in range(1,10):#控制行数
    for j in range(1,i+1):#输出与行数相当的列
        print(str(j)+"x"+str(i)+"="+str(j*i)+"\t",end='')
    print("")#换