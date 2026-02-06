class SystemHelpers:
    def __init__(self):
        pass

    def extract(self, data):
        """
        Standard extractor for dispatcher output
        """
        return data.get("meta"), data.get("payload")
