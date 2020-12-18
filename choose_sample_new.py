import os
import sys
import random
import numpy as np
import pandas as pd
import xlrd
from pandas import Series, DataFrame


def Test():
    # 超参数设置
    r1 = 0.5

    train = {}
    test = {}
    cc = 0;
    ccc = 0;
    flag = 1
    count = 0
    df_count = 0
    # 初始化存储array
    # 初始化array为-1，列数为100
    store = np.arange(1000)
    ii = 0
    n = 0
    for iii in store:
        store[ii] = -1
        ii += 1

    # start    计算函数的数据
    # ent代表实体，rel代表关系
    ent = np.zeros([40943, 100])
    rel = np.zeros([18, 100])
    e1n = np.ones([1, 100])
    en1 = np.ones([100, 1])
    valid = []
    n = 0
    ent_i = 0
    train2id = []
    # end

    # 读取所有的embedding并将它放入数组中
    with open('/Users/ihao/Desktop/entity2vec_wn18.txt') as f:
        nn = 0
        for line in f:
            n = 0
            nn += 1
            # =========此处要修改n的值为列数=========
            while n < 100:
                ent[ent_i][n] = line.strip().split('\t')[n]
                n += 1
            ent_i += 1
            print('============')
            print(nn)
    iii = 0
    # / Users / ihao / Desktop / embeded / rel_new.txt
    with open('/Users/ihao/Desktop/relation2vec_wn18.txt') as f2:
        for line in f2:
            n = 0
            # =========此处要修改n的值为列数=========
            while n < 100:
                rel[iii][n] = line.strip().split('\t')[n]
                n += 1
            iii += 1
    split_n = 0
    split_n1 = 0
    split_n2 = 0
    out = []
    nor = []
    df_n = 0
    n = 0

    # df = pd.read_excel('/Users/ihao/Desktop/fb15k237Store.xlsx', sheet_name='Sheet1', na_values='n/a')
    # df_t = pd.read_excel('/Users/ihao/Desktop/fb15k237Store.xlsx', sheet_name='test', na_values='n/a')

    fenmu = 0
    # 为了求afax的分母
    # =========此处要修改路径=========
    # with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/test2id.txt') as test2id9:
    with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/test2id.txt') as test2id9:
        # 直接遍历test2id中的前100个三元组
        for test_line in test2id9:
            flag = 1
            ccc = 0
            # 忽略掉第一行的行数值
            if cc == 0:
                cc += 1
                continue
            # 如果到了100个，就退出
            if count == 99:
                break
            dd = 0
            # 进入train2id中查找
            # =========此处要修改路径=========
            # with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/train2id.txt') as t2id9, open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/train2id.txt') as t2id29:
            with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/train2id.txt') as t2id9, open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/train2id.txt') as t2id29:
                for train_line in t2id9:
                    if dd == 0:
                        dd += 1
                        continue
                    #     如果相等，说明在 train2id 中的值在 test2id 中出现过
                    if (test_line.split(' ')[0:]) == (train_line.split(' ')[0:]):
                        flag = 0
                        continue
                #  说明test在train中还没有出现过
                if flag == 1:
                    head_in_100 = int(test_line.split(' ')[0])
                    # 判断是否出现过 head
                    if (store == head_in_100).any():
                        # 出现过则直接跳过
                        continue
                    else:
                        # 未出现，则进行下一步操作
                        df_t_n = 0
                        iiii = 0
                        for check_line in t2id29:
                            # 跳过首行的行数值
                            if df_t_n == 0:
                                df_t_n += 1
                                continue
                            # icount = 0
                            # 在train2id中查找head相同的值
                            if int(check_line.split(' ')[0]) == head_in_100:
                                df_inh = int(check_line.split(' ')[0])
                                df_int = int(check_line.strip().split(' ')[1])
                                df_inr = int(check_line.strip().split(' ')[2])
                                # 求出 (h1*r1-t1)^2 的值，相加，最后开平方
                                fenmu += np.power(ent[df_inh] * rel[df_inr] - ent[df_int], 2)
                                print(fenmu)
            count += 1

    # 对分母开根号，得到想要的值
    fenmu = np.sqrt(fenmu)
    # 将计数器还原
    count = 0
    cc = 0
    # =========此处要修改路径=========
    # with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/test2id.txt') as test2id, open(
    #             '/Users/ihao/Desktop/sample_out.txt', 'w+') as outp:
    with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/test2id.txt') as test2id, open(
            '/Users/ihao/Desktop/sample_out_wn18.txt', 'w+') as outp:
        # 直接遍历test2id中的前100个三元组
        for test_line in test2id:
            flag = 1
            ccc = 0
            # 忽略掉第一行的行数值
            if cc == 0:
                cc += 1
                continue
            # 如果到了100个，就退出
            if count == 99:
                break
            dd = 0
            # 进入train2id中查找
            # =========此处要修改路径=========
            # with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/train2id.txt') as t2id, open(
            #                 '/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/FB15K237/train2id.txt') as t2id2:
            with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/train2id.txt') as t2id, open(
                '/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18/train2id.txt') as t2id2:
                for train_line in t2id:
                    if dd == 0:
                        dd += 1
                        continue
                    #     如果相等，说明在 train2id 中的值在 test2id 中出现过
                    if (test_line.split(' ')[0:]) == (train_line.split(' ')[0:]):
                        flag = 0
                        continue
                #  说明test在train中还没有出现过
                if flag == 1:
                    # hrt = str(test_line.split(' ')[0]) + ' ' + str(test_line.strip().split(' ')[1]) + ' ' + str(
                    #     test_line.strip().split(' ')[2])
                    head_in_100 = int(test_line.split(' ')[0])
                    # print((a == 999).any())
                    # 判断是否出现过 head
                    if (store == head_in_100).any():
                        # 出现过则直接跳过
                        continue
                    else:
                        # 未出现，则进行下一步操作
                        df_t_n = 0
                        iiii = 0
                        for check_line in t2id2:
                            # 跳过首行的行数值
                            if df_t_n == 0:
                                df_t_n += 1
                                continue
                            # icount = 0
                            # 在train2id中查找head相同的值
                            if int(check_line.split(' ')[0]) == head_in_100:
                                df_inh = int(check_line.split(' ')[0])
                                df_int = int(check_line.strip().split(' ')[1])
                                df_inr = int(check_line.strip().split(' ')[2])
                                # 使用excel作为容器，但是考虑后还是np.array好
                                # df_t['ht'][icount] = check_line.split(' ')[0]
                                # df_t['tt'][icount] = check_line.strip().split(' ')[1]
                                # df_t['rt'][icount] = check_line.strip().split(' ')[2]
                                # df_t['point'][0] = calculate(df_inh, df_int, df_inr)
                                # 查找对应的 embedding 值
                                # f = ent[df_inh] + rel[df_inr] - ent[df_int]
                                # (hi*ri-ti)*ri
                                f = (ent[df_inh] * rel[df_inr] - ent[df_int]) * rel[df_inr]
                                f = np.array(f)
                                f = f.reshape(1, -1)
                                nor_x = np.linalg.norm(f)
                                # nor_x = np.sqrt(f.dot(f.T))
                                # f=||h+r-t|| ==> nor_x
                                # print(nor_x)
                                # hrt = str(nor_x) + "\n"
                                # 将nor_x 写入文件
                                # validout.write(hrt)
                                # 对 f 求偏导
                                ratio = f
                                # ratio1 = np.sqrt(f.dot(f.T))
                                afax = ratio / fenmu
                                # print(afax)
                                f2 = (ent[df_inh] + afax) + rel[df_inr] - ent[df_int]
                                f2 = np.array(f2)
                                f2 = f2.reshape(1, -1)
                                nor_x2 = np.linalg.norm(f2)
                                # nor_x2 = np.sqrt(f2.dot(f2.T))
                                n_hrt = float(-(nor_x - r1 * nor_x2))
                                # df_t['point'][icount] = n_hrt
                                #
                                # 改进--使用array
                                # 将三元组都存储到np.array中
                                if iiii == 0:
                                    arr = np.array([[df_inh, df_int, df_inr, n_hrt]])
                                    iiii += 1
                                else:
                                    arr = np.append(arr, [[df_inh, df_int, df_inr, n_hrt]], axis=0)

                                # icount += 1
                        # df_t.sort_values('point', ascending=False)
                        # 将元素降序排列
                        if len(arr) != 0:
                            sort_arr = arr[arr[:, 3].argsort()[::-1]]
                        lin_n = 0
                        for lin in sort_arr:
                            # 直接忽略前面5个，相当于删除了
                            if lin_n < 5:
                                lin_n += 1
                                continue
                            # 写入到 txt
                            str_out = str(int(lin[0])) + ' ' + str(int(lin[1])) + ' ' + str(int(lin[2])) + ' ' + str(
                                lin[3]) + '\n'
                            print(str_out)
                            outp.write(str_out)
                        arr = ''
                        sort_arr = ''
                        store[n] = head_in_100
                        n += 1
                        print(n)
            count += 1


if __name__ == '__main__':
    Test()
