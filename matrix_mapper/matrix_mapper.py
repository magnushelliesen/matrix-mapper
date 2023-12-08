import numpy as np


def matrix_mapper(X: np.ndarray, n: int, m: int):
    """
    Function that maps one matrix X to another x
    """
    N, M = X.shape
    
    # Get number of rows and columns to remove
    N_div_n, N_mod_n = divmod(N, n)
    M_div_m, M_mod_m = divmod(M, m)

    # Determine how many to the left/right/top/bottom
    N_mod_n_div_2, N_mod_n_mod_2 = divmod(N_mod_n, 2)
    M_mod_m_div_2, M_mod_m_mod_2 = divmod(M_mod_m, 2)

    remove_t = N_mod_n_div_2
    remove_b = N_mod_n_div_2+N_mod_n_mod_2
    remove_l = M_mod_m_div_2
    remove_r = M_mod_m_div_2+M_mod_m_mod_2

    # Return P'XQ
    return (
        np.repeat(np.eye(n), N_div_n, axis=0).T
        .dot(X[remove_t:N-remove_b, remove_l:M-remove_r])
        .dot(np.repeat(np.eye(m), M_div_m, axis=0))
        /(N_div_n*M_div_m)
    )