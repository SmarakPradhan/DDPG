import gym
import numpy as np
from DDPG import PlotLearning, Agent




if __name__ == "__main__":
    
    env = gym.make('LunarLanderContinuous-v2')
    print("STATE SHAPE:",env.observation_space.shape)
    print("ACTION SHAPE:",env.action_space.shape)

    
    

    
    LR_ACTOR = 0.0025
    LR_CRITIC = 0.0025

    agent = Agent(lr_actor=LR_ACTOR, lr_critic =LR_CRITIC, input_dims=env.observation_space.shape, tau=0.001, env=env,
              batch_size=64,  layer1_size=400, layer2_size=300, n_actions=env.action_space.shape[0])

    n_games = 1000
    
    filename = "LunarLander_lr_critic_" + str(LR_CRITIC) + "_lr_actor_" + str(LR_ACTOR) + str(n_games) + "_games.png"

    np.random.seed(0)

    score_to_beat = env.reward_range[0]
    score_history = []
    for i in range(n_games):
        observation = env.reset()
        is_terminal = False
        score = 0
        agent.noise.reset()
        while not is_terminal:
            action = agent.choose_action(observation)
            observation_next,reward,is_terminal,info = env.step(action)
            agent.Memory(observation,action,reward,observation_next,is_terminal)
            agent.learn()
            score += reward
            observation = observation_next
        score_history.append(score)
        avg_score = np.mean(score_history[-100:])

        if avg_score > score_to_beat:
            score_to_beat = avg_score
            agent.save_models()

        print("For Episode",i+1,"SCore %.1f" % score,"Average Score %.1f"% avg_score)

        PlotLearning(score_history, filename, window=100)



