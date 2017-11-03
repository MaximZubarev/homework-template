def cancel(func):
    def _inner():
        return IndexError(func.__name__, 'is canceled!')

    return _inner


def timeit(func):
    import time

    def _inner():
        start = time.clock()

        result = func()

        print('Passed', time.clock() - start)
        return result

    return _inner


def count_execution(func):
    func.count = 0

    def _inner():
        func.count += 1
        print(func.count)
        return func()

    return _inner


def catch(func):
    def _inner():
        try:
            print(func())
        except Exception as e:
            print(e)

    return _inner
