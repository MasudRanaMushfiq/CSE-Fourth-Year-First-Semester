

# CNN-Based MNIST Image Classification

---

## 1. `from tensorflow.keras.datasets import mnist`

```python
from tensorflow.keras.datasets import mnist
```

### What is MNIST?

**MNIST** stands for:
> **Modified National Institute of Standards and Technology**

It is a famous dataset used in **machine learning and computer vision** for recognizing **handwritten digits from 0 to 9**.

Think of it as a huge collection of handwritten digit images, where each image already has the correct answer attached to it.

### How much data does MNIST have?

The standard MNIST dataset contains:

| Dataset  | Number of images |
| -------- | ---------------- |
| Training | **60,000**       |
| Testing  | **10,000**       |
| Total    | **70,000**       |

Each image is `28 × 28` grayscale.

---

## 2. `from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout`

```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
```

This imports different neural network layers.

### `Conv2D`
**Conv2D (2D Convolution)** is a CNN layer that scans an image using small filters to **extract important features** like edges, lines, and shapes.

#### Why use it?
We use Conv2D to **automatically detect useful patterns in images**, making it easier for the CNN to classify them.

```python
Conv2D
```

Used to detect features from images, such as:
- Edges
- Lines
- Curves
- Shapes

---

### `MaxPooling2D`

```python
MaxPooling2D
```

Used to reduce the size of the feature map.

Example:
```python
MaxPooling2D(pool_size=(3, 3), strides=(1, 1))
```

It takes the **maximum value** from each pooling region.

Benefits:
- Reduces data size
- Reduces computation
- Keeps important features

---

### `Flatten`

```python
Flatten()
```

Converts a **multi-dimensional feature map into a one-dimensional array**.

For example:
```text
Feature Map
3 × 3 × 64
        ↓
Flatten
        ↓
576 values
```

This allows the CNN output to be connected to a `Dense` layer.

---

### `Dense`

```python
Dense
```

A fully connected neural network layer.

---

### `Dropout`

```python
Dropout
```

#### What is Dropout?
**Dropout** is a technique that randomly turns off some neurons during training.

#### Why use Dropout?
It helps **prevent overfitting**, so the model performs better on new/unseen data.

Example:

```python
Dropout(0.5)
```

means roughly **50% of neurons are randomly ignored during each training step**.

Example:
```text
Without Dropout:
Training Accuracy = 99%
Testing Accuracy  = 90%

Possible overfitting
```

Dropout can help the model generalize better to unseen test data.

---

## 3. `from tensorflow.keras.callbacks import EarlyStopping`

```python
from tensorflow.keras.callbacks import EarlyStopping
```

`EarlyStopping` automatically stops training when the model is no longer improving.

Example:
```python
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)
```

#### Meaning:
- `monitor="val_loss"` → Watches the validation/testing loss.
- `patience=3` → Waits for 3 epochs without improvement.
- `restore_best_weights=True` → Restores the model weights from the best epoch.

For example:
```text
Epoch 1 → val_loss improves ✓
Epoch 2 → val_loss improves ✓
Epoch 3 → val_loss improves ✓
Epoch 4 → No improvement
Epoch 5 → No improvement
Epoch 6 → No improvement

Training stops
```

---

## 4. Loading the MNIST Dataset

```python
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

`mnist.load_data()` gives you **four things**:

```text
X_train → 60,000 training images  (each is 28×28 pixels)
y_train → 60,000 correct labels   (0–9)
X_test  → 10,000 testing images
y_test  → 10,000 correct labels
```

**Analogy:** Imagine 60,000 flashcards showing handwritten digits, each with the answer written on the back. You study 60,000 of them, then take a test on 10,000 new ones.

Why 28×28? Because each image is a small grid of 28 rows and 28 columns of pixels. Pixel values range from **0 (black)** to **255 (white)**.

**The first time you run:**

```python
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

Keras will download the MNIST dataset from the internet **if it isn't already cached on your computer**. It then saves it locally, so you normally don't need to download it again.

### How much?

