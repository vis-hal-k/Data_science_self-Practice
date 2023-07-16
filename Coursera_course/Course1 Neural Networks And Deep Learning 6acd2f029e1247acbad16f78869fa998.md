# Course1: Neural Networks And Deep Learning.

Housing price Prediction 

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled.png)

This is single neuron example

/white
we can get large neuron ex by stacking single one.

Above function called ******************ReLU →****************** Rectified Linear Unit..

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%201.png)

Here size,bedrooms,Zipcode,wealth  is comes in X (input layer).
And By stacking it together we get Neural network to predict price=Y . The circle in image is called middle layers of this neural network  is densely connected to the input layer.

************IMPLEMENT************ 

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%202.png)

## Supervised Learning with a Neural Network.

| INPUT (X) | OUTPUT ( Y ) | Application |  |
| --- | --- | --- | --- |
| Home features | Price | Real Estate | standard NN |
| ad, user info  | Click on ad ? (0/1) | Online advertising | standard NN |
| Image  | Text transcript | speech recognition | For image often use CNN |
| English | Hindi | Machine translation  | for language comes under sequence so often use complex RNN |
| Image, radar info  | Position of other cars | Autonomous Driving | Image → CNN
Radar → Complex, structure, Hybrid Neural Network  |
| Audio | Text transcript | speech recognition | for sequence, it is 1D time series, RNN for sequence data |

### Standard NN

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%203.png)

### CNN

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%204.png)

### RNN (Recurrent NN)

This basically good for 1 dimension sequence type.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%205.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%206.png)

Neural Network can be converted in supervised Learning .
Supervised Learning means deals of structured and unstructured data.

Neural networks are a class of models commonly used in supervised learning. They are composed of interconnected layers of artificial neurons, organized in a way that allows them to learn complex patterns and relationships within the data. Each neuron in the network takes inputs, applies a weighted sum, passes the result through an activation function, and produces an output. The network's parameters, such as weights and biases, are adjusted during training to minimize the difference between predicted outputs and true labels.

In the context of using neural networks for supervised learning, the network architecture is designed to learn the mapping between input features and output labels. The training process involves presenting the labeled training data to the network, computing the predicted outputs, comparing them to the true labels, and updating the network's parameters through a process called backpropagation. This iterative process continues until the network achieves satisfactory performance on the training data.

Here's an example to illustrate the concept:

Suppose we have a dataset of housing prices, where each data sample consists of features like the size of the house, number of bedrooms, and location, along with the corresponding target value, which is the actual sale price of the house. We want to build a neural network model that can predict the price of a house based on its features.

We would use the labeled dataset to train the neural network in a supervised learning fashion. During training, the network takes the features of a house as input, passes them through its layers, and produces a predicted price as output. The difference between the predicted price and the true price is computed using a loss function. The network's parameters (weights and biases) are then updated through backpropagation and gradient descent to minimize the loss. This process is repeated for multiple iterations until the network learns to make accurate predictions.

Once the neural network is trained, it can be used to predict the prices of new, unseen houses by feeding their features into the network and obtaining the predicted prices as outputs.

In summary, neural networks are powerful models used in supervised learning tasks. They learn the mapping between input features and output labels by iteratively adjusting their parameters based on the labeled training data. This enables them to make predictions on new, unseen data examples.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%207.png)

Modern Rise of deep learning it was scaled data and scale of computation just our ability to train very large Neural Networks either on ********CPU or GPU******** that enabled us to make a lot of progress.

Interestingly many of the algorithmic innovations have been about trying to make NN run much faster. Ex → $Sigmoid$ , $Relu$

> It turns out that one of the problems of using sigmoid functions and machine learning is that there are these regions here where the slope of the function where the gradient is nearly zero and so learning becomes really slow, because when you implement gradient descent and gradient is zero the parameters just change very slowly. And so, learning is very slow whereas by changing the what's called the activation function the neural network to use this function called the value function of the rectified linear unit, or RELU, the gradient is equal to 1 for all positive values of input. right. And so, the gradient is much less likely to gradually shrink to 0 and the gradient here. the slope of this line is 0 on the left but it turns out that just by switching to the sigmoid function to the RELU function has made an algorithm called gradient descent work much faster and so this is an example of maybe relatively simple algorithmic innovation. But ultimately, the impact of this algorithmic innovation was it really helped computation.
> 

 

