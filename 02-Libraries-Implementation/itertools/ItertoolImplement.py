import itertools

if __name__ == "__main__":
    seq = ["joe", 'er', 'erqw']
    cycle_1 = itertools.cycle(seq)
    print(next(cycle_1), next(cycle_1), next(cycle_1), next(cycle_1), next(cycle_1), )

    count_1 = itertools.count(100, 10)
    print(next(count_1), next(count_1), next(count_1))

    print(list(itertools.chain("alskdmalfsdgjnwlekrqlwmrlkamfdf", "asdalkfmgdlgn123123123123")))
