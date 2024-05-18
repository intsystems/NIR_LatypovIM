import cvxpy as cp
import numpy as np

def clip_default(x,y):
    """
    default function for clip, 
    which does not take into account monotonicity
    """
    return x - y


def gamma_for_budget(budget, c_x, x_s, v_s, L_s, clip_functions = None, norm = 1):
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
    assert norm in [1,2]
    assert len(x_s) == len(v_s) == len(L_s), print("provided argument lens is not the same")
    if clip_functions is not None:
        assert len(x_s) == len(clip_functions), f"({len(x_s)=}) != ({len(clip_functions)})"
    m, n = x_s.shape

    gamma = cp.Variable()
    x = cp.Variable(n)

    constraints = [x @ c_x <= budget, 0. <= x] 

    for i, L_i, v_i, x_i in zip(range(m), L_s, v_s, x_s):
        cf = clip_default
        if clip_functions is not None:
            cf = clip_functions[i]
        constr = cp.norm(cf(x, x_i), norm) <= (v_i/L_i) * gamma
        constraints.append(constr)

    objective = cp.Minimize(gamma + 1e-2 *( x @ c_x)/budget)
    prob = cp.Problem(objective, constraints)

    if norm == 2:
        result = prob.solve(solver=cp.ECOS, max_iters = 300)
    else:
        result = prob.solve(solver=cp.SCS,)


    

    x = x.value
    gamma = gamma.value

    return x, gamma