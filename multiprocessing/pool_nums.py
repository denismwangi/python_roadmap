from multiprocessing import Pool


def num_cubes(number):
    return number * number * number


if __name__ == "main":

    numbers = range(10)
    pool = Pool()

    result = pool.map(num_cubes, numbers)
    #pool.apply(num_cubes, numbers[0])
    pool.close()
    pool.join()

    print(result)

    print("end main")
