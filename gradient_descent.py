data = [
  (0.0, 0.0),
  (.5, 0),
  (0.0, 0.5),
  (1.0, 1.0),
  (1.0, 1.2),
  (1.1, 1.0),
  (2.0, 2.0),
  (2.3, 2.1),
  (2.0, 2.1),
  (3.0, 3.0),
  (3.0, 3.5),
  (4.0, 4.0),
  (4.5, 4.0)
]



# import matplotlib.pyplot as plt

# x = []
# y = []

# for x1, y1 in data:
#     x.append(x1)
#     y.append(y1)

# slope =  0.9836078329
# intercept = 0.376370703955

# abline_values = [slope * i + intercept for i in x]

# plt.scatter(x, y, alpha=0.5)
# plt.plot(x, abline_values)
# plt.show()


"""
  h(x) = 01 + 02x

  J(01, 02) =  SUM 1..m ( 1/2m(h(x) - y)^2 )

  d/d01 SUM 1..m( 1/m(h(x) - y))
  d/d02 SUM 1..m( 1/m(h(x) - y) * x)

"""

def deriv_theta_0(n, theta_0, theta_1, x, y):
  return (theta_0 + theta_1 * x) - y

def deriv_theta_1(n, theta_0, theta_1, x, y):
  return deriv_theta_0(n, theta_0, theta_1, x, y) * x

def run_descent(data):

  n = len(data)
  theta_0 = 0
  theta_1 = 0

  for i in range(10000):
    sum_0 = 0
    sum_1 = 0
    for x, y in data:
      sum_0 += deriv_theta_0(n, theta_0, theta_1, x, y)
      sum_1 += deriv_theta_1(n, theta_0, theta_1, x, y)

    theta_0 = theta_0 - .01 * (1.0 / n) * sum_0
    theta_1 = theta_1 - .01 * (1.0 / n) * sum_1

  print theta_0, theta_1

run_descent(data)
