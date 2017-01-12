class RateLimiter:

    def __init__(self, threshold):

        self.counter = 0
        self.threshold = threshold

    def is_active(self):

        if self.counter == self.threshold:
            self.counter = 0
            return False
        else:
            self.counter += 1
            return True
