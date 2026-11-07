

# DNN Polynomial Regression 

---

## 1. `import tensorflow as tf`

```python
import tensorflow as tf
```

### What is TensorFlow?
TensorFlow is a **machine-learning/deep-learning framework**. It provides the mathematical and computational tools needed to build and train neural networks.
- `as tf` means: Give TensorFlow the short name `tf`.

---

## 2. `import numpy as np`

```python
import numpy as np
```

### What is NumPy?
NumPy is a Python library for **working with numerical data, arrays, and mathematical operations**.

---

## 3. `import matplotlib.pyplot as plt`

```python
import matplotlib.pyplot as plt
```

### What is Matplotlib?
Matplotlib is a library for **creating graphs and visualizations**.

### Why use it?
Your assignment plots:
- original polynomial
- normalized polynomial
- training loss
- validation loss
- training MAE
- validation MAE

**MAE** means **Mean Absolute Error**.
- It is a measurement of **how far the model's predictions are from the actual answers, on average**.

**Mean** → average
**Absolute** → ignore whether the error is positive or negative
**Error** → difference between actual and predicted value
So: **MAE = average of the absolute prediction errors**

---

## 4. `train_test_split`

```python
from sklearn.model_selection import train_test_split
```

### 1. What is it?
A Scikit-learn function that **randomly divides your dataset into separate parts**.

In machine learning, we usually don't want to use **all data for training**.
Instead, we divide the data into:
```text
Dataset
   │
   ├── Training data
   ├── Validation data
   └── Testing data
```

### 2. `train_test_split()` can **randomly select** which samples go into each group.

For example:
```c++
Training:
8  2  5  1  9  4  7  3

Testing:
6  10
```

This helps prevent the split from depending on the original ordering of the dataset.

---

### 3. `x_normalized` and `y_normalized`

- `x_normalized` and `y_normalized` are paired input-answer data. 
- `train_test_split()` randomly divides those pairs into two groups while preserving the pairing. 
- `x_train` contains 80% of the training inputs, and `y_train` contains the correct answers for exactly those inputs. `
- `x_temp` contains the remaining 20% of the inputs, and `y_temp` contains the correct answers for exactly those remaining inputs.

### 4. `random_state`

`random_state` controls **how the random splitting is done**.

#### Without `random_state`
```text
Run 1 → Training: A C D F G H I J
   Test: B E

Run 2 → Training: A B D E F H I J
   Test: C G
```

The groups can change.

#### With `random_state=42`
```text
Run 1 → Training: A C D F G H I J
   Test: B E

Run 2 → Training: A C D F G H I J
   Test: B E

Run 3 → Training: A C D F G H I J
   Test: B E
```

So **random does not mean "different every time."** It means the selection is made using a randomization process; `random_state` lets you **reproduce that same random selection**.

It makes the random split repeatable. The split is still random, but `random_state = 42` ensures that the same samples go into the same groups every time we run the code.

---

## 5. `MinMaxScaler`

```python
from sklearn.preprocessing import MinMaxScaler
```

### What is it?
`MinMaxScaler` is a **data-preprocessing tool** in Scikit-learn that **changes the range of numerical data to a chosen range**.

In your assignment, you use:
```python
MinMaxScaler(feature_range=(-1, 1))
```

So it changes your data so that:
- the **smallest value** becomes `-1`
- the **largest value** becomes `1`
- values between them are converted to values between `-1` and `1`

It uses the **minimum (Min)** and **maximum (Max)** values of the data.
**MinMaxScaler** = a tool that **rescales numerical values using their minimum and maximum values**.

---

## 6. `Sequential`

```python
from tensorflow.keras import Sequential
```

### What is it?
`Sequential` is a Keras model type where layers are arranged **one after another**.

For example, imagine a pipeline:
```text
Input > One layer → next layer → next layer → output.
```

Each step happens **after the previous step**.

A Keras `Sequential` model works the same way. It allows you to build a neural network by putting layers **one after another**.

---

## 7. `Dense, Input`

```python
from tensorflow.keras.layers import Dense, Input
```

These are actual **neural-network building blocks**.

### `Input`

```python
Input(shape=(1,))
```

#### Why is it called `Input`?
Because it represents the **input interface/entry point of the model**.
It tells Keras the expected shape of the data entering the network.

#### What is it?
It tells the network:
> "Each input sample contains one value."

In your assignment, that value is `x`.
```text
  x
  ↓
