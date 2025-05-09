def bright(rgb, intensity: float):
    return tuple([int(min(max(color * (1 + intensity), 0), 255)) for color in rgb])

# arr = [[0] * 3 for _ in range(4)]
#
# print(arr)
#
# for i in range(4):
#     for j in range(3):
#         arr[i][j] += 1
#         print(i, j, arr)
#
