class Alert():
    def __init__(self, data):
        if isinstance(data, dict):
            # Data contains just a key and a value
            # But we don't know the name of the key
            for key, value in data.items():
                key = key[0].lower() + key[1:]
                self.message = value
                break

        else:
            # Data is a Str
            self.message = data


# Success alert
class Success(Alert):
    def __init__(self, data):
        super().__init__(data)


# Information alert
class Information(Alert):
    def __init__(self, data):
        super().__init__(data)


# Error alert
class Error(Alert):
    def __init__(self, data):
        super().__init__(data)
