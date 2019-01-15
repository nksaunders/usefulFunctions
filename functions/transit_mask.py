import numpy as np

def create_planet_mask(time_array, period, t0, duration=0.2):
    '''Returns a boolean mask for a given time. True where planets are not transiting.
    Parameters
    ----------
    time : np.ndarray of JD
        Array of time values at which to compute the mask. Note: Make sure that time is
        in JULIAN DAY.
    period : float
        Period of planet
    t0 : float
        Transit mid point
    duration : float
        Transit duration
    Returns
    -------
    mask : boolean array
        Array where True indicates there is no planet transiting. False indicates a planet is transiting.
    '''
    ph = (time_array - t0)/period % 1
    mask = (ph > ((duration * 1.5)/period)/2) & (ph < 1 - ((duration * 1.5)/period)/2)
    return mask
