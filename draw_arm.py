import numpy as np
from matplotlib import pyplot as plt


def arm_animate( l1 = 1 , l2 = 1 , l3 = 0.2 , t1_d = np.pi/2 , t2_d = np.pi/4 , t3_d = 0 ):
    plt.ion()
    plt.show()

    steps = 20

    theta_1 = np.linspace(0,t1_d,steps)
    theta_2 = np.linspace(0,t2_d,steps)
    theta_3 = np.linspace(0,t3_d,steps)

    for step_i in range(steps):

        theta_1_i = theta_1[step_i]
        theta_2_i = theta_2[step_i]
        theta_3_i = theta_3[step_i]

        x0 = 0
        y0 = 0
        x1 = np.round(l1*np.cos(theta_1_i), 2)
        y1 = np.round(l1*np.sin(theta_1_i), 2) 
        x2 = np.round(x1 + l2*np.cos(theta_2_i), 2)
        y2 = np.round(y1 + l2*np.sin(theta_2_i), 2)
        x3 = np.round(x2 + l3*np.cos(theta_3_i), 2)
        y3 = np.round(y2 + l3*np.sin(theta_3_i), 2)
            
        plt.clf()
        plt.plot( [x0,x1] , [y0,y1] , color='blue', linewidth=5 )
        plt.plot( [x1,x2] , [y1,y2] , color='blue', linewidth=5 )
        plt.plot( [x2,x3] , [y2,y3] , color='blue', linewidth=5 )
        plt.xlim([-2,2])
        plt.ylim([-2,2])
        plt.pause(0.02)
    
    return 0


arm_animate()