class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        
        self.value = compute_function([data.value for data in self.inputs])

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
    