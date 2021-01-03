class ColorSpace:
    def __init__(self):
        self.red = 100
        self.green = 100
        self.blue = 100

    def __getattr__(self, item):
        if item == "rgb":
            return (self.red, self.green, self.blue)
        elif item == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == "rgb":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(key, value)

if __name__ == "__main__":
    color = ColorSpace()
    print(color.rgb)
    color.rgb = (12,123,53)
    print(color.rgb)