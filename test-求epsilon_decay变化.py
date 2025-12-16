import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    p_index = 50
    val = np.power([0.99, 0.985, 0.98, 0.978, 0.97,0.965, 0.95, 0.945, 0.94, 0.6],list([p_index])*10)
    print(f"This is a {val}")

    power_val = []

    for i in range(0,201,1):
        val = np.power([0.995, 0.985, 0.98, 0.975, 0.97,0.965, 0.95, 0.945, 0.94, 0.6],list([i])*10)
        power_val.append(val)


    plt.plot(power_val,label=[0.995, 0.985, 0.98, 0.975, 0.97,0.965, 0.95, 0.945, 0.94, 0.6])
    plt.legend()
    plt.show()