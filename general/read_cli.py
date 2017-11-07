# applicant = input("Enter the applicant's name: ")
# interviewer = input("Enter the interviewer's name: ")
# time = input("Enter the appointment time: ")
# print(interviewer, "will interview", applicant, "at", time)

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)


print fib(1)
print fib(2)
print fib(3)
print fib(4)
print fib(5)
print fib(6)
print fib(7)
print fib(8)