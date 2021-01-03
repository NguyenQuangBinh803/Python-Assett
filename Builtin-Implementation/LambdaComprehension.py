if __name__ == "__main__":
    data = [12, 34, 35, 25, 34, 65, 654, 74, 7, 657, 14]
    temperature_in_celsius = [12,23,5,45,56]

    # TODO make use of lambda
    data_square = list(map(lambda x: x ** 2, filter(lambda x: x < 100, data)))
    print(data_square)

    # TODO replace lambda with comprehence
    data_square = [x**2 for x in data if x < 100]
    print(data_square)

    # TODO comprehension dictionary
    temp_dict = {t: (t*9/5) + 32 for t in temperature_in_celsius if t > 0}
    print(temp_dict)

    # TODO merge dictionary with comprehension
    dict_1 = {"Edward": 1000, "Miyuki": 1000, "Gustav": 1000}
    dict_2 = {"Atthony": 922, "Diana": 5000, "Louise": 7000}
    new_dict = {name:level for d in (dict_1, dict_2) for name, level in d.items()}
    print(new_dict)

    # TODO difference between set and list, a set get only unique valye
    ctemps = [123,123,123,12,312,312,312,312,3,3123123,1,231231,23,123,12,312,312,312312,312,31,23,12,312,3,123,12,3]
    unique_value = {c for c in ctemps}
    print(unique_value)

    # TODO find unique words in paragraph
    paragraph = "A paragraph " \
                "is a series of related sentences developing a" \
                " central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument."
    words = paragraph.split()
    unique_words = {w for w in words}
    print(unique_words)