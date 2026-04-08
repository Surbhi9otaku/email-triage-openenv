from env import EmailEnv
from models import EmailAction

env = EmailEnv()

email = env.reset()

while True:
    print("\nEmail:", email)
    
    user_input = input("Your response: ")
    action = EmailAction(response=user_input)

    email, reward, done, _ = env.step(action)

    print("Reward:", reward)

    if done:
        print("Finished!")
        break