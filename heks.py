import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixed value for number of axes to avoid input error in non-interactive environments
num_axes = 3  # Change this value as needed

# Parameters
base_length = 1.0  # Base length of the first segment
num_frames = 500  # Number of animation frames

def gravity_speed(t):
    return np.sin(t * np.pi)  # Simulates gravity effect (fast down, slow up)

# Compute segment lengths
segment_lengths = [base_length / (2 ** i) for i in range(num_axes)]

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-2 * base_length, 2 * base_length)  # Expanded space
ax.set_ylim(-2 * base_length, 2 * base_length)
ax.set_aspect('equal')
ax.set_title(f"{num_axes} Rotating Axes System")

# Line objects
lines = [ax.plot([], [], 'bo-', lw=2)[0] for _ in range(num_axes)]
trace, = ax.plot([], [], 'r.', markersize=1)  # Traced path

# Trace storage
trace_x, trace_y = [], []

def update(frame):
    time = frame / num_frames  # Normalize time (0 to 1)
    
    angles = [0] * num_axes
    for i in range(num_axes):
        if i == num_axes - 1:
            speed_factor = gravity_speed(time) * (2 ** i) * 3  # Gravity-based speed only for last line
        else:
            speed_factor = (2 ** i) * 3  # Increase speed with each axis
        angles[i] = speed_factor * time * 2 * np.pi
    
    x, y = [0], [0]  # Start at origin

    for i in range(num_axes):
        new_x = x[-1] + segment_lengths[i] * np.cos(angles[i])
        new_y = y[-1] + segment_lengths[i] * np.sin(angles[i])
        x.append(new_x)
        y.append(new_y)
    
    # Update visualization
    for i in range(num_axes):
        lines[i].set_data([x[i], x[i+1]], [y[i], y[i+1]])

    # Trace path of last segment
    trace_x.append(x[-1])
    trace_y.append(y[-1])
    trace.set_data(trace_x, trace_y)

    return lines + [trace]

# Animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=10, blit=True)
plt.show()