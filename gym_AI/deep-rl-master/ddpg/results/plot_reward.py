import numpy
import matplotlib.pyplot as plt

FILE_NAME = 'rewards_nonshare.npz'

def smooth(reward_vec, filter_size):
    l = len(reward_vec) - filter_size + 1
    print(len(reward_vec))
    smooth_reward_vec = numpy.zeros(l)
    for i in range(l):
        reward = numpy.mean(reward_vec[i:i+filter_size])
        smooth_reward_vec[i] = reward
    return smooth_reward_vec
    

if __name__ == '__main__':
    f = numpy.load(FILE_NAME)
    reward = f['arr_0']
    qmax = f['arr_1']
    
    reward_smooth = smooth(reward, 300)
    l = len(reward_smooth)
    
    fig = plt.figure(figsize=(8,6))
    line1, = plt.plot(reward_smooth, color='r', linestyle='-', linewidth=3)
    line2, = plt.plot(numpy.arange(l), -150 * numpy.ones(l), color='k', linestyle=':', linewidth=1)
    plt.xlabel('Episode', fontsize=26)
    plt.ylabel('Reward', fontsize=24)
    plt.xticks(fontsize=22) 
    plt.yticks([-800, -700, -600, -500, -400, -300, -200, -150, -100, 0], fontsize=22) 
    plt.axis([-20, l+10, -600, -100])
    plt.tight_layout()
    fig.savefig('reward.pdf', format='pdf', dpi=1200)
    plt.show()
    
    
    




