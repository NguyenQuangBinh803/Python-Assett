import logging

class function:
    def __init__(self):
        format_string = "%(asctime)s : %(levelname)s : %(processName)s : %(threadName)s : %(funcName)s :%(lineno)d %(message)s"
        logging.basicConfig(filename="logging.log", level=logging.DEBUG, format=format_string)
        logging.info("image")
        logging.warning("image")
        logging.critical("image")
        # logging.("image")



# class

if __name__ == "__main__":
    func = function()