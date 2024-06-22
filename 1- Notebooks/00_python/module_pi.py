import random
import math

# Méthode de Leibniz
def pi_leibniz(n_terms):
    """Méthode de Leibniz"""
    pi_approx = 0
    for k in range(n_terms):
        pi_approx += (-1)**k / (2*k + 1)
    return 4 * pi_approx

# Méthode de Monte Carlo
def pi_monte_carlo(n_points):
    """Méthode de Monte Carlo"""
    inside_circle = 0
    for _ in range(n_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / n_points) * 4

# Méthode de la série de Nilakantha
def pi_nilakantha(n_terms):
    """Méthode de la série de Nilakantha"""
    pi_approx = 3
    sign = 1
    for i in range(2, 2 * n_terms + 1, 2):
        pi_approx += sign * (4 / (i * (i + 1) * (i + 2)))
        sign *= -1
    return pi_approx

# Exemple d'utilisation des méthodes
if __name__ == "__main__":
    terms = 10000
    points = 10000

    print("Approximation de Pi avec la méthode de Leibniz :", pi_leibniz(terms))
    print("Approximation de Pi avec la méthode de Monte Carlo :", pi_monte_carlo(points))
    print("Approximation de Pi avec la méthode de Nilakantha :", pi_nilakantha(terms))
