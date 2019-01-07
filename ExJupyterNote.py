#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


x = np.linspace(2, 5, 3)
print('x: ',x)
plt.plot(x, np.sin(x))
plt.show() 
