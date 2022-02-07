from ex2 import fetcher
import time
CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def innerWrapper(*args, **kwargs):
            totalTimeAllRuns = 0

            for n in range(num):
                start = time.time()
                func(*args, **kwargs)
                currentTime = time.time() - start
                print(f'Время выполнения прогона:{n}: {currentTime}')
                totalTimeAllRuns += currentTime

            print(f'Среднее время прогона: {totalTimeAllRuns / num}')

        return innerWrapper
		
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
