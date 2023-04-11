import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from hyppo.ksample import Energy, MMD, DISCO

chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if MMD(compute_kernel="laplacian", gamma=1).test(x, y)[1] > 0.09:
        return False
    else:
        return True