Input
```

### Understanding `Input(shape=(1,))`

You asked about **`Input(shape=(1,))`** and mainly got confused about **two things**:
1. **`shape=(1,)`** → why there is a comma.
    - `(1,)` is a **one-item Python tuple**.
    - The comma tells Python it is a tuple, not just the number `1`.

2. **How to pass multiple values** → If each sample has multiple features:
    - `shape=(1,)` → 1 feature: `[x]`
    - `shape=(3,)` → 3 features: `[x1, x2, x3]`

So your main confusion was **why the input shape is written as** **`(1,)`** **instead of just** **`1`****, and how that shape changes when there are multiple input features.**

---

### `Dense`

```python
Dense(32, activation="relu")
```

#### What is it?
`Dense` is a type of **neural-network layer** where every neuron is connected to **all neurons in the previous layer**.

Your model has:
```text
32 neurons
64 neurons
128 neurons
1 output neuron
```

These neurons contain **weights and biases** that are adjusted during training.
That's how the DNN learns the polynomial relationship.

#### `Dense` is NOT the name of a hidden layer.

`Dense` is the name of a **layer type**.
Its job is to **define a layer of fully connected neurons**.

So:
```python
Dense(32)
```
means: “Create a fully connected layer containing 32 neurons.”

---

## 8. Evaluation Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
```

These don't build the model. They help you **judge how well the model performed**.

---

### `mean_squared_error`

MSE = Mean Squared Error.
It measures the average **squared difference** between actual and predicted values.

```text
Actual:     10
Predicted:   9

Error = 1
Squared error = 1
```

Your test result was approximately:
```text
MSE = 0.0000005738
```

Very small → good prediction.

---

### `mean_absolute_error`

MAE = Mean Absolute Error.
It measures the average **absolute difference** between actual and predicted values.

Example:
```text
Actual:     10
Predicted:   9

Absolute error = |10 - 9| = 1
```

Your test MAE was approximately:
```text
0.0005535
```

Again, very small.

---

### `r2_score`

R² measures how well the model explains the relationship in the data.

Generally:
```text
R² = 1       → perfect fit
R² ≈ 1       → very good
R² = 0       → poor/no explanatory improvement over baseline
R² < 0       → can be very poor
```

Your result:

```text
R² = 0.999996
```

So your DNN learned the polynomial extremely well on the test data.

---

## 9. Function Definition

```python
def function_name(parameter):
    return result
```

- `def` → defines a function
- `function_name` → function's name
- `parameter` → input to the function
- `:` → starts the function body
- `return` → sends the result back

Example:
```python
def add(x):
    return x + 5
```

Here, `x` is the input, and `x + 5` is the returned result.

---

## 10. `x = np.linspace(-20, 20, 5000).reshape(-1, 1)`

Based on your questions, think of it in **two steps**:

### 1. `np.linspace(-20, 20, 5000)`

Creates **5,000 evenly spaced numbers** from `-20` to `20`:
```text
[-20, -19.99, -19.98, ..., 19.99, 20]
```

So basically, it creates a **1D array of numbers**.

### 2. `.reshape(-1, 1)`

Converts that array into a **table with 1 column and 5,000 rows**:
```text
[-20   ]
[-19.99]
[-19.98]
[ ...  ]
[20    ]
```

- `1` → **1 column**
- `-1` → NumPy automatically calculates the number of rows → **5,000**

---

## 11. Normalizing / Scaling `x` and `y`

This part is **normalizing/scaling both the input** **`x`** **and output** **`y`** before giving them to the DNN.

### 1. Create a scaler for `x`

```python
x_scaler = MinMaxScaler(feature_range=(-1, 1))
```

Means:
> Create a MinMaxScaler that will convert the `x` values into the range **-1 to 1**.

For your `x`:
```text
Original:   -20 ... 0 ... 20
                    ↓
Scaled:      -1 ... 0 ... 1
```

`x_scaler` is the tool that will do this.

---

### 2. Create another scaler for `y`

```python
y_scaler = MinMaxScaler(feature_range=(-1, 1))
```

Same idea, but this scaler is specifically for `y`.
We use **separate scalers** because `x` and `y` have different minimum and maximum values.

---

### 3. Actually scale `x`

```python
x_normalized = x_scaler.fit_transform(x)
```

This does **two things**:
**`fit`** → looks at `x` and learns its minimum and maximum.
**`transform`** → uses those values to convert `x` into `-1` to `1`.

So:
```text
     x
     ↓
find min/max
     ↓
convert to -1 to 1
     ↓
x_normalized
```

