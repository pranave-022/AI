from copy import deepcopy

# ---------- Helper Functions ----------

def is_variable(term):
    return isinstance(term, str) and term[0].islower()

def occur_check(var, expr):
    if var == expr:
        return True
    elif isinstance(expr, tuple):
        return any(occur_check(var, sub) for sub in expr)
    return False

def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    if x == y:
        return subst
    elif is_variable(x):
        if occur_check(x, y):
            return None
        subst[x] = y
        return subst
    elif is_variable(y):
        if occur_check(y, x):
            return None
        subst[y] = x
        return subst
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst
    else:
        return None

def substitute(expr, subst):
    """Apply substitution θ to expression."""
    if isinstance(expr, tuple):
        return tuple(substitute(e, subst) for e in expr)
    elif is_variable(expr) and expr in subst:
        return subst[expr]
    else:
        return expr


# ---------- Forward Chaining Algorithm ----------

def forward_chain(KB, query):
    new = set()
    while True:
        inferred = False
        for rule in KB:
            # Rule format: (premises, conclusion)
            if not isinstance(rule, tuple) or not isinstance(rule[0], tuple):
                continue  # skip facts

            premises, conclusion = rule

            # Find substitutions satisfying all premises
            theta = {}
            satisfied = True
            for p in premises:
                match_found = False
                for fact in KB:
                    if isinstance(fact, tuple) and not isinstance(fact[0], tuple):
                        sub = unify(p, fact, deepcopy(theta))
                        if sub is not None:
                            match_found = True
                            theta.update(sub)
                            break
                if not match_found:
                    satisfied = False
                    break

            if satisfied:
                q_prime = substitute(conclusion, theta)
                if q_prime not in KB and q_prime not in new:
                    new.add(q_prime)
                    inferred = True
                    # check if matches query
                    phi = unify(q_prime, query)
                    if phi is not None:
                        return phi
        if not inferred:
            return False
        KB.update(new)


# ---------- Example ----------
KB = {
    ('has_fever', 'John'),
    ('has_cough', 'John'),
    # Rule: ((premises), conclusion)
    ((('has_fever', 'x'), ('has_cough', 'x')), ('has_flu', 'x'))
}

query = ('has_flu', 'John')

result = forward_chain(KB, query)
print("Result:", result)
