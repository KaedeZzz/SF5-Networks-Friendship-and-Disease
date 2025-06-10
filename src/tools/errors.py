
def check_rate(rate: float):
    """Check if the transition rate is between 0 and 1."""
    if not 0.0 < rate < 1.0:
        raise ValueError('Transition rate must be between 0 and 1.')