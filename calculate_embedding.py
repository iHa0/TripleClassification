import os
import sys
import random
import numpy as np

def Test():
    ent = np.zeros([40943, 100])
    rel = np.zeros([11, 100])
    e1n = np.ones([1, 100])
    en1 = np.ones([100, 1])
    arr_judge = np.zeros([3034 - 1, 3])
    valid=[]
    n=0
    ent_i = 0
    train2id = []
    # / Users / ihao / Desktop / embeded / ent_new.txt
    with open('/Users/ihao/Desktop/wn18rr_data/N1_0.01/ent_new.txt') as f:
        nn = 0
        for line in f:
            n = 0
            nn += 1
            while n < 100:
                ent[ent_i][n] = line.strip().split(', ')[n]
                n += 1
            ent_i += 1
            print('============')
            print(nn)
    ii=0
    # / Users / ihao / Desktop / embeded / rel_new.txt
    with open('/Users/ihao/Desktop/wn18rr_data/N1_0.01/rel_new.txt') as f2:
        for line in f2:
            n = 0
            while n < 100:
                rel[ii][n] = line.strip().split(', ')[n]
                n += 1
            ii += 1
    split_n = 0
    split_n1 = 0
    split_n2 = 0
    out = []
    nor = []
    iio = 0
    icount = 0
    with open('/Users/ihao/Desktop/wn18rr_data/vaild2id.txt') as vaild :
        # with open('/Users/ihao/Desktop/FB15k237-embedding/valid2id.txt') as vaild, open(
        #         '/Users/ihao/Desktop/FB15k237-embedding/n1_embeded/valid_index&num.txt', 'w+') as validout:
        for line in vaild:
            if iio == 0:
                # numm = line.strip()[0:]
                # numm = int(numm)
                iio += 1
                continue
            n = 0
            # arr_judge = np.zeros([numm, 3])
            # count = 0
            #split_n => h
            split_n = int(line.strip().split(' ')[0])
            #split_n1 => t
            split_n1 = int(line.strip().split(' ')[1])
            # split_n2 => r
            split_n2 = int(line.strip().split(' ')[2])
            f = ent[split_n]+rel[split_n2]-ent[split_n1]
            # print(f.dtype)
            # print(f.shape)
            # print(f.ndim)
            # print(f)
            f = np.array(f)
            f = f.reshape(1, -1)
            # print(f.dtype)
            # print(f.shape)
            # print(f.ndim)
            # print(f)
            nor_x = np.linalg.norm(f)
            arr_judge[icount][0] = nor_x
            # f=||h+r-t|| ==> nor_x
            print(nor_x)
            # hrt = str(nor_x) + "\n"
            # 将nor_x 写入文件
            # validout.write(hrt)
            # print(count)
            # count += 1
            icount += 1
    vaild_indexn = 0
    vaild_count = 0
    with open('/Users/ihao/Desktop/wn18rr_data/valid_index.txt') as vaild_index:
        for linee in vaild_index:
            if vaild_indexn == 0:
                vaild_indexn += 1
                continue
            arr_judge[vaild_count][1] = int(linee.strip()[0:])
            vaild_count += 1
    print(arr_judge)
    max_index = np.argmax(arr_judge, axis=0)[0]
    max_num = arr_judge[max_index][0]
    min_index = np.argmin(arr_judge, axis=0)[0]
    min_num = arr_judge[min_index][0]
    leng = arr_judge[:, 0].size
    print(leng)
    inn = 0
    maxIndex = 0
    countii = 0
    maxN = 0
    while min_num < max_num :
        print(min_num)
        countii = 0
        for inn in range(int(leng)) :
            if arr_judge[inn][0] < min_num:
                arr_judge[inn][2] = 0
            else:
                arr_judge[inn][2] = 1
            if int(arr_judge[inn][1]) == int(arr_judge[inn][2]):
                countii += 1
        if maxN < countii /leng :
            maxN = countii / leng
            maxIndex = min_num
        min_num += 0.1
    print(maxN)
    print(maxIndex)

    inn = 0
    countii = 0
    minn = maxIndex - 0.1
    maxx = maxIndex + 0.1
    while minn < maxx :
        print(minn)
        countii = 0
        for inn in range(int(leng)) :
            if arr_judge[inn][0] < minn:
                arr_judge[inn][2] = 0
            else:
                arr_judge[inn][2] = 1
            if int(arr_judge[inn][1]) == int(arr_judge[inn][2]):
                countii += 1
        if maxN < countii / leng:
            maxN = countii / leng
            maxIndex = minn
        minn += 0.0001
    print(maxN)
    print(maxIndex)












if __name__ == '__main__':
    Test()