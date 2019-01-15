from astroquery.mast import Observations
from astropy.table import join

def mast_query(target, radius=0):
    """
    Function to query mast and return all available information about the desired target.
    """
    obs = Observations.query_criteria(target_name=target, radius=radius)
    products = Observations.get_product_list(obs)

    return join(obs, products)