---

### 4. Actually scale `y`

```python
y_normalized = y_scaler.fit_transform(y)
```

Same process:
```text
    y
    ↓
find min/max
    ↓
convert to -1 to 1
    ↓
y_normalized
```

So **`fit_transform()`** **is where the actual scaling happens**.

---

## 12. Plotting the Original Polynomial

This code **plots the original polynomial as a graph**.
```python
plt.figure(figsize=(8, 5))
```

Creates a figure/window for the graph. `figsize=(8,5)` sets its size.
```python
plt.plot(x, y)
```

Plots **x on the horizontal axis** and **y on the vertical axis**.
```python
plt.title("Original Polynomial")
```

Sets the graph title.
```python
plt.xlabel("x")
```

Labels the horizontal axis as `x`.
```python
plt.ylabel("y")
```

Labels the vertical axis as `y`.
```python
plt.grid(True)
```

Shows grid lines to make the graph easier to read.
```python
plt.show()
```

Actually **displays the graph**.

---

## 13. `plt.subplot(2, 2, 1)`

The important part:
```python
plt.subplot(2, 2, 1)
```

means:
> **2 rows, 2 columns, and use position 1.**

The positions are:
```text
┌──────────────┬──────────────┐
│      1       │      2       │
├──────────────┼──────────────┤
│      3       │      4       │
└──────────────┴──────────────┘
```

So:
```python
plt.subplot(2, 2, 1)  # Plot 1
plt.subplot(2, 2, 2)  # Plot 2
plt.subplot(2, 2, 3)  # Plot 3
plt.subplot(2, 2, 4)  # Plot 4
```

The general format is:
```text
plt.subplot(number_of_rows, number_of_columns, position)
```

So **`2, 2, 1`** **= 2 rows × 2 columns, position 1**.

#### `len(x_train)`

```python
print("Train:", len(x_train))
```

`len(x_train)` → counts how many samples are in the training data

---

## 14. Building the DNN Architecture

This code **builds your DNN architecture and then displays its structure**.
```python
model = Sequential([
    Input(shape=(1,)),
    Dense(32, activation="relu"),
    Dense(64, activation="relu"),
    Dense(128, activation="relu"),
    Dense(1)
])
```

Think of it as:

```C++
Input: 1 value
          ↓
Dense: 32 neurons   ← hidden layer
          ↓
Dense: 64 neurons  ← hidden layer
          ↓
Dense: 128 neurons ← hidden layer
          ↓
Dense: 1 neuron    ← output
```

- `Sequential` → puts the layers **one after another**
- `Input(shape=(1,))` → each sample has **1 input feature**
- `Dense(32)` → creates a fully connected layer with **32 neurons**
- `Dense(64)` → 64 neurons
- `Dense(128)` → 128 neurons
- `Dense(1)` → 1 output neuron, which gives the predicted `y`
- `activation="relu"` → uses ReLU as the activation function in the hidden layers

---

### 15. `model.summary()`

```python
model.summary()
```

This **does not train the model**.

It simply asks Keras:
> **“Show me the structure/details of my model.”**

It displays things such as:
```text
Layer       Output Shape       Parameters
Input       (None, 1)              0
Dense       (None, 32)            64
Dense       (None, 64)           2112
Dense       (None, 128)          8320
Dense       (None, 1)            129
```

So you can check **what layers exist, how many neurons they have, and how many trainable parameters the network contains**.

---

## 15. Understanding `None` in `model.summary()`

In your `model.summary()`, you see something like:
```text
Input    (None, 1)
Dense    (None, 32)
```

The **`None`** **means the number of samples (batch size) is not fixed**.

For example, your model can receive:
```text
10 samples → shape (10, 1)
32 samples → shape (32, 1)
100 samples → shape (100, 1)
```

The model only specifies:
```text
(None, 1)
   ↑   ↑
   │   └── 1 feature
   └────── any number of samples
```

So **`None`** **does NOT mean missing data or zero**. It means:
> **“The number of samples can vary.”**

This is useful because you don't have to build a separate model for different batch sizes.

---

## 16. `model.compile()`

This part **configures how the DNN will learn and how its performance will be measured**. It does **not train the model yet**.

```python
model.compile(
    optimizer = "adam",
    loss      = "mse",
    metrics   = ["mae"]
)
```

Think of it as telling the model:
> **How should you learn, what should you minimize, and what should I measure?**

---

### 1. `optimizer="adam"`

**Optimizer** decides **how the model changes its weights to reduce the error**.

