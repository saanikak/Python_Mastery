import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " milliseconds.")
        return result
    return wrapper


@time_it
def calc_square(nums):
    results = [i**2 for i in nums]
    return results

@time_it
def calc_cube(nums):
    results = [i**3 for i in nums]
    return results

nums = range(1,10000)
sq = (calc_square(nums))
cb = (calc_cube(nums))