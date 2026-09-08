# 📘 Abstract Factory Design Pattern

## 📌 Overview

The **Abstract Factory Pattern** provides an interface to create **families of related objects** without specifying their concrete classes.
It is known as a **factory of factories** and belongs to the **Creational Design Pattern** category.

This pattern is useful when a system needs to be independent of how its objects are created and represented.

---

## 🎯 Intent

* Encapsulate a group of individual factories
* Provide an interface for creating related objects
* Promote loose coupling and scalability

---

## 🧠 Key Components

* **AbstractFactory** → Declares factory methods
* **Concrete Factories** → Create specific object families
* **Abstract Product** → Declares product interfaces
* **Concrete Products** → Implements product interfaces
* **Factory Producer** → Returns the required factory

---

## 🧩 UML Concept (Textual)

```
Client → FactoryProducer → AbstractFactory
                 ↓
        ConcreteFactory → ConcreteProduct
```

---

## 🛠 Implementation Steps

### Step 1: Create Shape Interface

```java
interface Shape {
    void draw();
}
```

---

### Step 2: Create Concrete Shape Classes

```java
class Rectangle implements Shape {
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}

class Square implements Shape {
    public void draw() {
        System.out.println("Inside Square::draw() method.");
    }
}

class RoundedRectangle implements Shape {
    public void draw() {
        System.out.println("Inside RoundedRectangle::draw() method.");
    }
}

class RoundedSquare implements Shape {
    public void draw() {
        System.out.println("Inside RoundedSquare::draw() method.");
    }
}
```

---

### Step 3: Create Abstract Factory

```java
abstract class AbstractFactory {
    abstract Shape getShape(String shapeType);
}
```

---

### Step 4: Create Concrete Factory Classes

```java
class ShapeFactory extends AbstractFactory {
    public Shape getShape(String shapeType) {
        if (shapeType.equalsIgnoreCase("RECTANGLE"))
            return new Rectangle();
        else if (shapeType.equalsIgnoreCase("SQUARE"))
            return new Square();
        return null;
    }
}

class RoundedShapeFactory extends AbstractFactory {
    public Shape getShape(String shapeType) {
        if (shapeType.equalsIgnoreCase("RECTANGLE"))
            return new RoundedRectangle();
        else if (shapeType.equalsIgnoreCase("SQUARE"))
            return new RoundedSquare();
        return null;
    }
}
```

---

### Step 5: Create Factory Producer

```java
class FactoryProducer {
    public static AbstractFactory getFactory(boolean rounded) {
        if (rounded)
            return new RoundedShapeFactory();
        else
            return new ShapeFactory();
    }
}
```

---

## ▶️ Demo / Usage

```java
public class AbstractFactoryPatternDemo {
    public static void main(String[] args) {

        AbstractFactory shapeFactory = FactoryProducer.getFactory(false);
        Shape shape1 = shapeFactory.getShape("RECTANGLE");
        shape1.draw();

        Shape shape2 = shapeFactory.getShape("SQUARE");
        shape2.draw();

        AbstractFactory roundedFactory = FactoryProducer.getFactory(true);
        Shape shape3 = roundedFactory.getShape("RECTANGLE");
        shape3.draw();

        Shape shape4 = roundedFactory.getShape("SQUARE");
        shape4.draw();
    }
}
```

---

## 📤 Output

```
Inside Rectangle::draw() method.
Inside Square::draw() method.
Inside RoundedRectangle::draw() method.
Inside RoundedSquare::draw() method.
```

---

## ✅ Advantages

* Supports **open/closed principle**
* Ensures consistency among related objects
* Easy to introduce new product families

---

## ❌ Disadvantages

* Code complexity increases
* Adding new product types requires changes in factories

---

## 🏁 Conclusion

The **Abstract Factory Pattern** is ideal when multiple related objects must be created together while hiding implementation details.
It is widely used in **GUI toolkits, themes, and cross-platform frameworks**.

---