`adam` is the name of a popular optimization algorithm.

Adam is popular because it is a good general-purpose default and often works well without much manual tuning.

#### Common optimizers

| Optimizer    | Basic idea                                       |
| ------------ | ------------------------------------------------ |
| **SGD**      | Basic gradient-based weight updates              |
| **Momentum** | SGD + keeps some direction from previous updates |
| **RMSprop**  | Adjusts learning step based on recent gradients  |
| **Adam**     | Combines ideas from Momentum + RMSprop           |
| **AdamW**    | Adam with improved weight decay handling         |

Simple idea:
```text
  Prediction
      ↓
Calculate error
      ↓
Adam adjusts weights
      ↓
 Better prediction
```

---

### 2. `loss="mse"`

**Loss** tells the model **what error it should try to minimize during training**.

`mse` = **Mean Squared Error**

It calculates the average of:
```text
(actual−predicted)2
(actual - predicted)^2
```

Your DNN tries to make this value as **small as possible**.

There are many loss functions:
```text
Loss function
│
├── MSE
├── MAE
├── Huber Loss
├── Binary Cross-Entropy
├── Categorical Cross-Entropy
└── ...
```

#### Common choices:

|Loss|Usually used for|
|---|---|
|**MSE**|Regression|
|**MAE**|Regression|
|**Huber**|Regression, especially with outliers|
|**Binary Cross-Entropy**|Binary classification|
|**Categorical Cross-Entropy**|Multi-class classification|

For **your polynomial regression**, MSE is a very common choice.

---

### 3. `metrics=["mae"]`

`metrics` tells Keras what additional measurement to show while training.

`mae` = **Mean Absolute Error**

It calculates:
```text
∣actual−predicted∣
|actual - predicted|
```

So your model uses:
```text
MSE → what the model tries to minimize
MAE → additional error measurement we want to see
```

#### Metrics
`metrics=["mae"]` means you're choosing **MAE as a metric to monitor**.

There are also many metrics:
```text
Metrics
│
├── MAE
├── MSE
├── RMSE
├── R²
├── Accuracy
├── Precision
├── Recall
└── ...
```

##### Common choices:

|Metric|Usually used for|
|---|---|
|**MAE**|Regression|
|**MSE**|Regression|
|**RMSE**|Regression|
|**R²**|Regression|
|**Accuracy**|Classification|
|**Precision / Recall**|Classification|

#### In short
```text
optimizer="adam" → HOW the model learns
loss="mse"       → WHAT error it tries to minimize
metrics=["mae"]  → WHAT additional error we want to monitor
```

---

## 17. `model.fit()` — Actual Training

This is the **actual training step** of your DNN.
```python
history = model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_data=(x_val, y_val),
    verbose=1
)
```

Think of `model.fit()` as:

> **“Train this model using these inputs and answers, for this many rounds, with this batch size, while checking validation performance.”**

---

### 1. `x_train`

```python
x_train
```

These are the **training inputs**.

In your case, they are the normalized `x` values.
```text
x_train → input to DNN
```

---

### 2. `y_train`

```python
y_train
```

These are the **correct answers** corresponding to `x_train`.
```text
x_train → DNN → predicted y
                    ↓
              compare with y_train
                    ↓
                 calculate MSE
                    ↓
              update weights
```

So:
```text
x_train = questions
y_train = correct answers
```

---

### 3. `epochs=100`

An **epoch** means going through the entire training dataset once.

Epoch = the number of times the model goes through the entire training dataset during training.

You have **4,000 training samples**.
```text
Epoch 1 → model sees all 4,000 samples
Epoch 2 → model sees all 4,000 samples again
...
Epoch 100 → model sees all 4,000 samples again
```

So the model gets **100 complete passes** through the training data.

---

### 4. `batch_size=32`

Instead of giving all 4,000 samples to the model at once, it processes them in groups of **32**.
```text
4000 training samples

[32] [32] [32] [32] ... [32]
```

Approximately:
```text
4000/32 = 125
```

So one epoch has **125 batches**.

After processing a batch, the optimizer updates the model's weights.

Batch size = how many training samples the model processes in one step before updating its weights.

---

### 5. `validation_data=(x_val, y_val)`

This gives the model **validation data** to check its performance during training.

Your validation set has **500 samples**.
```text
Training:
x_train + y_train
       ↓
   update weights

Validation:
x_val + y_val
       ↓
   check performance
```

**Validation data is not used to update the weights.**

It helps you see whether the model is learning well on data it wasn't trained on.

