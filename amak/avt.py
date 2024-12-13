class AVT:
    class Feedback:
        LOWER = 0
        GOOD = 1
        GREATER = 2

    def __init__(self, initial_value, lower_bound, upper_bound, initial_delta_t, lambda_a, lambda_d):
        self.value = initial_value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.delta_t = initial_delta_t
        self.delta_t_m1 = initial_delta_t
        self.lambda_a = lambda_a
        self.lambda_d = lambda_d

        self.last_feedback = self.Feedback.GOOD
        self.feedback = self.Feedback.GOOD

    def receive_feedback(self, new_feedback):
        self.delta_t_m1 = self.delta_t
        self.last_feedback = self.feedback
        self.feedback = new_feedback
        switcher = {
            self.Feedback.LOWER: self._lower,
            self.Feedback.GOOD: self._good,
            self.Feedback.GREATER: self._greater
        }
        switcher.get(self.feedback)()

    def _greater(self):
        if self.last_feedback == self.Feedback.GREATER:
            self.delta_t = self.delta_t_m1 * self.lambda_a
        elif self.last_feedback == self.Feedback.LOWER:
            self.delta_t = self.delta_t_m1 * self.lambda_d
        else:
            self.delta_t = self.delta_t_m1
        self._fix_delta_t()
        self.value = self.value + self.delta_t
        self._fix_value()

    def _lower(self):
        if self.last_feedback == self.Feedback.GREATER:
            self.delta_t = self.delta_t_m1 * self.lambda_d
        elif self.last_feedback == self.Feedback.LOWER:
            self.delta_t = self.delta_t_m1 * self.lambda_a
        else:
            self.delta_t = self.delta_t_m1
        self._fix_delta_t()
        self.value = self.value - self.delta_t
        self._fix_value()

    def _good(self):
        if self.last_feedback == self.Feedback.GREATER:
            self.delta_t = self.delta_t_m1 * self.lambda_d
        elif self.last_feedback == self.Feedback.LOWER:
            self.delta_t = self.delta_t_m1 * self.lambda_d
        else:
            self.delta_t = self.delta_t_m1 * self.lambda_d
        self._fix_delta_t()
        self._fix_value()

    def _fix_delta_t(self):
        if self.delta_t < 0:
            self.delta_t = 0
        elif self.delta_t > self.upper_bound - self.lower_bound:
            self.delta_t = self.upper_bound - self.lower_bound

    def _fix_value(self):
        if self.value < self.lower_bound:
            self.value = self.lower_bound
        elif self.value > self.upper_bound:
            self.value = self.upper_bound

