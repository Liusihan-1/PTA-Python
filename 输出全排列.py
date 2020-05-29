def permutations(n):
    indices = list(range(1,n+1))
    for i in range(0,n):
        print(indices[i],end="")
    print("")
    while True:
        low_index = n-1
        while low_index > 0 and indices[low_index-1] > indices[low_index]:
            low_index -= 1
        if low_index == 0:
            break
        low_index -= 1
        high_index = low_index+1
        while high_index < n and indices[high_index] > indices[low_index]:
            high_index += 1
        high_index -= 1
        indices[low_index], indices[high_index] = indices[
            high_index], indices[low_index]
        indices[low_index+1:] = reversed(indices[low_index+1:])
        for i in range(0, n):
            print(indices[i], end="")
        print("")
n=int(input())
permutations(n)
