import random
def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0 
    neu = 0
    for i in range(len(arr)):
        if arr[i]<0:
            neg+=1
        elif arr[i]>0:
            pos+=1
        else:
            neu+=1

    print('%.6f' %(int(pos)/len(arr)))
    print('%.6f' %(neg/len(arr)))
    print('%.6f' %(neu/len(arr)))


arr = []
for i in range(1000):
    arr.append(random.randint(-10,10))

plusMinus(arr)
