from tasks import tasks
from models import EmailAction

class EmailEnv:
    def __init__(self):
        self.current = 0

    def reset(self):
        self.current = 0
        return tasks[self.current]["email"]

    def step(self, action: EmailAction):
        task = tasks[self.current]
        correct = task["answer"]

        if action.response == correct:
            reward = 1.0
        else:
            reward = -0.5

        self.current += 1
        done = self.current >= len(tasks)

        next_email = None if done else tasks[self.current]["email"]

        return next_email, reward, done, {}