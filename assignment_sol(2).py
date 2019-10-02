'''The function at given a list of integers and a number K, return contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''





def solve( s , k):
    arr = s.split()
    output = []
    buffer_arr = []
    buffer_len = -1
    i = 0

    while i < len(arr):
        w = arr[i]
        if len(w) > k:
            print('\n[*] Cannot complete because of this word: "%s"' % w)
            return
        if (len(w) + buffer_len + 1) <= k:
            buffer_len += len(w) + 1
            buffer_arr.append(w)
            i += 1
        else:
            result = ' '.join(buffer_arr)
            output.append(result)
            buffer_arr = []
            buffer_len = -1
    if buffer_arr:
        result = ' '.join(buffer_arr)
        output.append(result)
    return output


# End of solve(...)


input_str=input()
k = int(input())
X = solve(input_str, k)
for s in X:
    print(s)