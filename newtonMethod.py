import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)

# the functions, which are y = sin(x) and z = cos(x) here
y = np.cos(x)
z = x

# setting the axes at the centre
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')

ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')

ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')

ax.yaxis.set_ticks_position('left')
# ax.set_ylim([0, 30])

# plot the functions
plt.plot(x,y, 'c', label='f(x)=1+e^(2x)')

plt.plot(x,z, 'm', label='g(x)=x^2')

plt.legend(loc='upper left')

# show the plot
plt.show()

def m(x):

    return (x**(2/3)*(4-(x**2)))

def f(x):

    return np.cos(x)

    # return ((2*(4-(x**2)))/(3*(x**(1/3))))-(2*(x**(5/3)))

    # return x**3 - 5*x - 9

# Defining derivative of function
def g(x):

    return (-14*(x**(2/3))/3)-((2*(4-(x**2)))/(9*(x**(4/3))))

    # return 3*x**2 - 5

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):

    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')

    step = 1

    flag = 1

    condition = True

    while condition:

        if g(x0) == 0.0:

            print('Divide by zero error!')

            break
        
        x1 = x0 - f(x0)/g(x0)

        print(f'''Iteration-{step}, x1 ={x1}, f(x1) = {m(x1)}, f'(x1)={f(x1)} and f"(x1)={g(x1)}''')

        x0 = x1

        step = step + 1
        
        if step > N:

            flag = 0

            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:

        print('\nRequired root is: %0.4f' % x1)

        if g(x1)<0:

            print(f"We found maximum at {x1} is {m(x1)}")
    else:

        print('\nNot Convergent.')


# Input Section
print('''Here, f(x)= x\u00B2\u2044\u00B3(4-x\u00B2)''')

x0 = input('Initial Guess: ')

e = input('Tolerable Error: ')

N = input('Maximum Step: ')

print('''Here, f'(x)= (2(4-x\u00B2)/3x\u00B9\u2044\u00B3(4-x\u00B2))-2x\u2075\u2044\u00B3''')

print('''And, f''(x)= (2(4-x\u00B2)/3x\u00B9\u2044\u00B3(4-x\u00B2))-2x\u2075\u2044\u00B3''')

# Converting x0 and e to float
x0 = float(x0)

e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)