"""
K临近算法
"""

from numpy import *
import operator


def createDateSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    print("dataSetSize:", dataSetSize)
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print("diffMat\n", diffMat)
    sqDiffMat = diffMat ** 2
    print("sqDiffMat\n", sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    print("sqDistances\n", sqDistances)
    distances = sqDistances ** 0.5
    print("distances\n", distances)
    sortedDistIndicies = distances.argsort()
    print("sortedDistIndicies\n", sortedDistIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        print("voteIlabel", i, voteIlabel)
        print("classCount[voteIlabel]", i, classCount[voteIlabel])
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print("sortedClassCount\n", classCount, sortedClassCount)
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDateSet()
    print("group\n", group)
    print("labels\n", labels)
    classify = classify0([0.5, 0], group, labels, 3)
    print("classify:", classify)
