class BindingObject:
    def __init__(self, binding_data_):
        self.binding_data = [binding_data_]

    def __str__(self):
        return str(self.binding_data)

    def set(self, reference_data_):
        self.binding_data[0] = reference_data_

    def get(self):
        return self.binding_data[0]


if __name__ == "__main__":
    refernece_object = BindingObject("INITIAL DATA")
    binding_object = refernece_object
    refernece_object.set("CHANGES")
    print (binding_object)
