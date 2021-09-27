# Huber
"""
delta = 0.1
for i in range(m):
    if abs(self.y[i][0] - self.hypothesis(w, b, x[i])) <= delta:
        err += 0.5 * math.pow(self.y[i][0] - self.hypothesis(w, b, x[i]), 2)
    else:
        err += delta * abs(self.y[i][0] - self.hypothesis(w, b, x[i])) - 0.5 * math.pow(delta, 2)

err /= m
"""

"""
for i in range(m):
    cosenoHiperbolico = math.cosh(self.y[i][0] - self.hypothesis(w, b, x[i]))
    err += math.log(cosenoHiperbolico)
"""