### Question 1:

Recall this diagram of iterating over different ML ideas. Which of the statements below are true? (Check all that apply.)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%208.png)

- [ ]  Being able to try out ideas quickly allows deep learning engineers to iterate more quickly.
- [ ]  Faster computation can help speed up how long a team takes to iterate to a good idea.
- [ ]  It is faster to train on a big dataset than a small dataset.
- [ ]  Recent progress in deep learning algorithms has allowed us to train good models faster (even without changing the CPU/GPU hardware).
    - *Correct Ans here*
        
        1, 2 and 3
        

### Question 2

Neural Network are good figuring out functions relating an input x to an output y given enough examples. True/False ?

- [ ]  True
- [ ]  False
    - *Correct Ans here*
        
        True
        

### Question 3

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%209.png)

- [ ]  Increasing the size of a neural network generally does not hurt an algorithm’s performance, and it may help significantly.
- [ ]  Decreasing the size of a neural network generally does not hurt an algorithm’s performance, and it may help significantly.
- [ ]  Increasing the training set size generally does not hurt an algorithm’s performance, and it may help significantly.
- [ ]  Decreasing the training set size generally does not hurt an algorithm’s performance, and it may help significantly.
- [ ]  Increasing the training set size of a traditional learning algorithm always improves its performance.
- [ ]  Increasing the training set of a traditional learning algorithm stops helping to improve the performance after a certain size.
    - *Correct Ans here*
        
        1, 3 and 5
        

### Question 4

Question 8: Why is an RNN (Recurrent Neural Network) used for machine translation, say translating English to French? (Check all that apply.)

- [ ]  It can be trained as a supervised learning problem.
- [ ]  It is strictly more powerful than a Convolutional Neural Network (CNN).
- [ ]  It is applicable when the input/output is a sequence (e.g., a sequence of words).
- [ ]  RNNs represent the recurrent process of Idea->Code->Experiment->Idea->…
    - ***********Correct Ans here***********
        
        1 and 3
        

---

## Basic of Neural Network Programing

Logistic regression is an example of Binary Classifications.

![Y is target value which is 0 and 1. ](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2010.png)

Y is target value which is 0 and 1. 

### Notations

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2011.png)

## Logistic Regression

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2012.png)

## Logistic regression Cost function

 

 

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2013.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2014.png)

### Summary:

In logistic regression, the loss function and cost function are used to measure the performance of the model and guide the learning process. Let's explain each of them:

1. Loss Function:
The loss function is a measure of how well the model predicts the true labels for each training example. In logistic regression, the most commonly used loss function is the binary cross-entropy loss (also known as log loss or logistic loss). The formula for the binary cross-entropy loss for a single training example is:

L(y, ŷ) = -[y * log(ŷ) + (1 - y) * log(1 - ŷ)]

Where:

- L is the loss value
- y is the true label (0 or 1) for the training example
- ŷ is the predicted probability of the positive class (usually obtained using the sigmoid function) for the training example

The loss function penalizes the model more when it makes incorrect predictions with high confidence (i.e., large deviation between y and ŷ). It converges to 0 when the predicted probability ŷ approaches the true label y. This signifies that the model's prediction is becoming more accurate, and the loss is decreasing. The loss function is used to measure how well the model predicts the true labels for each training example and helps the model to get more accurate predictions.

1. Cost Function:
The cost function, also known as the objective function or the average loss, is the average value of the loss function over the entire training dataset. It represents the overall performance of the model across all training examples. The purpose of the cost function is to guide the learning process and find the optimal set of model parameters (weights(w) and biases(b)) that minimize the prediction errors. b is intercept. 

The cost function for logistic regression is the average binary cross-entropy loss over the training dataset. It can be calculated as follows:

J(w, b) = (1/m) * ∑[L(y, ŷ)]

Where:

- J is the cost function
- w is the vector of model weights
- b is the bias term
- m is the number of training examples
- L(y, ŷ) is the loss function for each training example

The goal of training the logistic regression model is to find the values of w and b that minimize the cost function J. This is typically done using optimization algorithms such as gradient descent, where the gradients of the cost function with respect to the model parameters are computed and used to update the parameter values iteratively until convergence.

