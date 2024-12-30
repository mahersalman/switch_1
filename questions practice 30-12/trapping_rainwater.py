"""
Trapping Rainwater Problem states that given an array of n non-negative integers
 arr[] representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after rain.

Tasks:
1.	Write a brute force solution
2.	Write an efficient solution in O(n)
3.	Solve the problem but now return the max amount of water that can be trapped between 2 buildings

"""

def get_max_amount_can_trapped(arr):
    left_side_max = [arr[0]]*len(arr)
    for i in range(1,len(arr)):
        left_side_max[i] = max(left_side_max[i-1],arr[i])

    right_side_max = [arr[-1]]*len(arr)
    for i in range(len(arr)-2,-1,-1):
        right_side_max[i] = max(right_side_max[i+1],arr[i])
    
    water_per_index = []
    for i in range(len(arr)):
        water_per_index.append(min(left_side_max[i],right_side_max[i])-arr[i])
    
    max_amount = 0
    current_amount = 0
    for i in water_per_index:
        if i == 0:
            max_amount = max(max_amount,current_amount)
            current_amount = 0
        else:
            current_amount+=i
    return max_amount



#Optimal O(n)
def trapping_rainwater(arr):
    left_side_max = [arr[0]]*len(arr)
    for i in range(1,len(arr)):
        left_side_max[i] = max(left_side_max[i-1],arr[i])

    right_side_max = [arr[-1]]*len(arr)
    for i in range(len(arr)-2,-1,-1):
        right_side_max[i] = max(right_side_max[i+1],arr[i])
    
    water_per_index = []
    for i in range(len(arr)):
        water_per_index.append(min(left_side_max[i],right_side_max[i])-arr[i])
    
    return sum(water_per_index)



#Brute Force - O(n^2)
def trapping_rainwater(array):
    def find_max_building(index,array):
        max_height_index = index+1
        water = 0
        for i in range(index+1,len(array)):
            
            if array[i] >= array[index]:
                return i
            max_height_index = i if array[i] > array[max_height_index] else max_height_index
        return -1 if max_height_index == 0 else max_height_index

    def water_trap_per_partition(start,end,array):
        water = min(array[start],array[end])*(end-start-1)    

        for i in range(start+1,end):
            water -= array[i]
        return water

    water = 0
    i = 0
    while i < len(array)-1:
        next_max_building= -1
        if array[i] != 0 :
            next_max_building = find_max_building(i,array)
            if next_max_building != -1:
                water += water_trap_per_partition(i,next_max_building,array)
                i=next_max_building
            else:
                i+=1
        else:
            i+=1
        
    return water        


