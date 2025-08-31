def sieve_eratosthenes(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


print(sieve_eratosthenes(30))  # Example usage