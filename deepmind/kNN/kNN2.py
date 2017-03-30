"""
使用k-近邻算法尝试改进约会网站的配对效果
"""

from numpy import *
import operator

import matplotlib
import matplotlib.pylab as plt


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('    ')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(float(listFromLine[-1])))
        index += 1
    return returnMat, classLabelVector


def draw():
    datingDataMat, datgingLabels = file2matrix("data_test/datingtestSet.txt")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datgingLabels), 15.0 * array(datgingLabels))
    plt.show()


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataset = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


if __name__ == '__main__':
    datingDataMat, datgingLabels = file2matrix("data_test/datingtestSet.txt")
    print("datingDataMat\n", datingDataMat)
    print("datgingLabels\n", datgingLabels)
    # draw()
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    print("normDataSet\n", normDataSet)
    print("ranges\n", ranges)
    print("minVals\n", minVals)

