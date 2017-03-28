"""
使用k-近邻算法尝试改进约会网站的配对效果
"""

from numpy import *
import operator


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


if __name__ == '__main__':
    datingDataMat, datgingLabels = file2matrix("data_test/datingtestSet.txt")
    print()