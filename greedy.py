# 거스름돈 그리디

# N=1260
# count=0

# coin=[500,100,50,10]

# for c in coin:
#     count += N // c
#     N %= c


# print(count)



# 큰 수의 법칙

# a,m,k = map(int,input().split())
# j = list(map(int, input().split()))

# j.sort()
# first = j[a-1]  # 가장 큰 수
# second = j[a-2]  # 두번째로 큰 수

# cnt = 0

# # 가장 큰 수가 더해지는 횟수 
# count = int(m / (k+1)) * k  
# count += m % (k+1)  
# print(count)

# # 가장 큰 수 / 두번째로 큰 수를 곱해서 저장함
# cnt += (count) * first
# cnt += (m-count) * second

# print(cnt)

# 일반 풀이
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         cnt += first
#         m-=1
    
#     if m == 0:
#         break
#     cnt += second
#     m -= 1

# print(cnt)


# 숫자 카드 게임

# a,b = map(int, input().split())

# cnt = 0

# for i in range(a):
#     n = list(map(int, input().split()))
#     # 현재 줄에서 가장 작은 수 찾기
#     minv = min(n)
#     # 가장 작은 수들 중에서 가장 큰 수 찾기
#     cnt = max(cnt, minv)

# print(cnt)

# 2중 반복문 구조 사용 예시

# for i in range(a):
#     n = list(map(int, input().split()))
#     # 현재 줄에서 가장 작은 수 찾기
#     minv = 10001
#     for j in n:
#         minv = min(minv, j)
#         print(minv,j)
#     # 가장 작은 수들 중에서 가장 큰 수 찾기
#     cnt = max(cnt, minv)

# print(cnt)

n,k = map(int, input().split())
cnt = 0

# while n >= k:

#     while n % k != 0:
#         n -= 1
#         cnt += 1
#     # k로 나누기
#     n //= k
#     cnt += 1

# print(cnt)

# while n > 1:
#     n-=1
#     cnt+=1

# print(cnt)

while True:
    # (n == k 로 나누어 떨어지는 수) 가 될 때까지 1씩 빼기
    target = (n//k) * k
    cnt += (n-target)
    n = target

    # n이 k 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    
    cnt+=1
    n//k
    # k로 나누기
   
# 마지막으로 남은 수에 대하여 1씩 빼기
cnt+=(n-1)
print(cnt)
