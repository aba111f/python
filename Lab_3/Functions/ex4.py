import math
def filter_prime(list):
    nums = list
    answer = []
    for x in nums:
        if x <= 1:
            continue
        i = 1
        primer = 0
        while i <= math.sqrt(x):
            if primer > 1:
                break
            if (int(x/i) * i) == x:
                primer += 1
            i += 1
        if primer <= 1:
            answer.append(x)
    return answer

print(filter_prime([1, 2, 3, 4 ,5 ,6 ,7 , 8]))