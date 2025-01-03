import numpy as np
def create_matrix(mc):
    print("\n Array"+str(mc)+" elements")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("\n Array"+str(mc)+" row,column")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("\n NO MATCH")
        return(create_matrix(mc))
    print("\n ARRAY \n")
    array_1=array_1.reshape(row,column)
    print(array_1)
    return(array_1)
arr1=create_matrix(1)
arr2=create_matrix(2)
print("\n Dot Product \n")
print(np.dot(arr1,arr2))