The MNIST dataset is approximately:
- **Download size:** ~**11 MB**
- **Dataset after extraction:** ~**21 MB**

It contains:
```text
60,000 training images
10,000 testing images
```

Each image is `28 × 28` grayscale.

---

## 5. Displaying the First 5 Training Images

```python
plt.figure(figsize=(10, 2))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')

plt.show()
```

This is **visual inspection** — you're checking that the data loaded correctly.

Breaking it down:
- `plt.figure(figsize=(10, 2))` → creates a wide canvas **10 inches wide and 2 inches high**.
- `plt.subplot(1, 5, i+1)` → makes 5 slots in a single row
- `plt.imshow(X_train[i], cmap='gray')` → shows the image in grayscale
- `plt.title(f"Label: {y_train[i]}")` → puts the correct answer above each image
- `plt.axis('off')` → hides the axis numbers
- `plt.show()` → actually displays it

You should see 5 handwritten digits with labels like **5, 0, 4, 1, 9**.

---

## 6. Normalization

```python
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
```

**What's happening?**
Pixel values were originally **0–255**. Neural networks learn better when inputs are small, so we convert them into **0 – 1**.

```text
Before:  0, 128, 255
After:   0.0, 0.502, 1.0
```

Why `float32`?
Because neural networks do math with decimals. Division creates decimals, so we convert first.
`astype("float32")` converts the pixel data to floating-point numbers so the division produces suitable numerical inputs for the model.

**Why normalize both training and testing?** So the model sees the same scale in both. If you only normalized the training data, the model would be confused during testing.

---

## 7. Reshaping for CNN

```python
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
```

Original shape: `(60000, 28, 28)` → no channel info
New shape: `(60000, 28, 28, 1)` → has a channel dimension

**Why the extra 1?**
CNNs expect 4D input: `(number of images, height, width, channels)`.

- **Grayscale** images → 1 channel (this is MNIST)
- **RGB** images → 3 channels
- **RGBA** images → 4 channels

The `-1` means **"figure out the number automatically"** (it becomes 60000). Reshaping doesn't change the pixel values — it only changes how they're organized.

---

## 8. Building the CNN Model

```python
model = Sequential([
    Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),

    Conv2D(64, 3, activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),

    Dense(128, activation='relu'),
    Dropout(0.5),

    Dense(10, activation='softmax')
])
```

Let's walk through what each layer does:

### First Conv2D (Convolution Layer)

```python
Conv2D(32, 3, activation='relu', input_shape=(28,28,1))
```

- **32 filters** → looks for 32 different patterns (edges, curves, etc.)

### What does `32` mean?

`32` means the CNN automatically creates **32 different learnable filters (kernels)**.

Each filter learns to detect a **different feature/pattern** from the image.

For example:
```text
Filter 1  → vertical edges
Filter 2  → horizontal edges
Filter 3  → diagonal edges
Filter 4  → curves
...
Filter 32 → some other learned pattern
```

**But:** these are just examples. You don't tell the CNN what each filter should detect. The filters' weights are **automatically learned during training**.

- **3** → uses a 3×3 sliding window (Kernel Size)
- **relu** → converts negatives to 0, keeps positives
- **input_shape** → expects 28×28 grayscale

This layer **scans the image** and learns patterns, like edges and lines.

Keep in mind that `input_shape` is normally specified only for the **first layer** because subsequent layers get their input automatically from the previous layer.

### First MaxPooling2D

```python
MaxPooling2D((2, 2))
```

Uses a 2×2 window and **takes the maximum** in each block. This shrinks the image by half, keeping only the strongest signals.

### Second Conv2D

```python
Conv2D(64, 3, activation='relu')
```

Now it learns **more complex patterns** — combinations of curves and lines. The 32 filters become **64 filters** (more capacity).

### Second MaxPooling2D

```python
MaxPooling2D((2, 2))
```

Shrinks again. After this, the image is only 5×5 with 64 channels.

### Flatten

```python
Flatten()
```

