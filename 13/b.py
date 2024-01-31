import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# Z = np.zeros((100, 100))
# for i in range(len(x)):
#     for j in range(len(y)):
#         Z[i, j] = np.sin((x[i]**2 + y[j]**2) ** 0.5)


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap='inferno')
# plt.show()
# plt.close()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X, Y, Z, c='r', marker='o', s = 2)
# plt.show()
# plt.close()

plt.contourf(X, Y, Z, cmap='inferno', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Wave')
plt.show()



# # Plot the 3D surface
# plt.contourf(x, y, u, cmap='hot', levels=20)
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# # plt.title(f'Time step {i}')
# # plt.show()
# plt.savefig(f'Fluid Dynamics\pr10\lax')
# plt.close()
