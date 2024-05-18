import cvxpy as cp
import numpy as np

def gamma_exact(budget, c_x, v_s, functions):
    """
    function to compute gamma for given costs, points and values
    optimization task:

    min gamma
    s.t.  c_b^T x <= budget
          ||clip(x, x_i, f_i)|| <= gamma v_i / L_i
    
    Arguments:
        budget --
        c_x: vector of costs if x
        x_s: list of x_i
        v_s: list of v_i
        L_s: list of L_i
        clip_functions: list of clip functions. clip_functions_i = f(x,y, f_i)

        we do not provide f_i to function for demonstrative purposes
    """
    m = v_s.shape[0]
    n = len(c_x)
    gamma = cp.Variable()
    x = cp.Variable(n)

    constraints = [x @ c_x <= budget, 0. <= x, 0 <= gamma] 

    for i, v_i, in zip(range(m), v_s):
        func = functions[i]
        # constr = cp.abs(func(x)[0] - v_i) <= v_i * gamma
        constr = (func(x)[0] >= v_i *(1 - gamma))  # because functions are to be maximized
        constraints.append(constr)

    objective = cp.Minimize(gamma)
    prob = cp.Problem(objective, constraints)

    result = prob.solve(solver=cp.SCIPY, verbose = False)

    x = x.value
    gamma = gamma.value

    return x, gamma