---

## 18. Training Data vs Validation Data

The validation data is **not used to train/update the weights**.

It is basically a **check**:

> "After learning from the training data, how well does the model perform on data it didn't learn from?"

Exactly — this is the key idea. **Training data adjusts the weights; validation data only checks the result.**

Here is the actual process for **one batch**:
```text
1. Take 32 training samples
            ↓
2. DNN uses current weights
            ↓
3. Produce predictions
            ↓
4. Compare predictions with actual y_train
            ↓
5. Calculate MSE (loss)
            ↓
6. Backpropagation calculates how each weight contributed to the error
            ↓
7. Adam uses that information to change the weights
            ↓
8. Move to the next batch
```

### So who does what?

**Loss (MSE):**
> Measures **how wrong the prediction is**.

**Backpropagation:**
> Calculates **how each weight should change to reduce that error**.

**Optimizer (Adam):**
> Actually **updates the weights** based on those calculated changes.

So:
```text
Prediction
    ↓
MSE → "How wrong are we?"
    ↓
Backpropagation → "Which weights caused the error and
                    in which direction should they change?"
    ↓
Adam → "Okay, I'll update those weights."
```

---

## 19. When Does Training and Validation Happen?

Because your:
```python
batch_size = 32
```

you have about **125 batches per epoch**:
```text
Batch 1  → calculate error → update weights
Batch 2  → calculate error → update weights
Batch 3  → calculate error → update weights
...
Batch 125 → calculate error → update weights
                         ↓
                    1 epoch done
```

Then it starts another epoch using the **updated weights**.
```text
Epoch 2
   ↓
Training → update weights
   ↓
Validation → only check
```

So the simplest rule to remember is:
> **Training → calculate error → adjust weights.**
> **Validation → calculate error → don't adjust weights.**

---

## 20. Complete Understanding of One Epoch

For your example:
```text
4,000 training samples
batch_size = 32
epochs = 100
```

### Epoch 1

The model takes 32 samples:
```text
32 x values + 32 target y values
        ↓
     predict y
        ↓
     calculate MSE
        ↓
   backpropagation
        ↓
   Adam updates weights
```

Then it takes the **next 32 samples** and does the same thing.
```text
Batch 1 → predict → error → update weights
Batch 2 → predict → error → update weights
Batch 3 → predict → error → update weights
...
Batch 125 → predict → error → update weights
```

After approximately **125 batches**, all 4,000 training samples have been processed.

➡️ **Epoch 1 is complete.**

### Then Epoch 2

It starts again with the training data:
```text
Batch 1 → 32 samples → predict → error → update weights
Batch 2 → 32 samples → predict → error → update weights
...
Batch 125 → 32 samples → predict → error → update weights
```

➡️ **Epoch 2 is complete.**

And this continues:
```text
Epoch 1
Epoch 2
Epoch 3
...
Epoch 100
```

#### One important correction

When you say:
> "train, then check loss, then update"

More precisely:
```text
32 inputs + targets
       ↓
Forward pass → prediction
       ↓
Calculate loss (MSE)
       ↓
Backpropagation → calculate weight gradients
       ↓
Adam → update weights
```

The **loss is calculated before the weight update**, and the optimizer uses the gradient information to decide how to update the weights.

Then the next 32 samples use the **newly updated weights**.

So your understanding is essentially:
> **Take 32 samples → calculate prediction/error → update weights → take the next 32 → repeat 125 times → epoch finished → start again with updated weights → repeat until 100 epochs.**

---

## 21. How the Model Learns from Initial Weights

Initially, the model has **randomly initialized weights**, so its first prediction is usually not accurate.

For example:
```text
Input x = 5
Actual y = 285

Initial model:
x = 5 → prediction = 100
```

Then:
```text
Prediction = 100
Actual     = 285
              ↓
        calculate error
              ↓
     backpropagation
              ↓
       Adam adjusts weights
```

Now the model has **slightly better weights**.

Next batch:
```text
New 32 inputs
      ↓
Use the UPDATED weights
      ↓
Make predictions
      ↓
Calculate error
      ↓
Adjust weights again
```

And it keeps repeating:
```text
Predict
  ↓
Measure error
  ↓
Adjust weights
  ↓
Predict again with improved weights
  ↓
Measure error
  ↓
Adjust again
  ↓
...
```

So the core idea of training is:
> **The model makes predictions, measures how wrong they are, adjusts its weights to reduce the error, and then makes better predictions using those updated weights.**

