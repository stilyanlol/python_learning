n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n + 1):

    num = int(input())

    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")
