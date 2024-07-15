def start_Fast_Spiking():
    T               =   1000                    # total simulation length [ms]
    dt              =   0.5                     # step size [ms]
    time            =   np.arange(0, T+dt, dt)  # step values [ms]

    V = Izhikevich_Model(_I=10,a=0.1,b=0.2,c=-65,d=8)
    I = I_values(time=time)

    # Plotting
    fig = plt.figure("Fast Spiking Neuron", figsize=(15, 8))
    ax = fig.add_subplot(111)
    plt.title("Fast Spiking Izhikevich Neuron Simulation")

    line = plt.plot(time, V, label="Membrane Potential")[0]
    line2 = plt.plot(time, I, label="Applied Current")[0]
    plt.legend(loc="upper right")
start_Fast_Spiking()

