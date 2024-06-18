import sys
from time import time, sleep


def print_progress_bar(iteration, total, elapsed_time):
    bar_size = 20
    percent = 100 * (iteration / float(total))
    filled_length = int(bar_size * iteration // total)
    bar = "=" * filled_length + ">" + " " * (bar_size - filled_length - 1)
    elapsed = elapsed_time
    if iteration == 0:
        eta = 0
    else:
        eta = (elapsed_time / iteration) * (total - iteration)

    sys.stdout.write(
        f"\rETA: {eta:.2f}s [{percent:>5.1f}%][{bar}] {iteration}/{total} | elapsed time {elapsed:.2f}s"
    )
    sys.stdout.flush()
    if iteration == total:
        print()


def ft_progress(lst):
    total = len(lst)
    start_time = time()
    for i, item in enumerate(lst):
        elapsed_time = time() - start_time
        print_progress_bar(i + 1, total, elapsed_time)
        yield item


def case_one():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


def case_two():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)


if __name__ == "__main__":
    case_one()
