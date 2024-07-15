# inspired by Devrim Celik's code

def Izhikevich_Model(_I = 10, a = 0.02, b = 0.2, c = -65, d = 8):

    spike_value = 35                 
    T               =   1000                    # total simulation length [ms]
    dt              =   0.5                     # step size [ms]
    time            =   np.arange(0, T+dt, dt)  # step values [ms]
    # VOLTAGE
    V               =   np.zeros(len(time))     # voltage history
    V[0]            =   -70                     # set initial to resting potential
    # RECOVERY
    u               =   np.zeros(len(time))     # array for saving Recovery history
    u[0]            =   -14
    # CURRENT
    I = np.zeros(len(time))
    I[200:1500] = _I

    for t in range(1, len(time)):
        
        # if we still didn't reach spike potential
        if V[t-1] < spike_value:
            # ODE for membrane potential
            dV      = (0.04 * V[t-1] + 5) * V[t-1] + 140 - u[t-1]
            V[t]    = V[t-1] + (dV + I[t-1]) * dt
            # ODE for recovery variable
            du      = a * (b * V[t-1] - u[t-1])
            u[t]    = u[t-1] + dt * du
        
        # spike reached!
        else:
            V[t-1] = spike_value    # set to spike value
            V[t] = c                # reset membrane voltage
            u[t] = u[t-1] + d       # reset recovery

    return V

def I_values(_I=10, time=None):
    I = np.zeros(len(time))
    I[200:1500] = _I
    return I


def start_IZ_sim():
    # time parameters for plotting
    T               =   1000                    # total simulation length [ms]
    dt              =   0.5                     # step size [ms]
    time            =   np.arange(0, T+dt, dt)  # step values [ms]

    
    V = Izhikevich_Model()
    I = I_values(time=time)

    # Plotting
    fig = plt.figure("Simple Izhikevich Neuron", figsize=(15, 8))
    ax = fig.add_subplot(111)
    plt.title("Izhikevich Neuron Simulation")

    # plot lines
    line = plt.plot(time, V, label="Membrane Potential")[0]
    line2 = plt.plot(time, I, label="Applied Current")[0]

    # add legend
    plt.legend(loc="upper right")

start_IZ_sim()
