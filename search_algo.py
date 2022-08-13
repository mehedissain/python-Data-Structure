def search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)


data = [10,20,30,40]
curr_index =data[0] 
key = 10  
search(data,curr_index+1,key)    








# def search(arr, x):
 
#     for i in range(len(arr)):

 
#         if arr[i] == x:
#             return print(i)
 
#     return -1

# print(search(data,50))
    
    
