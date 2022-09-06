import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        num = min(num, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for i in range(num)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        for k, v in expected_balls.items():
            if drawn_balls.count(k) < v:
                break
        else:
            count += 1
    return count / num_experiments
    