Converts the 5×5×64 = 1600 features into a **single 1D list** of 1600 numbers. Dense layers can't process 2D data — they need a flat list.
`Flatten()` needs no arguments because it automatically reads the previous layer's shape and converts all values into a single 1D vector.

### Dense(128)

```python
Dense(128, activation='relu')
```

Fully connected layer with 128 neurons. It looks at the 1600 extracted features and learns how to **combine them** to classify digits.

### Dropout(0.5)

```python
Dropout(0.5)
```

**Randomly turns off 50% of neurons during training.** This forces the network to not rely too heavily on any single neuron. It reduces **overfitting** (memorizing training data).

During testing/prediction, dropout is turned off automatically.

### Dense(10, softmax)

```python
Dense(10, activation='softmax')
```

The **final layer** — 10 neurons (one for each digit 0–9). Softmax produces **probabilities**:

```text
Digit 0 → 0.01
Digit 1 → 0.02
...
Digit 5 → 0.87   ← highest probability → predict "5"
...
Digit 9 → 0.02
```

The highest probability becomes the prediction.

### Softmax Output

The final **10 neurons** represent the **10 digits (0–9)**.

**Softmax** gives each neuron a probability showing how likely the input is to be that digit.

```text
10 neurons → 10 probabilities → highest probability = prediction
```

For example:

```text
[0.01, 0.02, 0.05, 0.80, 0.03, ...]
                  ↑
              highest
```

The highest value is at **index 3**, so the model predicts **digit 3**.

---

## 9. `model.summary()`

```python
model.summary()
```

This is the same idea as Assignment 01 — it **shows the structure** of your model:

| Layer        | Output Shape        | Parameters |
| ------------ | ------------------- | ---------- |
| Conv2D       | (None, 26, 26, 32)  | 320        |
| MaxPooling2D | (None, 13, 13, 32)  | 0          |
| Conv2D       | (None, 11, 11, 64)  | 18,496     |
| MaxPooling2D | (None, 5, 5, 64)    | 0          |
| Flatten      | (None, 1600)        | 0          |
| Dense        | (None, 128)         | 204,928    |
| Dropout      | (None, 128)         | 0          |
| Dense        | (None, 10)          | 1,290      |

**Total: 225,034 parameters.**

### Understanding the Output Shapes

- `(None, 26, 26, 32)` → `None` = batch size (unknown), `26×26` = smaller because 3×3 filter removes edges, `32` = filters
- Pooling **halves** the size: `26 → 13`
- Second conv shrinks `13 → 11`
- Second pooling shrinks `11 → 5`
- Flatten turns `5×5×64 = 1600` into a single vector
- Dense has 128 neurons
- Final Dense has 10 outputs

---

## 10. Compiling the Model

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

| Component  | Value                            | What it does                    |
| ---------- | -------------------------------- | ------------------------------- |
| `optimizer`| `'adam'`                         | HOW the model updates weights   |
| `loss`     | `sparse_categorical_crossentropy`| WHAT error to minimize          |
| `metrics`  | `['accuracy']`                   | WHAT to monitor                 |

### Why sparse categorical crossentropy?

**Why use it for MNIST?**
MNIST is a **multi-class classification** problem with **10 classes: 0–9**.

The labels are stored as **integers**:
```text
0, 1, 2, 3, ..., 9
```

So we use:
```python
loss='sparse_categorical_crossentropy'
```

**Concept:** It compares the model's predicted probabilities with the **actual digit label** and calculates how wrong the prediction is.

### `metrics=['accuracy']`

We use **accuracy** to see how many predictions are correct.

Example:
```text
1000 test images
950 predicted correctly
```

Accuracy:

```text
950 / 1000 = 95%
```

---

## 11. EarlyStopping Callback

```python
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)
```

**Purpose:** Stop training if the model stops improving, to prevent overfitting.

| Parameter              | Value        | Meaning                                  |
| ---------------------- | ------------ | ---------------------------------------- |
| `monitor`              | `'val_loss'` | Watch validation loss                    |
| `patience`             | `3`          | Allow 3 epochs of no improvement         |
| `restore_best_weights` | `True`       | Keep the best version of the model       |
| `verbose`              | `1`          | Print a message when stopping            |

