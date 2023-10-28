import matplotlib.pyplot as plt
import numpy as np


def calculateYwithoutError(t, x1, x2, size):
    y_ = np.zeros((size, ))
    for i in range(size):
        y_[i] = t[0] + t[1] * x1[i] + t[2] * x2[i]
    return y_

def Painting(x, y):
    fig, axes = plt.subplots()
    axes.scatter(x, y, c='green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

def ylinealModel(n, tetta, outlier):
    # Search y without observation error
    x1 = sorted(np.random.uniform(0., 10., n))
    x2 = sorted(np.random.uniform(0., 10., n))

    y = calculateYwithoutError(tetta, x1, x2, n)
    xall = []

    # Search observation error
    e = np.random.binomial(n=1., p=(1 - outlier), size=n)

    counter = 0
    for i in e:
        if i == 0:
            counter += 1

    # Search y_res:
    varMainObservations = 0.01
    varEmissions = 5.
    y_res = np.zeros((n,))

    for i in range(n):
        if e[i] == 1:
            y_res[i] = y[i] + np.random.normal(0, np.sqrt(varMainObservations))
        else:
            y_res[i] = y[i] + np.random.normal(0, np.sqrt(varEmissions))
    for i in range(n):
        xall.append(x1[i])
    for i in range(n):
        xall.append(x2[i])
    return y_res, xall

def lineToColum(x, n, tetta):
    # Преобразование входной строки x в матрицу
    nTetta = len(tetta) - 1
    xnew = np.zeros((nTetta, n))
    counterDel = 0
    for stepi in range(nTetta):
        for stepj in range(n):
            xnew[stepi][stepj] = x[counterDel]
            counterDel += 1
    return xnew

def LMSMatrix(x, y):
    return np.dot((np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose())), y)

def filingMatrixX(x, xall, tetta):
    nTetta = len(tetta)
    n = len(x[0])
    for stepi in range(n):
        x[0][stepi] = 1.
    for stepi in range(1, nTetta):
        for stepj in range(n):
            x[stepi][stepj] = xall[stepi - 1][stepj]
    return x.transpose()

def relativeError(tettaTrue, tettanew):
    n, counter = len(tettaTrue), 0
    for stepi in range(n):
        counter += pow((tettaTrue[stepi] - tettanew[stepi]), 2) / pow(tettaTrue[stepi], 2)
    return counter
def T0(xMassive, j, h):
    mean = 0
    for value in xMassive:
        mean += value[j]
    return mean / h
def MCD(X, n):
    p = 2
    B, xInterm, di = [], [[], []], []
    mean_X0, mean_X1, count = 0, 0, 0

    while 1:
        h = int((n + p + 1) / 2)
        for line in xInterm:
            count += 1
            for i in range(h):
                line.append(X[i][count])

        data = np.array([xInterm[0], xInterm[1]])
        S = np.cov(data, bias=True)

        if np.linalg.det(S) == 0:
            print("det(S) == 0!")
            break

        mean_X0 = T0(xInterm, 0, h)
        mean_X1 = T0(xInterm, 1, h)
        for i in range(h):
            B.append([[xInterm[0][i] - mean_X0], [xInterm[1][i] - mean_X1]])

        for i in range(h):
            a = np.dot(np.array(B[i]).transpose(), pow(S, -1))
            di.append(np.dot(a, np.array(B[i]))[0][0])
        xInterm.clear()
    return 0
def main():
    n, tetta, tettaNew = 10, np.array([1., 1.5, 2.]), np.array([0., 0., 0.])

    Outlier = 0.

    yTrue, xAll = ylinealModel(n=n, tetta=tetta, outlier=Outlier)
    X = np.zeros((len(tetta), n))
    X = filingMatrixX(X, lineToColum(xAll, n, tetta), tetta)
    MCD(X, n)
    tettaNew = LMSMatrix(X, yTrue.reshape(n, 1))
    print("\nOutlier = ", Outlier*100,"%", "\ntetta:\n", tettaNew)
    print("\nОтносительная ошибка:\n", relativeError(tettaTrue=tetta, tettanew=tettaNew))
    Outlier += 0.05

if __name__ == '__main__':
    main()

