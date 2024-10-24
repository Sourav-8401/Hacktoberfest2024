def generate_primes(n):
    primes = []
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    prime = [True for _ in range(n+1)]
    
    p = 2
    while p * p <= n:
        # If prime[p] is still true, then it is a prime
        if prime[p]:
            # Mark all multiples of p as false
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    # Collecting all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    
    return primes

# Example usage
n = 50  # Generate primes up to 50
print(generate_primes(n))