**Example scenario:**

```text
Epoch 1 → val_loss = 0.10 ✓ improves
Epoch 2 → val_loss = 0.07 ✓ improves
Epoch 3 → val_loss = 0.05 ✓ improves (best)
Epoch 4 → val_loss = 0.06 ✗ no improvement (1)
Epoch 5 → val_loss = 0.07 ✗ no improvement (2)
Epoch 6 → val_loss = 0.08 ✗ no improvement (3)
→ Training stops, best weights from Epoch 3 restored
```

This is **just like** Assignment 01's concept of early stopping — but this time you're directly using Keras's `EarlyStopping` callback (which you also used in Assignment 01).

---

## 12. Training the Model

```python
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)
```

Same idea as Assignment 01's `model.fit()`. Let's break it down:

| Parameter            | Value          | Meaning                                     |
| -------------------- | -------------- | ------------------------------------------- |
| `X_train`            | images         | The training inputs                         |
| `y_train`            | labels         | The correct answers                         |
| `epochs=20`          | 20             | Max 20 passes through data                  |
| `batch_size=64`      | 64             | 64 images per weight update                 |
| `validation_split=0.2`| 20%           | Reserve 20% of training data for validation |
| `callbacks=[early_stop]`| —           | Apply early stopping                        |
| `verbose=1`          | —              | Show progress bar                           |

### About validation_split

**60,000 training images → 48,000 training + 12,000 validation**

```text
X_train (60,000)
       ↓
  80% for actual training → 48,000
  20% for validation      → 12,000
```

The **validation set is NOT used to update weights** — it's just a check to see how the model performs on data it hasn't been directly trained on. Same principle as Assignment 01.

### About batch_size

64 images processed per weight update. With 48,000 training images, that's 750 batches per epoch.

### What actually happens

```text
For each batch of 64 images:
    Forward pass → predictions
    Calculate loss
    Backpropagation → gradients
    Adam updates weights
    Move to next batch
```

Repeat 750 times per epoch.

### After 11 epochs

The model stopped at Epoch 11 (early stopping triggered), and the best weights from **Epoch 8** were restored.

---

