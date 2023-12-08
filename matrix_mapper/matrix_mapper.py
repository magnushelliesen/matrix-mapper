import numpy as np


def matrix_mapper(X: np.ndarray, n: int, m: int):
    """
    Function that maps one matrix X to another x
    """
    N, M = X.shape
    
    # Get number of rows and columns to remove
    N_mod_n = N % n
    M_mod_m = M % m

    # Determine how many to the left/right/top/bottom
    N_mod_n_div2, N_mod_n_mod2 = divmod(N_mod_n, 2)
    M_mod_m_div2, M_mod_m_mod2 = divmod(M_mod_m, 2)

    remove_t = N_mod_n_div2
    remove_b = N_mod_n_div2+N_mod_n_mod2
    remove_l = M_mod_m_div2
    remove_r = M_mod_m_div2+M_mod_m_mod2

    # Pretty sure i can do kindof a quadratic, Q'XQ --> x
    
    return X[remove_t:-remove_b, remove_l:-remove_r]