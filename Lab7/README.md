### LAB 7 

Welcome

Here is how you can run a Python script that I created, which uses a plugin/library called matplotlib which is a comprehensive library for creating static, animated, and interactive visualizations in Python.

To show its application it is important to install it first, let's create a Virtual ENV called scripts so that it is easier to manage and find. You can name it whatever you find comforable.

```bash
virtualenv ~/venv/jinja
source ~/venv/scripts/bin/activate
python -m pip install -U pip
python -m pip install -U matplotlib
```
Now, Lets plot a simple graph using the script that I have written to show the functionality of the matplotlib library.
Now, in Python, run the following code
```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)')
ax.grid()

fig.savefig("test.png")
plt.show()
```
The above code should create a simple plot with time on the x-axis and voltage on the y-axis.

As you can see there are different functionalities such as 

```python
ax.grid()
ax.set()
ax.plot()
```

Finally, the graph is shown with the code,
```python
plt.show()
```
This can be a very useful library if you work with 2-dimensional graphs and plots. Often mathematical or scientific applications require more than single axes in a representation. This library helps us to build multiple plots at a time. You can, however, use Matplotlib to manipulate different characteristics of figures as well.

At the end do not forget to deactivate your VEnv.
```bash
deactivate
```

Thank you for taking your time to look at my work.
