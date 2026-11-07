

# The Four Pillars of OOP

The **four pillars of Object-Oriented Programming (OOP)** are:

1. **Encapsulation**
2. **Abstraction**
3. **Inheritance**
4. **Polymorphism**

- **Public** means it can be accessed from anywhere that can access the object/class.
- **Private** means it can only be directly accessed inside the same class. 
- **Protected** members can be accessed inside the same class and by its subclasses (child classes). 

A good way to understand them is: **Encapsulation and Abstraction control how we expose things; Inheritance helps us reuse/extend classes; Polymorphism lets objects behave differently through a common interface.**

---

## 1. Encapsulation

**Encapsulation is the practice of bundling related data and behavior together in a class(Unite) and controlling how the object's internal state(data) can be accessed or modified.**

- Encapsulation means making all related things encapsulated/together.
- But good encapsulation usually also involves **controlling access to the internal data**.

Think of a **bank account**.

You shouldn't be able to directly change:
```text
balance = -50000
```

Instead, the class provides controlled methods:
```text
deposit()
withdraw()
```

### Example
```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public double getBalance() {
        return balance;
    }
}

```

Here:
```text
private balance
```

cannot be directly accessed from outside the class.

Instead:
```text
deposit()
getBalance()
```

provide controlled access.
### Why use encapsulation?
- Protect data
- Prevent invalid modification
- Control how data is accessed
- Make code easier to maintain

---

# 2. Abstraction

**Abstraction means showing only the important/useful features and hiding unnecessary implementation details.**

Think about driving a car.

You use:
```text
steering wheel
accelerator
brake
```

You don't need to know exactly how the engine, fuel injection, transmission, etc. work internally.

Similarly:
```java
car.start();
```

You simply use `start()` without knowing its internal implementation.

### Example

```java
class Car {

    public void start() {
        // complicated engine operations
        // ........
        // are hidden here
    }
}
```

The user only sees:
```text
start()
```

The complicated implementation is hidden.

### Why use abstraction?
- Reduce complexity
- Make systems easier to use
- Hide unnecessary implementation details
- Focus on **what an object does**, rather than **how it does it**

---

# 3. Inheritance

**Inheritance allows a new child class to acquire properties and methods from an existing parent class.**

Example:
```text
             Animal
                △
                │
        ┌───────┴───────┐
        ↓               ↓
       Dog             Cat
```

`Animal` is the **parent or superclass**.
`Dog` and `Cat` are **child or subclasses**.

We can say:
> **Dog IS-A Animal**

### Example

```java
class Animal {

    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {

    void bark() {
        System.out.println("Barking");
    }
}
```

Now:
```java
Dog d = new Dog();

d.eat();   // inherited from Animal
d.bark();  // Dog's own method
```

The `Dog` class gets `eat()` from `Animal`.
### Why use inheritance?
- Code reuse
- Create specialized classes
- Represent "is-a" relationships
- Avoid repeating common functionality

### My Special Questions and Answers: 
- **Inheritance** means a child class gets or reuses features of a parent class.
- When `Dog extends Animal`, the `Dog` object contains the **parent all (`Animal`) state + its own created(dog) state**.
- **Public & protected** variables or methods → inherited and accessible by the child.
- **Private** variables or methods → exist in the parent part but **cannot be directly accessed** by the child. But also can access by another public or protected class who return this private data. 
- Parent methods are **not literally copied** into the child; the child only reuses the parent's existing implementation. 
- The child can **add new variables or methods**.
- The child can **override** a parent's method to provide different behavior.
- `extends` represents an **IS-A relationship**. 

#### Override: 
1. When you override a parent method, the **entire original method implementation is replaced** by the child’s new implementation.  
2. The variables and statements **inside that overridden method are not automatically carried over**; you must write them again
3. **When you override a method, you provide a new full implementation for that method in the child.** You keep the same method signature (name + parameters, with compatible return type), but the **method body implement according to your requirement, completely different**. You **cannot  reuse the variables or statements on any of them in child.** 


---
### Is Parent Code Copied Into Child Class?
The key is that **Java doesn't need to copy the parent source code into the child**. It stores information about the inheritance relationship and uses that information when compiling/running.

Suppose:
```java
class Animal {
    protected int age;

    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }
}
```

When Java sees:
```java
class Dog extends Animal
```

the compiler records:

> **Dog is a subclass of Animal.**

Then when it sees:
```java
Dog d = new Dog();
d.eat();
```

the compiler knows:
```text
Dog
 ↓
parent = Animal
 ↓
Animal has eat()
 ↓
use Animal's eat() implementation
```

#### What about the actual object?

Conceptually:
```text
Dog object
┌─────────────────┐
│ Animal state    │
│ age             │
├─────────────────┤
│ Dog state       │
│ ...             │
└─────────────────┘
```

The `eat()` **code itself doesn't need to be copied into the Dog class**. The runtime knows that `Dog` inherits `eat()` from `Animal`, so it can execute the `Animal.eat()` implementation.

#### If Dog overrides it

```java
class Dog extends Animal {
    @Override
    void eat() {
        System.out.println("Dog eating");
    }
}
```

Now Java knows:
```text
Dog
 ↓
has its own eat()
 ↓
use Dog.eat()
```

