# import packages
import gym
import minerl
import logging
logging.basicConfig(level=logging.DEBUG)

# set up OpenAI Gym for MineRL's `BASALT - Find Cave v0 challenge`
env = gym.make('MineRLBasaltFindCave-v0')

# note: this command will launch the MineRL environment, which takes time. Be patient!
obs = env.reset()

# take actions until either the agent dies or the three-minute timer runs out
done = False
while not done:
    # take a random action
    action = env.action_space.sample()
    # note: in BASALT environments, sending ESC action will end the episode
    # let's not do that
    action["ESC"] = 0
    obs, reward, done, _ = env.step(action)
    env.render()
