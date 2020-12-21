import os
import sys
import random
import numpy as np


strent = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/ent.txt"
strentnew = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/ent_new.txt"
strrel = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/rel.txt"
strrelnew = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/rel_new.txt"
strent_new = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/ent_new.txt"
strrel_new = "/Users/ihao/Desktop/ConvKB/WN18RR/n2/rel_new.txt"
strvalid2id = "/Users/ihao/Desktop/ConvKB/WN18RR/test2id.txt"
strvalidIndex = "/Users/ihao/Desktop/ConvKB/WN18RR/test_index.txt"
# 有多少列
LIE = 50
# ent 的数量
ENTNUM = 40943
# rel 的数量
RELNUM = 11
# valid/test 的数量（WN18RR.valid==3034,WN18RR.test==3134）(WN18.valid&test == 5000)
VALIDTESTN = 3134

def Test():
    # count12 = 0
    f12 = open(strent, 'r')
    f22 = open(strentnew, 'w')
    for line in f12:
        f22.write(line.replace('], [', '\n'))
        # count12 += 1
    # print(count12)
    # print('=======')
    f12.close()
    f22.close()
    f122 = open(strrel, 'r')
    f222 = open(strrelnew, 'w')
    for line in f122:
        f222.write(line.replace('], [', '\n'))
        # count12 += 1
    # print(count12)
    # print('=======')
    f122.close()
    f222.close()
    # 以下五个np.array需要修改值
    ent = np.zeros([ENTNUM, LIE])
    rel = np.zeros([RELNUM, LIE])
    e1n = np.ones([1, LIE])
    en1 = np.ones([LIE, 1])
    arr_judge = np.zeros([VALIDTESTN - 1, 3])
    valid=[]
    n=0
    ent_i = 0
    train2id = []
    # /Users/ihao/Desktop/embeded/ent_new.txt
    with open(strent_new) as f:
        nn = 0
        for line in f:
            n = 0
            nn += 1
            while n < LIE:
                ent[ent_i][n] = line.strip().split(', ')[n]
                n += 1
            ent_i += 1
            print('============')
            print(nn)
    ii=0
    # / Users / ihao / Desktop / embeded / rel_new.txt
    with open(strrel_new) as f2:
        for line in f2:
            n = 0
            while n < LIE:
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
    with open(strvalid2id) as vaild:
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
    # with open('/Users/ihao/Desktop/wn18rr_data/valid_index.txt') as vaild_index:
    with open(strvalidIndex) as vaild_index:
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

    print("==========%===========")
    print(maxN)
    print("==========%===========")
    print(maxIndex)












if __name__ == '__main__':
    Test()