import matplotlib.pyplot as plt, mpld3


plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=3, ms=20)

a = plt.figure()
b = mpld3.fig_to_d3(a)
c = mpld3.fig_to_dict(a)