By minimizing the cost function, the logistic regression model can learn the optimal decision boundary that separates the two classes (in the case of binary classification) or assigns probabilities to multiple classes (in the case of multi-class classification).

In summary, the loss function measures the performance of the model for individual training examples, while the cost function represents the overall performance across the entire training dataset. Both are essential components in training logistic regression models and guiding the learning process to find the optimal parameters for accurate predictions.

## Gradient Descent

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2015.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2016.png)

Gradient descent helps find the value of (w). Here we  moves to global minima. 

**Gradient descent is a mathematical optimization algorithm** used to find the minimum value of a function. It works by iteratively adjusting the parameters of the function in the opposite direction of the gradient, which points in the direction of steepest ascent. This process is repeated until a minimum value is reached or a specified number of iterations have been completed. Gradient descent is widely used in machine learning and artificial intelligence applications to optimize model parameters and improve performance.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2017.png)

Certainly! In mathematical terms, gradient descent can be represented as follows:

1. Initialization:
    - Initialize the parameters of the model: θ = [θ₁, θ₂, ..., θₙ] (where n is the number of parameters)
    - Set the learning rate: α
2. Compute the gradient:
    - For each parameter θⱼ, compute the partial derivative of the cost function J(θ) with respect to θⱼ: ∂J(θ)/∂θⱼ
3. Update the parameters:
    - For each parameter θⱼ, update it by subtracting the learning rate multiplied by the gradient:
    θⱼ := θⱼ - α * ∂J(θ)/∂θⱼ
4. Repeat steps 2 and 3 until convergence:
    - Iterate the steps of computing the gradient and updating the parameters until a stopping criterion is met. This criterion could be a maximum number of iterations, reaching a certain threshold of improvement, or other conditions.

The partial derivative ∂J(θ)/∂θⱼ represents the rate of change of the cost function J(θ) with respect to each parameter θⱼ. It indicates the direction and magnitude of the steepest increase in the cost function. By subtracting the product of the learning rate α and the gradient from each parameter, we move the parameters in the direction of steepest descent to minimize the cost function.

- Derivatives  Basic
    
    ### Derivatives
    
    ![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2018.png)
    

## Computation Graph and Derivatives

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2019.png)

![This is forward pass.](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2020.png)

This is forward pass.

### Computation derivative.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2021.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2022.png)

## Logistic regression Gradient Descent

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2023.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2024.png)

## Gradient Descent on m Example| DL

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2025.png)

## Vectorization

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2026.png)

```python
import numpy as np 
import time 
x=  np.random.rand(10000)
w= np.random.rand(10000)
print(w,"\n",x)
#  By vectorization Method
t = time.time() 
z = np.dot(w,x) + 1 
duration1 = time.time() - t 
print("z =",z," duration1 =",duration1*1000)
print( f'z = {z}, duration1 = { duration1*1000 }') # learn new way to print
"""
OUTPUT
z = 2501.396565161168  duration1 = 0.5612373352050781
z = 2501.396565161168, duration1 = 0.5612373352050781
"""
#  By Non Vectorization Method 
z = 0 
t= time.time()
for i in range(10000):
	z += w[i]*x[i] 
z += 1 
duration2 = time.time() - t  
print(f"z = {z} , duration2 = {duration2*1000}")
"""
z = 2501.3965651611684 , duration2 = 8.414983749389648
""" 
```

### More example of Vectorization

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2027.png)

### Vectorizing Logistic Regression

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2028.png)

```python
 # for z
Z = np.dot(W.T , X) + b 
# for a
def sigmoid(Z):
	V1 = 1+np.exp(-Z)
return 1/V1

A = sigmoid(Z)
```

### ****Vectorizing Logistic Regression's Gradient Computation****

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2029.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2030.png)

