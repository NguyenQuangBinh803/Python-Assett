import csv


def merge_csv(csv_list, output_path):
    fieldnamese = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnamese.extend(x for x in fn if x not in fieldnamese)

    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnamese)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


from string import Template

info = {
    "title": "Algebra Engine",
    "author": "Edward J. C. Ashenbert"
}

print(Template("This engine is ${title} writen by ${author}").substitute(info))

import collections
from collections import Counter
from collections import deque


def calculate_next_price(*args):
    '''
    This function is used to predict the next price of stock
    :param args: list of input data
    :return: integer value
    '''
    pass


def counter_implementation():
    class1 = ["Edward", "Miyuki"]
    counter_1 = Counter(class1)
    print(counter_1.value())
    print(calculate_next_price.__doc__)


def namedtuple_implementation():
    Info = collections.namedtuple("Ìnformation", "Name Address Telephone")
    info1 = Info("Edward", "Nagaoka", "0949619772")
    print(info1)


def deque_implementation():
    list_of_numbers = deque()
    for i in range(10):
        list_of_numbers.append(i)
    for i in range(10):
        list_of_numbers.appendleft(i)
    print(list_of_numbers)
    list_of_numbers.rotate(10)
    print(list_of_numbers)


def main():
    deque_implementation()


if __name__ == "__main__":
    main()
