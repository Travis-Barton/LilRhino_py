#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:30:06 2020

@author: tbarton
"""

import pandas as pd
import sklearn as skl
import numpy as np
from detect_peaks import detect_peaks
from feeder_view_plots import get_feeder_view_plot
import random as rd
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from tqdm import tqdm
from collections import Counter
from statistics import mode
import os
import scipy.stats as stats
import random as rd
from multiprocessing import Pool
import sys_utils as su
import time
import datetime
def codes_done(title = 'Hey Dude', msg = 'Your code is done'):
    os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(msg, title))



def get_pa(wf):
    e_wf_fund, e_wf_fund_pa = get_frequency_content(wf, frequency=60, sample_rate=7812.5)
    e_wf_total = get_total_frequency_content(wf, frequency=60, sample_rate=7812.5)[0]
    e_wf_total_fund = e_wf_total / e_wf_fund
    e_wf_ref_pa = [2 * np.pi * xx * 60 / 7812.5 for xx in range(len(e_wf_fund_pa))]
    e_wf_fund_pa_ref = [norm_angle if norm_angle < 180 else norm_angle - 360
                        for norm_angle in ((e_wf_fund_pa - e_wf_ref_pa - np.pi) % (2 * np.pi)) * 180 / np.pi]
    return e_wf_fund_pa_ref

def delay_print(s, sleep = .1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(sleep)