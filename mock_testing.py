mu = [255.88, 200.77, 651.95, 198.3,
        198.25, 185.19, 56.66, 9.4, 131.35,
        15.19, 22.74, 22.36, 2.61, 17.86, 23.33, 12.68, 23.59, 26.33, 20.13, 26.49, 20.79, 22.95, 
        20.36, 32.77, 19.72, 11.22, 9.9, 13.5]

sigma = [17.16, 16.58, 46.17, 16.3, 
        32.22, 25.05, 16.41, 2.11, 12.38,
        1.84, 2.17, 2.24, 2.35, 2.88, 2.03, 1.22, 1.83, 5.17, 1.44, 3.5, 2.53, 2.51, 
        3.79, 2.11, 3.56, 1.94, 8.89, 1.49]

cols = ['PLT', 'WBC', 'RBC', 'HGB', 
        'MCV', 'MCH', 'MCHC', 'RDW', 'ALYM',
        'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D2', 'D3', 'DGR', 'E1', 'E2.ICU', 'E29.ICU', 'E3', 
        'F3', 'FGR', 'G1', 'G2P', 'H1', 'H2']


if len(cols) == len(sigma) and len(cols) == len(mu):
    print(True)

print(len(mu)), print(len(sigma)), print(len(cols))