print("Input size of array: ")
size = int(input()) 
nums = [0]*size
print("Input array: ")
for i in range(size):
    nums[i]=int(input())

indexToSumm=[0,1]

summ = nums[indexToSumm[0]]+ nums[indexToSumm[1]]
print(summ)