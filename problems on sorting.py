'''
sorting even elements in descending order at the beginning of the list and odd elements in ascending order at the end of the list
'''

nums = [3,6,1,7,4,2,5]
nums.sort()
res = []
for i in nums:
    if i % 2 == 0:
        res.insert(0,i)
    else:
        res.append(i)
print(res)

'''
2nd largest
'''

l1 = [10,23,456,9,24]
l1.sort()
print("2nd largest:",l1[len(l1)-2])

'''
Don't sort first and last k elements,sort rest of the array
'''
nums = [2,3,5,1,6,9,8]
k = 2
ans = nums[:k] + sorted(nums[k:len(nums)-k]) + nums[-k:]
print(ans)

'''
Based on the second element in the 2D list ,sort the 2D list

'''

l1 = [[1,2],[5,1],[2,4],[6,3]]
ans = []

for _ in range(len(l1)):
    min_value,min_indx = float('inf'),0
    for j in range(len(l1)):
        if l1[j][1] < min_value:
            min_value = l1[j][1]
            min_indx = j
    ans.append(l1[min_indx])
    l1.pop(min_indx)
print(ans)

'''
Sorting string based on frequency

'''
from collections import Counter
s = input()
d1 = Counter(s)
ans = ""

while d1:
    min_cnt = float('inf')
    min_value = None
    
    for val in d1:
        if d1[val] < min_cnt:
            min_cnt = d1[val]
            min_value = val
    
    ans += min_value * min_cnt
    d1.pop(min_value)

print(ans)