import numpy
import matplotlib.pyplot as plt

FILE_NAME = 'rewards_nonshare.npz'

if __name__ == '__main__':
    f = numpy.load(FILE_NAME)
    reward = f['arr_0']
    qmax = f['arr_1']
    
    l = len(qmax)
    
    fig = plt.figure(figsize=(8,6))
    line1, = plt.plot(qmax, color='r', linestyle='-', linewidth=3)
    #line2, = plt.plot(numpy.arange(l), -150 * numpy.ones(l), color='k', linestyle=':', linewidth=1)
    plt.xlabel('Episode', fontsize=26)
    plt.ylabel('Reward', fontsize=24)
    plt.xticks(fontsize=22) 
    plt.yticks(fontsize=22) 
    #plt.axis([-20, l+10, -600, -100])
    plt.tight_layout()
    fig.savefig('qmax.pdf', format='pdf', dpi=1200)
    plt.show()
    
    
    




