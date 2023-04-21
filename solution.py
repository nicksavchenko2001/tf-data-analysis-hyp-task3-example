import pandas as pd
import numpy as np


chat_id = 781119239 # Ваш chat ID, не меняйте название переменной

def solution(x, y):
    p_value = mannwhitneyu(x, y, alternative='less').pvalue
    return p_value < 0.07
