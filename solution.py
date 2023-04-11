import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if ks_2samp(x, y, alternative="two-sided").pvalue < 0.09:
        return False
    else:
        return True
