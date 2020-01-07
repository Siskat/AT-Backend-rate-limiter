import rate_limiter

bucket = rate_limiter.Bucket(100)
# exposed method
rate_limiter.callMethod()
