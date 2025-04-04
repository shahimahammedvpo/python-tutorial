
import numpy as np
a1 = np.random.randint(0, 20, (3, 3))
a2 = np.random.randint(0, 20, (3, 3))
add = a1 + a2
prod = np.dot(a1, a2)
tr = prod.T
print("Addition:\n", add)
print("Product:\n", prod)
print("Transpose:\n", tr)
