def min_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield (8*(-1) - 5*2) / 3 = -6 or (8*5 - 5*8) / 3 = 0
    a ---- b -- c and bc/ac = 3/8 => 8c - 8b = 3c - 3a => a = (8b - 5c)/3
    """
    return (8.0 * limit - 5.0 * maximum) / 3.0


def domain_from_limit_max(limit, maximum):
    """Prepare the scales paradigm for non-folded axes."""
    return min_from_limit_max(limit, maximum), maximum


def limit_folded_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield 2 * 2 - (-1) = 5 or 2 * 8 - 5 = 11
    """
    return 2.0 * maximum - limit  # explicit maximum + ( maximum - limit )


def min_folded_from_limit_max(limit, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)
    yield (11*2 - 8*(-1)) / 3 = 10 or (11*8 - 8*5) / 3 = 16
    a ---- b -- c ------- e and bc/ce = 3/8 => 8c - 8b = 3e - 3c => a = (11c - 8b)/3
    """
    return (11.0 * maximum - 8.0 * limit) / 3.0


def domain_folded_from_limit_max(limit, maximum):
    """Prepare the scales paradigm for folded axes."""
    max_domain = min_folded_from_limit_max(limit, maximum)
    min_domain = maximum + maximum - max_domain  # maximum - (max_domain - maximum)
    return min_domain, max_domain


def value_folded_from_limit_max(value, maximum):
    """
    Testdata: (-6, -1, 2, 5, 10) or (0, 5, 8, 11, 16)  # FIXME COPY
    yield 2 * 2 - (-1) = 5 or 2 * 8 - 5 = 11  # FIXME COPY
    """
    return 2.0 * maximum - value  # explicit maximum - ( value - maximum )


def limit_ordered_from_domain(domain):
    """
    Testdata: ("3", "2c", "2b", "2a", "1") or ("ORIGIN", "not ok", "LIMIT_VALUE", "ok")
    yield domain[len(domain) // 2] -> "2b" or "LIMIT_VALUE" in domain -> "LIMIT_VALUE"
    """
    if not domain:
        return 'NULL'
    if 'LIMIT_VALUE' in domain:
        return 'LIMIT_VALUE'
    return domain[len(domain) // 2]


def min_ordered_from_domain(domain):
    """
    Testdata: ("3", "2c", "2b", "2a", "1") or ("ORIGIN", "not ok", "LIMIT_VALUE", "ok")
    yield domain[0] -> "3" or domain[0] -> "ORIGIN"
    """
    return domain[0] if domain else 'NULL'


def domain_ordered_from_domain(domain):
    """Prepare the scales paradigm for ordered axes."""
    return domain if domain else 'NULL'


def max_ordered_from_domain(domain):
    """
    Testdata: ("3", "2c", "2b", "2a", "1") or ("ORIGIN", "not ok", "LIMIT_VALUE", "ok")
    yield domain[-1] -> "1" or domain[-1] -> "ok"
    """
    return domain[-1] if domain else 'NULL'
