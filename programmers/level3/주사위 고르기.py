from itertools import combinations, product
from collections import defaultdict
from bisect import bisect_left

def solution(dice):
    max_value = 0
    answer = []
    
    n = len(dice)
    TEMPLATE = set(range(n))
    
    for case_A in combinations(range(n), n // 2):
        case_A = set(case_A)
        case_B = tuple(TEMPLATE - case_A)
        case_A = tuple(case_A)
    
        selected_A = [dice[i] for i in case_A]
        selected_B = [dice[i] for i in case_B]
    
        data_A = defaultdict(int)
        for values in product(*selected_A):
            data_A[sum(values)] += 1
    
        data_B = defaultdict(int)
        for values in product(*selected_B):
            data_B[sum(values)] += 1
    
        keys_A = list(data_A.keys())
        keys_A.sort()
        keys_B = list(data_B.keys())
        keys_B.sort()
        
        acc_B = [0] * len(keys_B)
        acc_B[0] = data_B[keys_B[0]]
        for i in range(1, len(keys_B)):
            acc_B[i] = acc_B[i-1] + data_B[keys_B[i]]
    
        wins = 0
        sames = 0
        for i in range(len(keys_A)):
            idx = bisect_left(keys_B, keys_A[i])
    
            if idx < len(keys_B):
                if keys_A[i] == keys_B[idx]:
                    sames += data_A[keys_A[i]] * data_B[keys_B[idx]]
            if idx > 0:
                wins += acc_B[idx-1] * data_A[keys_A[i]]
        
        if max_value < wins:
            max_value = wins
            answer = sorted(map(lambda x : x+1, case_A))
    
    return answer