---

## 22. `verbose=1`

This controls how much training information Keras displays.
```python
verbose=0  # show nothing
verbose=1  # show progress bar
verbose=2  # show one line per epoch
```

You use:
```python
verbose=1
```

so you'll see something like:
```text
Epoch 1/100
125/125 ━━━━━━━━━ ... loss: ...
Epoch 2/100
125/125 ━━━━━━━━━ ... loss: ...
...
```

---

## 23. Why `history =`?

`model.fit()` returns a **History object** containing the training results.

The **`history`** **object** comes from this line:
```python
history = model.fit(...)
```

### What is `history`?

When `model.fit()` trains your model, Keras **keeps a record of what happened during each epoch**.

That record is returned as a **History object**.

Think of it like a **training diary**:
```text
history
│
├── Epoch 1 → loss, MAE, val_loss, val_MAE
├── Epoch 2 → loss, MAE, val_loss, val_MAE
├── Epoch 3 → loss, MAE, val_loss, val_MAE
│
...
│
└── Epoch 100 → loss, MAE, val_loss, val_MAE
```

### What is inside it?

You can access the recorded values using:
```python
history.history
```

This is basically a **dictionary** containing lists of values.

For your model, you'll have things like:
```python
history.history["loss"]
history.history["mae"]
history.history["val_loss"]
history.history["val_mae"]
```

For example:
```text
history.history["mae"]

→ [0.25, 0.18, 0.12, ..., 0.001]
```

Each value corresponds to an epoch:
```text
Epoch 1 → 0.25
Epoch 2 → 0.18
Epoch 3 → 0.12
...
```

#### So this line:
```python
plt.plot(history.history["mae"])
```

means:
> **Go into the training history → get the recorded MAE values → plot them.**

And:
```python
plt.plot(history.history["val_mae"])
```

means:
> **Go into the training history → get the recorded validation MAE values → plot them.**

#### Very simply
```text
model.fit()
    ↓
trains model
    ↓
records results from each epoch
    ↓
returns History object
    ↓
history
    ↓
history.history["mae"]
history.history["val_mae"]
```

So **`history`** **doesn't contain the trained model itself**. It mainly contains the **training progress/results recorded during** **`fit()`**.

---

## 24. `model.evaluate()` — Final Test Evaluation

This code is the **final evaluation of your trained model using the test data**.
```python
test_loss, test_mae = model.evaluate(x_test, y_test, verbose=0)

print("Test MSE:", test_loss)
print("Test MAE:", test_mae)
```

Let's break it down.

### 1. `model.evaluate()`

```python
model.evaluate(x_test, y_test, verbose=0)
```

`evaluate()` asks:
> **"After training is finished, how well does my model perform on the test data?"**

Your test data contains:
```text
x_test → 500 inputs
y_test → 500 correct answers
```

The model takes `x_test` and predicts:
```text
x_test
   ↓
trained model
   ↓
predicted y
```

Then Keras compares the predicted `y` with the actual `y_test`.

---

### 2. `x_test, y_test`

```python
model.evaluate(x_test, y_test, ...)
```

These are the **test inputs and their correct target values**.

For example, conceptually:
```text
x_test       y_test
  5            285
  2             -?
  10           4510
  ...
```

The model predicts values from `x_test`, then compares them with `y_test`.

Importantly, these are **normalized values** in your code because you split `x_normalized` and `y_normalized`.

---

### 3. What does `evaluate()` return?

You compiled the model with:
```python
model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)
```

So `evaluate()` returns:
```text
loss → MSE
metric → MAE
```

That's why you write:
```python
test_loss, test_mae = ...
```

The returned values are assigned like:
```text
test_loss  ← MSE
test_mae   ← MAE
```

So if you get:
```text
Test MSE: 0.0000005738
Test MAE: 0.0005535
```

it means:
```text
Test MSE = 0.0000005738
Test MAE = 0.0005535
```

---

### 4. Why `verbose=0`?

```python
verbose=0
```

means:

> **Don't show the evaluation progress/output while evaluating.**

So:

```python
model.evaluate(x_test, y_test, verbose=0)
```

runs quietly.

If you used:

```python
verbose=1
```

Keras could show a progress bar.

---

### 5. Then the `print()` statements

```python
print("Test MSE:", test_loss)
```

prints the MSE obtained from the test set.

And:
```python
print("Test MAE:", test_mae)
```

prints the MAE obtained from the test set.

---

### The whole process

