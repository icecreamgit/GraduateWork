import numpy as np
import stands.StandForFourMethods as StandForFourMethods
import stands.StandForDistansesMCD as StandForDistansesMCD


def WriteGrafics(params, mode, modeForGrafic):
    outlier = params["outlier"]
    emissionZones = params["emissionZones"]
    standForFourMethods = StandForFourMethods.StandForFourMethods()
    for emissionZone in emissionZones:
        params["emissionZones"] = emissionZone

        while outlier <= 0.25:
            params["outlier"] = outlier
            standForFourMethods.Main_StandForFourMethods(params, mode, modeForGrafic)
            outlier += 0.05
        outlier = 0.



def main():
    n, tetta, p = 500, np.array([1., 1.5, 2.]), 3
    limit = 1.0
    outlier = 0.25
    nCycle = 100

    # grafic - отображение зависимости кси от выбросов
    # oneOutput - вывод в консоль значений показателей точности оценивания
    # для LS, MCD, M-estimators of Cauchy and Huber
    modeForGrafic = "textOutput" # "textOutput" or "grafic" or "grafic_for_N"

    # Only: "normalModel" "cauchyModel" "exponentModel"
    # For I model (only normal) [[0.01, 0.1, 1, 2], [0.1, 0.25, 2, 3], [0.01, 0.1, 3, 5], [0.1, 0.5, 5., 7.]]
    # emissionZones = [[0.01, 0.1, 3, 5]]
    # mode = "normalModel"

    # For II model (normal + cauchy) [0.01, 0.1, 1, 1], [0.1, 0.25, 1, 1], [0.25, 0.5, 1, 1]
    # emissionZones = [[0.25, 0.5, 1, 1]]
    # mode = "cauchyModel"

    # For III model (normal + exp) [0.01, 0.1, 0.5, 1], [0.1, 0.25, 1, 2], [0.01, 0.1, 2, 5]
    emissionZones = [[0.01, 0.1, 2, 5]]
    mode = "exponentModel"


    standForFourMethods = StandForFourMethods.StandForFourMethods()
    standForDistansesMCD = StandForDistansesMCD.StandForDistansesMCD()

    params = {"n": n, "tetta": tetta, "outlier": outlier, "limit": limit,
              "emissionZones": emissionZones, "nCycle": nCycle}

    WriteGrafics(params, mode, modeForGrafic)

    # for emissionZone in emissionZones:
    #     params["emissionZones"] = emissionZone
    #     standForDistansesMCD.Main_StandForDistansesMCD(params, mode)


    # for emissionZone in emissionZones:
    #     params["emissionZones"] = emissionZone
    #     standForFourMethods.Main_StandForFourMethods(params, mode, modeForGrafic)
        # standForDistansesMCD.Main_StandForDistansesMCD(params)

if __name__ == '__main__':
    main()