[Reference_1](https://youtu.be/2BkqApHKwn0)

[Reference__2](https://www.youtube.com/watch?v=-2oIr8W1INA&ab_channel=KnowledgeCenter)

## Broad Casting in Python

 

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2031.png)

```python
A = np.array([[56.0 , 0 , 4.4 , 68.0] , 
     [1.2 , 104.0 , 52 , 8],
     [1.8 , 135 , 99 ,0.9]])
cal = A.sum(axis = 0  )
percentage = 100*A/cal
percentage     
print(f'cal = {cal} \n  Percentage = \n{percentage} ')
"""
OUTPUT 
cal = [ 59.  239.  155.4  76.9] 
Percentage = 
[[94.91525424  0.          2.83140283 88.42652796]
 [ 2.03389831 43.51464435 33.46203346 10.40312094]
 [ 3.05084746 56.48535565 63.70656371  1.17035111]]
"""
```

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2032.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2033.png)

- *Correct Ans here*
    
    c)  c = a + b.T
    

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2034.png)

- *********Correct Ans here*********
    
    d
    

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2035.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2036.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2037.png)

- ***************Correct Ans here***************
    
    d.
    

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2038.png)

- ************Correct Ans here************
    
    d) because here ans → log(2) this is of base “e” so ans is ***0.693***
    

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2039.png)

## NEURAL NETWORK

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2040.png)

### NEURAL NETWORK Representation ✨✨✨

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2041.png)

### Computational Neural Network

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2042.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2043.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2044.png)

This is for single Training example

### Vectorizing across Multiple Examples

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2045.png)

Horizontally in Capital Z and A are the numbers of trainings examples (i = 1,2,3,4….. m)

Vertically index corresponding to different node in hidden layer. so this called Hidden Unit. 

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2046.png)

Explanation :

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2047.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2048.png)

## Activation Function

In all above case we use Activation function (a) is a sigmoid function.
Now Lets do works on some other function is can be Non-Linear Function or tanh
function also called  **[tangent hyperbolic](https://en.wikipedia.org/wiki/Hyperbolic_functions) function**

The tanh function is always superior than sigmoid function.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2049.png)

### Difference in tanh and sigmoid

**An important difference between the two functions is the behavior of their gradient.** Let’s compute the gradient of each activation function:

Below, we plot the gradient of the sigmoid (red) and the tanh (blue) activation function:

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2050.png)

When we are using these activation functions in a neural network, our data are usually centered around zero. So, we should focus our attention on the behavior of each gradient in the region near zero.

We observe that the gradient of tanh is four times greater than the gradient of the sigmoid function. This means that using the tanh activation function results in higher values of gradient during training and higher updates in the weights of the network. **So, if we want strong gradients and big learning steps, we should use the tanh activation function.**

**Another difference is that the output of tanh is symmetric around zero leading to faster convergence.**

### Example

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2051.png)

Note: Activation function can be different for different layer.

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2052.png)

### Derivative of Activation Function

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2053.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2054.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2055.png)

## Gradient Descent for Neural Networks

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2056.png)

 

![Forward propagation 4 equation  and back propagation have 6 equation.](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2057.png)

Forward propagation 4 equation  and back propagation have 6 equation.

[Reference](https://youtu.be/7bLEWDZng_M)

### [Back propagation Intuition](https://youtu.be/yXcQ4B-YSjQ)   (watch later ,optional)

### Random Initialization

Random initialization is a crucial step in training a neural network. If we initialize the weights of the neural network as a zero matrix, all the hidden units in the hidden layer will be the same, which defeats the purpose of having a hidden layer and neural network.

Apply random initialization :

```python
W1 = np.random.randn((2,2))*0.01
b1 = np.random.randn((2,1))
w2 ... similarly
b2 = 0
```

## What is Deep Neural Network ?

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2058.png)

### Forward Propagation in a Deep Neural Network

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2059.png)

### Getting Matrix Dimension Right

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2060.png)

Vectorization Implementation

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2061.png)

### (Building Blocks of DL nn)Forward and Backward Propagation

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2062.png)

Cache is for storing the Z[L]

### Forward and Backward Propagation for layer L

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2063.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2064.png)

## Parameter Vs Hyperparameter

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2065.png)

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2066.png)

### ****What does this have to do with the brain?****

![Untitled](Course1%20Neural%20Networks%20And%20Deep%20Learning%206acd2f029e1247acbad16f78869fa998/Untitled%2067.png)

[Excalidraw](https://excalidraw.com/#json=5djuk4A-FMygHWTaxHSBr,9rEoNhLhvnyT9KuGynqz5A)