import gym

env = gym.make('CartPole-v0')  # creates the environment


def basic_policy(obs):  # determines what actions to take
    angle = obs[2]
    return 0 if angle < 0 else 1  # 0 means left and 1 right


totals = []  # list of the total reward accumulated for each episodes, 10

for episodes in range(1000):
    episodes_rewards = 0  # rewards for the episode, in this case "staying alive"
    obs = env.reset()  # initial observation, carts horizontal position (0.0 for center), carts velocity, pole angle
    action = 1  # move cart left or right
    for step in range(1000):  # 1000 total steps, prevents the program to run forever
        action = basic_policy(obs)  # perform action based on the policy and observed env
        env.render()
        obs, reward, done, info = env.step(action)  # update the observations and reward with action
        episodes_rewards += reward  # add reward at current time step
        if done:
            totals.append(episodes_rewards)
            break

print(totals)
print("The longest number of timesteps the pole was balanced: " + str(max(totals)))
