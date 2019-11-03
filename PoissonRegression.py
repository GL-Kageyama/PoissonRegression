#=================================================================
#---------------        Poisson regression        ---------------- 
#=================================================================
# Poisson regression is used to model the incidence of events.
#=================================================================
# Value description
# x : Time
# y : Effect
# Assuming Poisson distribution as objective variable
#=================================================================
# STEP 1 : Graph the relationship between time and effect
#=================================================================
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8, 0.1)
y = np.exp2(x) + np.random.randn(70) + 4

plt.scatter(x, y, color="c")
plt.show()

#=================================================================
# STEP 2 : Poisson regression to find effects on time
#=================================================================

beta = np.array([0., 0.])

for i in range(10000):
    exp_lindif_0 = -y + np.exp(beta[0] + beta[1]*x)
    exp_lindif_1 = x*(-y + np.exp(beta[0] + beta[1]*x))
    grad = np.array([np.sum(exp_lindif_0), np.sum(exp_lindif_1)])
    
    beta[0] = beta[0] - 0.00001*grad[0]
    beta[1] = beta[1] - 0.00001*grad[1]
    
    if (i + 1)%2000 == 0:
        print("STEP_" + str(i + 1))
        print(beta)
        print(grad)
        print("---------------------------------")
print(beta)

x_ = np.arange(1, 9, 0.05)
y_ = np.exp(beta[0] + beta[1]*x_)

# The orange dot curve is the obtained value.
plt.scatter(x_, y_, color="coral")
# The blue dot curve is the original value.
plt.scatter(x, y, color="c")
plt.show()

