# 이진 탐색 알고리즘

def search(arr, target, start, end): # 반복문을 이용할 경우
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

def search(arr, target, start, end): # 재귀를 이용할 경우
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return search(arr, target, start, mid-1)
    else:
        return search(arr, target, mid+1, end)