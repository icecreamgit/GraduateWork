import numpy as np

class NormalModel:
    def __calculateYwithoutError(self, t, x1, x2, size):
        y_ = np.zeros((size,))
        for i in range(size):
            y_[i] = t[0] + t[1] * x1[i] + t[2] * x2[i]

        return y_
    def Main_normalModel(self, params):
        # n, tetta, outlier, limit, emissionZones
        n = params["n"]
        tetta = params["tetta"]
        outlier = params["outlier"]
        limit = params["limit"]
        emissionZones = params["emissionZones"]

        # Search y without observation error
        x1 = np.random.uniform(0., limit, n)
        x2 = np.random.uniform(0., limit, n)

        y = self.__calculateYwithoutError(tetta, x1, x2, n)
        xall = [[], []]

        # Search observation error
        y_res = []

        for i in range(n):
            if x1[i] < 0.5 and x2[i] > 0.5:
                # I zone
                y_res.append(y[i] + np.random.normal(loc=0, scale=np.sqrt(emissionZones[0])))
            elif x1[i] <= 0.5 and x2[i] <= 0.5:
                # II zone
                y_res.append(y[i] + np.random.normal(loc=0, scale=np.sqrt(emissionZones[1])))
            elif x1[i] > 0.5 and x2[i] > 0.5:
                # III zone
                y_res.append(y[i] + np.random.normal(loc=0, scale=np.sqrt(emissionZones[2])))
            elif x1[i] > 0.5 and x2[i] < 0.5:
                # IV zone
                y_res.append(y[i] + np.random.normal(loc=0, scale=np.sqrt(emissionZones[3])))

        for i in range(n):
            xall[0].append(x1[i])
            xall[1].append(x2[i])
        y_res = np.array(y_res).reshape(n, 1)

        return y_res, xall