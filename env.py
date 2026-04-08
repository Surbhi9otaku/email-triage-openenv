from tasks import tasks
from models import EmailAction
from grader import grade


class EmailEnv:
    def __init__(self):
        self.current = 0

    def reset(self):
        self.current = 0
        return tasks[self.current]["email"]

    def step(self, action: EmailAction):
        task = tasks[self.current]
        correct = task["answer"]

        # grading (smart reward)
        reward = grade(task["type"], action.response, correct)

        # penalty for wrong answer
        if reward == 0:
            reward = -0.5

        # penalty for very short / useless answers
        if len(action.response.strip()) < 3:
            reward -= 0.2

        # move to next task
        self.current += 1
        done = self.current >= len(tasks)

        next_email = None if done else tasks[self.current]["email"]

        return next_email, reward, done, {}