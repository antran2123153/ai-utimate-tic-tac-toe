SCORE_1 = 6
SCORE_2 = 8
SCORE_3 = 10
SCORE_4 = 12

SCORE_WIN_BLOCK = 2000

def scoreBlock(block):
    for (i, j, k) in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,6,4)]:
        if block[i] == block[j] == block[k] == 1:
            return SCORE_WIN_BLOCK
        
    for (i, j, k) in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,6,4)]:
        if block[i] == block[j] == block[k] == 2:
            return -SCORE_WIN_BLOCK
        
    score = 0
    
    if block[0] == 1:
        score += SCORE_1
    if block[2] == 1:
        score += SCORE_1
    if block[6] == 1:
        score += SCORE_1
    if block[8] == 1:
        score += SCORE_1
        
    if block[1] == 1:
        score += SCORE_2
    if block[3] == 1:
        score += SCORE_2
    if block[5] == 1:
        score += SCORE_2
    if block[7] == 1:
        score += SCORE_2
        
    if block[4] == 1:
        score += SCORE_3
        
    if (block[0] == block[1] == 1 and block[2] == 0) or (block[1] == block[2] == 1 and block[0] == 0) or (block[0] == block[2] == 1 and block[1] == 0):
        score += SCORE_4
    if (block[3] == block[4] == 1 and block[5] == 0) or (block[4] == block[5] == 1 and block[3] == 0) or (block[3] == block[5] == 1 and block[4] == 0):
        score += SCORE_4
    if (block[6] == block[7] == 1 and block[8] == 0) or (block[7] == block[8] == 1 and block[6] == 0) or (block[6] == block[8] == 1 and block[7] == 0):
        score += SCORE_4
    if (block[0] == block[3] == 1 and block[6] == 0) or (block[3] == block[6] == 1 and block[0] == 0) or (block[0] == block[6] == 1 and block[3] == 0):
        score += SCORE_4
    if (block[1] == block[4] == 1 and block[7] == 0) or (block[4] == block[7] == 1 and block[1] == 0) or (block[1] == block[7] == 1 and block[4] == 0):
        score += SCORE_4
    if (block[2] == block[5] == 1 and block[8] == 0) or (block[5] == block[8] == 1 and block[2] == 0) or (block[2] == block[8] == 1 and block[5] == 0):
        score += SCORE_4
    if (block[0] == block[4] == 1 and block[8] == 0) or (block[4] == block[8] == 1 and block[0] == 0) or (block[0] == block[8] == 1 and block[4] == 0):
        score += SCORE_4
    if (block[2] == block[4] == 1 and block[6] == 0) or (block[4] == block[6] == 1 and block[2] == 0) or (block[2] == block[6] == 1 and block[4] == 0):
        score += SCORE_4
        
        
        
    if block[0] == 2:
        score -= SCORE_1
    if block[2] == 2:
        score -= SCORE_1
    if block[6] == 2:
        score -= SCORE_1
    if block[8] == 2:
        score -= SCORE_1
        
    if block[1] == 2:
        score -= SCORE_2
    if block[3] == 2:
        score -= SCORE_2
    if block[5] == 2:
        score -= SCORE_2
    if block[7] == 2:
        score -= SCORE_2
        
    if block[4] == 2:
        score -= SCORE_3
        
    if (block[0] == block[1] == 2 and block[2] == 0) or (block[1] == block[2] == 2 and block[0] == 0) or (block[0] == block[2] == 2 and block[1] == 0):
        score -= SCORE_4
    if (block[3] == block[4] == 2 and block[5] == 0) or (block[4] == block[5] == 2 and block[3] == 0) or (block[3] == block[5] == 2 and block[4] == 0):
        score -= SCORE_4
    if (block[6] == block[7] == 2 and block[8] == 0) or (block[7] == block[8] == 2 and block[6] == 0) or (block[6] == block[8] == 2 and block[7] == 0):
        score -= SCORE_4
    if (block[0] == block[3] == 2 and block[6] == 0) or (block[3] == block[6] == 2 and block[0] == 0) or (block[0] == block[6] == 2 and block[3] == 0):
        score -= SCORE_4
    if (block[1] == block[4] == 2 and block[7] == 0) or (block[4] == block[7] == 2 and block[1] == 0) or (block[1] == block[7] == 2 and block[4] == 0):
        score -= SCORE_4
    if (block[2] == block[5] == 2 and block[8] == 0) or (block[5] == block[8] == 2 and block[2] == 0) or (block[2] == block[8] == 2 and block[5] == 0):
        score -= SCORE_4
    if (block[0] == block[4] == 2 and block[8] == 0) or (block[4] == block[8] == 2 and block[0] == 0) or (block[0] == block[8] == 2 and block[4] == 0):
        score -= SCORE_4
    if (block[2] == block[4] == 2 and block[6] == 0) or (block[4] == block[6] == 2 and block[2] == 0) or (block[2] == block[6] == 2 and block[4] == 0):
        score -= SCORE_4

        
        
    return score



with open("data.txt", "w") as f:
    f.write("data = { ")
    for i1 in range(3):
        arr = [0,0,0,0,0,0,0,0,0]
        arr[0] = i1
        for i2 in range(3):
            arr[1] = i2
            for i3 in range(3):
                arr[2] = i3
                for i4 in range(3):
                    arr[3] = i4
                    for i5 in range(3):
                        arr[4] = i5
                        for i6 in range(3):
                            arr[5] = i6
                            for i7 in range(3):
                                arr[6] = i7
                                for i8 in range(3):
                                    arr[7] = i8
                                    for i9 in range(3):
                                        arr[8] = i9
                                        f.write('"')
                                        f.write(''.join([str(elem) for elem in arr]))
                                        f.write('"')
                                        f.write(" : ")
                                        f.write(str(scoreBlock(arr)))
                                        f.write(", ")
    f.write(" }")