So:
```java
Animal a = new Dog();
a.eat();
```

calls:
```text
Dog.eat()
```

This is **runtime polymorphism**.

#### The simplest mental model

Think of the class information as a chain:
```text
Dog
 │
 └── parent → Animal
                  │
                  └── parent → Object
```

Java keeps this **class metadata/inheritance relationship**, and method lookup follows that relationship.

So:

> **Inheritance is not source-code copying. The JVM knows the parent-child relationship through class metadata, and uses it to find fields/method implementations when needed.**


---


# 4. Polymorphism

This is usually the most confusing one at first.

**Polymorphism means "many forms."**

It allows us to use a **common interface/reference**, while different objects provide different behavior.

### Example

Suppose:

```text
             Animal
                △
                │
        ┌───────┴───────┐
        ↓               ↓
       Dog             Cat
```

All animals have:

```text
sound()
```

But each animal makes a different sound.

```java
class Animal {
    void sound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Bark");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Meow");
    }
}
```

Now:

```java
Animal a1 = new Dog();
Animal a2 = new Cat();

a1.sound();  // Bark
a2.sound();  // Meow
```

Notice something important:

```text
a1.sound()
```

and

```text
a2.sound()
```

use the **same method name**:

```text
sound()
```

but produce **different behavior** because the actual objects are different.

That's polymorphism.

### Remember

> **Polymorphism = "Same interface, different behavior."**

# A Big Real-World Example

Let's imagine you're building a **Payment System**.

You support:
```
Credit Card
Bkash
Bank Transfer
PayPal
```

You want all payment types to provide:
```
pay()
```

---

## Parent class

```
abstract class Payment {

    abstract void pay(double amount);

    void printReceipt() {
        System.out.println("Receipt generated");
    }
}
```

Now each payment type implements `pay()` differently.

---

## Credit Card

```
class CreditCardPayment extends Payment {

    @Override
    void pay(double amount) {
        System.out.println(
            "Paid " + amount + " using Credit Card"
        );
    }
}
```

---

## Bkash

```
class BkashPayment extends Payment {

    @Override
    void pay(double amount) {
        System.out.println(
            "Paid " + amount + " using Bkash"
        );
    }
}
```

---

## Bank

```
class BankPayment extends Payment {

    @Override
    void pay(double amount) {
        System.out.println(
            "Paid " + amount + " using Bank Transfer"
        );
    }
}
```

Now we can write:
```
Payment p1 = new CreditCardPayment();
Payment p2 = new BkashPayment();
Payment p3 = new BankPayment();

p1.pay(1000);
p2.pay(1000);
p3.pay(1000);
```

Output:
```
Paid 1000 using Credit Card
Paid 1000 using Bkash
Paid 1000 using Bank Transfer
```

The code calling the payments doesn't need to know the specific payment type.

---

# 13. The Huge Benefit

Imagine your application has:
```
void processPayment(Payment payment, double amount) {
    payment.pay(amount);
}
```

Now:
```
processPayment(new CreditCardPayment(), 1000);

processPayment(new BkashPayment(), 1000);

processPayment(new BankPayment(), 1000);
```

You don't need:
```
if (type == "credit") {
    ...
}
else if (type == "bkash") {
    ...
}
else if (type == "bank") {
    ...
}
```

That's one of the biggest benefits of polymorphism.

---

# 14. Adding a New Payment Type

Suppose tomorrow you add:
```
Nagad
```

You create:
```
class NagadPayment extends Payment {

    @Override
    void pay(double amount) {
        System.out.println(
            "Paid " + amount + " using Nagad"
        );
    }
}
```

Your existing:
```
processPayment()
```

doesn't need to change.

You can simply:
```
processPayment(new NagadPayment(), 1000);
```

This makes software **extensible and maintainable**.

# Overloading vs Overriding

Don't mix these up.
### Overloading

Same class, usually:
```
add(int, int)
add(int, int, int)
add(double, double)
```

Different parameters.
### Overriding

Parent-child relationship:
```
Animal.sound()
       ↓
Dog.sound()
```

Same method signature, different implementation.

---

# All Four Together

Imagine an **Animal Hospital System**.
```text
                    Animal
                       △
                       │
              ┌────────┴────────┐
              │                 │
             Dog               Cat
```

### Encapsulation

```text
Dog
- name
- age
+ getName()
+ setName()
```

The data is protected.

### Abstraction

```text
animal.treat()
```

The user doesn't need to know the internal treatment process.

### Inheritance

```text
Dog extends Animal
Cat extends Animal
```

Dog and Cat reuse common Animal functionality.

### Polymorphism

```text
Animal a = new Dog();
Animal b = new Cat();

a.sound();  → Bark
b.sound();  → Meow
```

Same `sound()` interface, different behavior.

---

## Final Exam-Friendly Definitions

|Pillar|Simple definition|
|---|---|
|**Encapsulation**|Bundling data and methods together and controlling access to the data|
|**Abstraction**|Hiding unnecessary implementation details and exposing essential features|
|**Inheritance**|Creating a new class based on an existing class to reuse/extend its features|
|**Polymorphism**|Allowing the same interface/method to have different behavior for different objects|

---








