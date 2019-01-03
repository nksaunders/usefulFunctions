import numpy as np
from astropy.stats import bls

def find_best_period(time, flux, dur=.2):
    '''
    A quick helper function to generate a Box Least Squares (BLS) periodogram
    for a given light curve and calculate the period with the highest BLS power.
    '''

    periodogram = bls.BoxLeastSquares(time, flux).autopower(dur)
    best_period = periodogram.period[np.argmax(periodogram.power)]

    return best_period
