import os
import sys
import random
# with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18RR/type_constrain.txt') as f:
strtypeConstrain = "/Users/ihao/git/ConvKB/ConvKB_pytorch/benchmarks/FB15K237/type_constrain.txt"
# with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18RR/test2id.txt') as f:
strtest = "/Users/ihao/git/ConvKB/ConvKB_pytorch/benchmarks/FB15K237/test2id.txt"
# with open('/Users/ihao/Desktop/wn18rr_data/test2id.txt', 'w+') as f, open('/Users/ihao/Desktop/wn18rr_data/test_index.txt', 'w+') as f2:
strintest = "/Users/ihao/Desktop/ConvKB/FB15K237/test2id.txt"
strtestindex = "/Users/ihao/Desktop/ConvKB/FB15K237/test_index.txt"

def Test():
    type_constraint_head = {}
    type_constraint_tail = {}

    with open(strtypeConstrain) as f:
        for line in f:
            print(line.strip().split('\t')[0])
            print(type_constraint_head.__contains__(line.strip().split('\t')[0]))
            if type_constraint_head.__contains__(line.strip().split('\t')[0]) == False:
                print(line.strip().split('\t')[2:])
                print(line.split('\t')[1:])
                type_constraint_head[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
            else :
                type_constraint_tail[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]

    train2id = []
    icic = 0
    # with open('/Users/ihao/Desktop/OpenKE-OpenKE-PyTorch/benchmarks/WN18RR/test2id.txt') as f:
    with open(strtest) as f:
        for line in f:
            if icic == 0:
                num = line.strip()[0:];
                num = int(num)
                icic += 1
            train = line.strip().split(' ')
            train.append(0)
            train2id.append(train)
    for i in range(int( num*0.5 )) :
        flag = True
        while flag :
            choice = random.randint(1, num)
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
    # with open('/Users/ihao/Desktop/wn18rr_data/test2id.txt', 'w+') as f, open(
            # '/Users/ihao/Desktop/wn18rr_data/test_index.txt', 'w+') as f2:
    with open(strintest, 'w+') as f, open(strtestindex, 'w+') as f2:
        print(len(train2id)-1)
        for i in range(len(train2id)-1):
            print(train2id[i][0])
            print(type(train2id[i][0]))
            if i == 0:
                print(train2id[i][0])
                hrt = str(train2id[i][0]) + '\n'
                f.write(hrt)
                f2.write(hrt)
                continue
            hrt = str(train2id[i][0]) + " " + str(train2id[i][1]) + " " + str(train2id[i][2]) + '\n'
            hrt2 = str(train2id[i][3]) + '\n'
            f.write(hrt)
            f2.write(hrt2)



if __name__ == '__main__':
    Test()