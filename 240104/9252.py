str1 = [0] + list(input())
str2 = [0] + list(input())

len_1 = len(str1)
len_2 = len(str2)

array = [['' for _ in range(len_1)] for _ in range(len_2)]

for i in range(1, len_2) :
    for j in range(1, len_1) :
        if str1[j] == str2[i] :
            array[i][j] = array[i-1][j-1] + str1[j]
        else :
            if len(array[i][j-1]) > len(array[i-1][j]) :
                array[i][j] = array[i][j-1]
            else : 
                array[i][j] = array[i-1][j]

answer = len(array[-1][-1])
print(answer)
if answer != 0 :
    print(array[-1][-1])
