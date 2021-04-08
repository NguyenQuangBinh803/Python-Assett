

if __name__ == "__main__":
    day = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    with open("logging.log", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    for index, d in enumerate(day, start=1):
        print(index, d)
            
            