```text
Model was already trained
          ↓
      x_test
          ↓
    trained model
          ↓
   predicted values
          ↓
compare with y_test
          ↓
 ┌────────┴────────┐
 ↓                 ↓
MSE               MAE
 ↓                 ↓
test_loss       test_mae
```

### One important distinction

`evaluate()` **does not train the model again**.

It only **checks the already-trained model** using the test data.

So:
```python
model.fit(...)       # TRAIN
model.evaluate(...)  # TEST/EVALUATE
```

In your assignment, this gives you the final answer to:

> **"How accurately does my trained DNN predict unseen test data?"**

---

## 25. Understanding `evaluate()` More Clearly

`evaluate()` does this:

```text
Already-trained model
        ↓
Give it ALL test data
(500 test samples)
        ↓
Model makes predictions
        ↓
Compare predictions with actual y_test
        ↓
Calculate MSE and MAE
        ↓
Return the measurements
```

So:
```python
test_loss, test_mae = model.evaluate(x_test, y_test, verbose=0)
```

means:
> **Run the trained model in prediction/evaluation mode on all 500 test samples, compare its predictions with the correct test answers, and calculate the MSE and MAE to measure how well the model performs.**

#### Important difference from training

During `fit()`:
```text
prediction → error → backpropagation → update weights
```

During `evaluate()`:
```text
prediction → error → calculate MSE/MAE
                         ↓
                    NO weight update
```

So **the model is used again, but it does not learn anything new from the test data**. The test set is only used to measure the final performance.

---

## 26. `predict()` and R² Score

This part is another **way of measuring how well the trained model predicts the test data**, but this time you're calculating **R² Score**.

```python
y_pred = model.predict(x_test, verbose=0)

r2 = r2_score(y_test, y_pred)

print("R² Score:", r2)
```

---

### 1. `model.predict(x_test)`

```python
y_pred = model.predict(x_test, verbose=0)
```

This means:
> Give all the test inputs to the trained model and get its predicted outputs.

So:
```text
x_test
  ↓
trained DNN
  ↓
predicted values
  ↓
y_pred
```

For example, conceptually:
```text
Actual y       Predicted y
  285             284.9
  120             120.1
  500             499.8
  ...
```

`y_pred` contains the model's predictions for all 500 test samples.

Just like `evaluate()`, **this does not update the weights**. It only predicts.

---

### 2. `r2_score(y_test, y_pred)`

```python
r2 = r2_score(y_test, y_pred)
```

Here you're asking:
> **How well do my predicted values explain/match the actual values compared with simply predicting the average?**

`r2_score()` comes from Scikit-learn:
```python
from sklearn.metrics import r2_score
```

It calculates the **R² score (coefficient of determination)**.

Generally:
```text
R² = 1       → perfect prediction
R² ≈ 1       → very good
R² = 0       → roughly no better than predicting the average
R² < 0       → worse than predicting the average
```

Your result:
```text
R² ≈ 0.999996
```

is extremely close to `1`, meaning your DNN's predictions are **very close to the actual polynomial values on the test set**.

---

### Why do we need this if we already calculated MSE and MAE?

They're different measurements:
```text
evaluate()
   ↓
MSE + MAE

predict()
   ↓
predicted values (y_pred)

r2_score()
   ↓
R²
```

So your assignment is using **three different performance measures**:

|Measure|What it tells you|
|---|---|
|**MSE**|Average squared prediction error|
|**MAE**|Average absolute prediction error|
|**R²**|How well the model explains the variation in the target|

#### The key difference

`evaluate()`:
> **"Calculate MSE and MAE for my test data."**

`predict()`:
> **"Give me the actual predictions made by my model."**

`r2_score()`:
> **"Using those predictions, calculate how well the model fits the actual test values."**

So the sequence is:
```text
x_test
  ↓
model.predict()
  ↓
y_pred
  ↓
compare y_pred with y_test
  ↓
r2_score()
  ↓
R² ≈ 0.999996
```

And again, **nothing is learned or updated here**. This is purely evaluation after training.

---

# 27. Single Real-World Example Prediction

This part is doing a **single real-world example prediction** after the model has already been trained.

The goal is:
> **Give the trained DNN** **`x = 5`****, get its predicted** **`y`****, convert that prediction back to the original scale, calculate the actual** **`y`****, and compare them.**

Let's go line by line.

---

### 1. Create one input value

```python
x_example = np.array([[5.0]])
```

You're creating one input:
```text
x = 5
```

But notice the shape:
```text
[[5.0]]
```

