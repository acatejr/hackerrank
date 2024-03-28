def circular_array_rotation(a, k, queries):
    iters = k % len(a)
    data = [(a[-iters:] + a[0:len(a)-iters])[i] for i in queries]
    return data

    # tmp_a = a
    # for i in range(k):
    #     arr = [tmp_a[-1]] + [v for v in tmp_a[0:len(tmp_a)-1]]
    #     tmp_a = arr

    # result = []
    
    # for q in queries:
    #     result.append(tmp_a[q])

    # return result
    
# result = circular_array_rotation([3,4,5], 2, [1,2])
# print(result)

result = circular_array_rotation([1,2,3], 2, [0,1,2])
print(result)
