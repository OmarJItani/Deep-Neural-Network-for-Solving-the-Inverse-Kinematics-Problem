import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
model = load_model('arm_model.h5')

# Create trajectory

angle = np.linspace(0,np.pi/2,100)
traj = []
for i in angle:
    traj.append([2*np.cos(i),2*np.sin(i)])   

# Make Predictions
desired_traj = traj.copy()

desired_shape = [[0 , 0]]

for i in range(len(desired_traj)):
    cur_input = desired_traj[i].copy()
    cur_input.extend(desired_shape[-1])
    cur_model_input = np.array([cur_input])
    next_shape = model.predict(cur_model_input)
    print(f'next shape: {next_shape}')
    new_next_shape = next_shape.tolist()[0]
    print(f'new next shape: {new_next_shape}')
    desired_shape.append(new_next_shape)

# Plot results

plt.ion()
plt.show()

for ind, shape in enumerate(desired_shape):

    theta_1_i = shape[0]
    theta_2_i = shape[1]

    x0 = 0
    y0 = 0
    x1 = np.round(np.cos(theta_1_i), 2)
    y1 = np.round(np.sin(theta_1_i), 2) 
    x2 = np.round(x1 + np.cos(theta_2_i), 2)
    y2 = np.round(y1 + np.sin(theta_2_i), 2)
        
    plt.clf()
    plt.scatter(desired_traj[ind][0] , desired_traj[ind][1] , color = 'red')
    plt.plot( [x0,x1] , [y0,y1] , color='blue', linewidth=5 )
    plt.plot( [x1,x2] , [y1,y2] , color='blue', linewidth=3 )
    plt.xlim([-2.5,2.5])
    plt.ylim([-2.5,2.5])
    plt.pause(0.02)