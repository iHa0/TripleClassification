import os
import sys
import random

def Test():
    type_constraint_head = {}
    type_constraint_tail = {}
    with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18RR/type_constrain.txt') as f:
        for line in f:
            # print(type_constraint_head.__contains__(line.strip().split('\t')[0]))
            if type_constraint_head.__contains__(line.strip().split('\t')[0]) == False:
                type_constraint_head[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
            else :
                type_constraint_tail[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]

    train2id = []
    icic = 0
    with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18RR/train2id.txt') as f:
        for line in f:
            if icic == 0:
                num = line.strip()[0:]
                num = int(num)
                icic += 1
            train = line.strip().split(' ')
            train.append(0)
            train2id.append(train)
    #
    #
    # 此处需要修改比例与train的数目
    #
    #

    for i in range(int( num*0.1 )) :
        flag = True
        while flag :
            choice = random.randint(1,num)
            print(i,type(choice),train2id[choice],choice,len(train2id))
            if train2id[choice][3] == 1:
                continue
            seed = random.random()
            if len(type_constraint_head[train2id[choice][2]]) > 0 and len(type_constraint_tail[train2id[choice][2]]) > 0 :
                if seed > 0.5:
                    index_value = random.choice(type_constraint_head[train2id[choice][2]])
                    train2id[choice][0] = index_value
                    train2id[choice][3] = 1
                    flag = False
                else:
                    index_value = random.choice(type_constraint_tail[train2id[choice][2]])
                    train2id[choice][1] = index_value
                    train2id[choice][3] = 1
                    flag = False
            elif len(type_constraint_head[train2id[choice][2]]) > 0:
                index_value = random.choice(type_constraint_head[train2id[choice][2]])
                train2id[choice][0] = index_value
                train2id[choice][3] = 1
                flag = False
            elif len(type_constraint_tail[train2id[choice][2]]) > 0 :
                index_value = random.choice(type_constraint_tail[train2id[choice][2]])
                train2id[choice][1] = index_value
                train2id[choice][3] = 1
                flag = False
    with open('/Users/ihao/Desktop/wn18rr_data/N1N2N3/wn18rr_n1.txt','w+') as f:
        for i in range(len(train2id)-1):
            if i == 0:
                print(train2id[i][0])
                hrt = str(train2id[i][0]) + '\n'
                f.write(hrt)
                continue
            hrt = str(train2id[i][0]) + " " + str(train2id[i][1]) + " " + str(train2id[i][2]) + '\n'
            f.write(hrt)



if __name__ == '__main__':
    Test()