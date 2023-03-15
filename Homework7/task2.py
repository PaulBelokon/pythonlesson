def math_tabl(progress,rows=10,columns=10):
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            print(f"{progress(i,j):4}", end="  ")
        print()
math_tabl(lambda x,y: x*y)