## 13. Evaluating on Test Data

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("\nTest Accuracy:", test_accuracy)
print("Test Loss:", test_loss)
```

**This is the final exam.** The model has never seen `X_test` before. This is a fair test of its real performance.

Output:

```text
Test Accuracy: 0.9911  (99.11%)
Test Loss: 0.0276
```

**99.11% accuracy** — the model correctly classifies 99.11% of unseen handwritten digits.

---

## 14. Plotting Training vs Validation Accuracy

```python
plt.figure(figsize=(8,5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()
```

Same idea as Assignment 01 — `history` holds the training diary.

- `history.history['accuracy']` → training accuracy per epoch
- `history.history['val_accuracy']` → validation accuracy per epoch

**What to look for:**

- Both curves rise → model is learning
- Curves stay close → model is generalizing well
- Training >> Validation → possible overfitting
- Both low → underfitting

---

## 15. Plotting Training vs Validation Loss

```python
plt.figure(figsize=(8,5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()
```

Same idea — `history.history['loss']` and `history.history['val_loss']`.

Looking at the plot, we can see:

- Training loss drops quickly and continues to decrease
- Validation loss also drops but flattens around epoch 4–6
- The gap between them shows some overfitting (but not too bad)
- The early stopping caught it at the right time

---

## 16. Visualizing Random Test Predictions

```python
import numpy as np

random_indices = np.random.choice(len(X_test), 20, replace=True)

fig, axes = plt.subplots(4, 5, figsize=(12, 10))
axes = axes.ravel()

for i, idx in enumerate(random_indices):
    prediction = model.predict(X_test[idx:idx+1], verbose=0)
    predicted_digit = np.argmax(prediction)
    actual_digit = y_test[idx]

    axes[i].imshow(X_test[idx].reshape(28, 28), cmap='gray')

    color = 'green' if predicted_digit == actual_digit else 'red'
    axes[i].set_title(
        f"Pred: {predicted_digit}\nActual: {actual_digit}",
        color=color,
        fontsize=10
    )
    axes[i].axis('off')

plt.tight_layout()
plt.show()
```

This is the **visual verification** part. You're picking 20 random test images, letting the model predict, and comparing with the actual label.

Let's break it down:

### Select 20 random images

```python
random_indices = np.random.choice(len(X_test), 20, replace=True)
```

- `len(X_test)` = 10,000
- Pick 20 random indices
- `replace=True` → allows duplicates (the same image could appear twice)

### Create a 4×5 grid

```python
fig, axes = plt.subplots(4, 5, figsize=(12, 10))
```

20 subplots arranged as 4 rows × 5 columns.

### Flatten the axes array

```python
axes = axes.ravel()
```

Turns a 4×5 grid into a simple 1D list of 20 axes.

### Loop through each image

```python
for i, idx in enumerate(random_indices):
```

`i` is the position (0 to 19), `idx` is the actual index in `X_test`.

### Make a prediction

```python
prediction = model.predict(X_test[idx:idx+1], verbose=0)
predicted_digit = np.argmax(prediction)
```

- `X_test[idx:idx+1]` → keeps the batch dimension (shape becomes `(1, 28, 28, 1)`)
- `np.argmax(prediction)` → gets the index of the highest probability → the predicted digit

### Get the actual digit

```python
actual_digit = y_test[idx]
```

### Show the image

```python
axes[i].imshow(X_test[idx].reshape(28, 28), cmap='gray')
```

Reshape back to 28×28 (remove the channel dimension for display).

### Color the title

```python
color = 'green' if predicted_digit == actual_digit else 'red'
```

- **Green** = correct prediction
- **Red** = incorrect prediction

### Set the title

```python
axes[i].set_title(f"Pred: {predicted_digit}\nActual: {actual_digit}", ...)
```

`\n` creates a new line, so it shows two lines: one for prediction, one for actual.

### Clean layout

```python
plt.tight_layout()
plt.show()
```

Prevents overlapping titles and shows the final grid.

**What you see:** 20 images, most labeled in green (correct), possibly a few in red (incorrect). This gives an intuitive feel for how well the model performs.

---

## Putting It All Together — The Complete Pipeline

```text
1. Load MNIST data (60,000 train + 10,000 test)
        ↓
2. Visualize 5 sample images (sanity check)
        ↓
3. Normalize pixels: 0–255 → 0–1
        ↓
4. Reshape: (n, 28, 28) → (n, 28, 28, 1)
        ↓
5. Build CNN:
   Conv2D → MaxPool → Conv2D → MaxPool → Flatten → Dense → Dropout → Dense(softmax)
        ↓
6. Compile with Adam + sparse categorical crossentropy + accuracy
        ↓
7. Set up EarlyStopping (monitor val_loss, patience 3)
        ↓
8. Train with model.fit() (20 epochs, batch_size 64, 20% validation)
        ↓
9. Evaluate on test data → 99.11% accuracy
        ↓
10. Plot training vs validation accuracy and loss
        ↓
11. Visualize 20 random predictions (green = correct, red = wrong)
```

---

## Key Takeaways

1. **CNNs are for images** — they use convolution layers to find patterns like edges and curves. This is why they're better than DNNs for image tasks.

2. **Convolution + Pooling = feature extraction** — the early layers find simple patterns, the later layers combine them into more complex ones.

3. **Dense layers = decision making** — after features are extracted, the Dense layers decide which digit the image represents.

4. **Dropout prevents overfitting** — it randomly disables neurons so the network doesn't memorize the training data.

5. **EarlyStopping is your safety net** — it stops training when improvement stops, and restores the best version.

6. **Validation data is for checking, not training** — like a mock exam before the real exam.

7. **Test data is the final exam** — never used during training, gives you the true performance.

8. **99.11% accuracy** — the CNN correctly classifies 99 out of every 100 unseen handwritten digits. Excellent result! 


---