It is a **2D array with shape** **`(1, 1)`**:
```text
1 sample
   ↓
[ 5.0 ]
```

This format matches your model's expected input:
```python
Input(shape=(1,))
```

---

### 2. Normalize `x = 5`

```python
x_example_normalized = x_scaler.transform(x_example)
```

Remember, during training you normalized `x` from its original range into `[-1, 1]`.
So the model was trained using **normalized x values**, not the original `5`.

Therefore, before giving `5` to the model, you must use the **same scaler**:
```text
Original x = 5
      ↓
x_scaler.transform()
      ↓
Normalized x
```

#### Why `transform()` instead of `fit_transform()`?

Because the scaler has **already learned the min/max values** from your original dataset.
You don't want to calculate new scaling rules for `5`.

So:
```python
x_scaler.transform(x_example)
```

means:
> Use the already-learned scaling rules to convert this new input.

---

### 3. Ask the trained model to predict

```python
y_pred_normalized = model.predict(
    x_example_normalized,
    verbose=0
)
```

Now the normalized `x = 5` goes into the trained DNN:
```text
x = 5
 ↓
normalize
 ↓
x_normalized
 ↓
trained DNN
 ↓
predicted normalized y
```

The important thing is that the model's output is also **normalized**, because you trained the model using `y_normalized`.

So:
```text
y_pred_normalized
```

is **not yet the original y value**.

---

### 4. Convert predicted y back to the original scale

```python
y_pred_actual = y_scaler.inverse_transform(y_pred_normalized)
```

This is very important.
Your model predicts a normalized value, but you want the answer in the original scale.

So `inverse_transform()` does the opposite of normalization:
```text
Normalized predicted y
        ↓
y_scaler.inverse_transform()
        ↓
Original predicted y
```

For example, your result was approximately:
```text
Predicted y ≈ 290.4
```

So now you have a prediction in the same scale as the original polynomial.

---

### 5. Calculate the actual answer

```python
actual_y = polynomial(x_example)
```

This doesn't use the DNN.

It directly uses your original equation:
```text
y = 5x³ − 10x² − 20x + 10
```

For `x = 5`:
```text
y = 5(5³) − 10(5²) − 20(5) + 10
  = 625 − 250 − 100 + 10
  = 285
```

So:
```text
Actual y = 285
```

This gives us the **correct answer** to compare against the DNN's prediction.

---

### 6. `x_example[0, 0]`

```python
print("Input x:", x_example[0, 0])
```

Why `[0, 0]`?

Because:
```python
x_example
```

looks like:
```text
[[5.0]]
```

It has:
```text
row 0
  ↓
[ column 0 ]
    ↓
    5.0
```

So:
```python
x_example[0, 0]
```

means:
> Get the value at row 0, column 0.

Result:
```text
5.0
```

---

### 7. Get the predicted value

```python
print("Predicted y:", y_pred_actual[0, 0])
```

Again, `y_pred_actual` is a 2D array containing one prediction:
```text
[[290.4]]
```

So `[0, 0]` extracts the actual number:
```text
290.4
```

---

### 8. Get the actual value

```python
print("Actual y:", actual_y[0, 0])
```

The polynomial calculated:
```text
[[285]]
```

So `[0, 0]` gives:
```text
285
```

---

### 9. Calculate absolute error

```python
abs(y_pred_actual[0, 0] - actual_y[0, 0])
```

This calculates:
```text
|Predicted - Actual|
```

With your result:
```text
|290.402 - 285|
```

≈
```text
5.402
```

So:
```text
Absolute Error ≈ 5.402
```

---

## 10 Whole Process of the Single Example

This is the easiest way to understand this entire block:

```text
             x = 5
               ↓
        Normalize x
               ↓
      x_normalized
               ↓
        Trained DNN
               ↓
    Predicted normalized y
               ↓
      Inverse normalize
               ↓
     Predicted y ≈ 290.4
               │
               │ compare
               ↓
     Actual y = 285
               ↓
     Absolute Error ≈ 5.4
```

### In one sentence

> **This code takes a new input** **`x=5`****, prepares it exactly like the training data, gives it to the trained DNN, converts the prediction back to the original scale, calculates the true answer using the original polynomial, and measures how far the prediction is from the true answer.**

One interesting point in your assignment: **the overall test metrics are extremely good, but this particular** **`x=5`** **prediction has a noticeably larger error (~5.4)**. That's not necessarily contradictory; the test metrics summarize the whole test set, while this code checks just one individual point.

---





