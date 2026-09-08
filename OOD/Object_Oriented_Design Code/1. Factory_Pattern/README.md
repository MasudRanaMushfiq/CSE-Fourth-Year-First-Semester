

# **Creational Design – Factory Pattern**

## **1. Title**

**Implementation of the Factory Pattern in Java**

---

## **2. Objectives**

* Understand the concept of **Factory Design Pattern** under Creational Design Patterns.
* Learn how to **create objects without exposing the creation logic** to the client.
* Implement a **factory class** that returns objects based on user input.

---

## **3. Theory**

**Factory Pattern:**

* The Factory Pattern is one of the most widely used **creational design patterns**.
* It defines an **interface or abstract class** for creating an object but lets **subclasses decide which class to instantiate**.
* Helps achieve **loose coupling** between client and implementation classes.

**Key Features:**

1. The client does **not know the exact implementation** class it is using.
2. Object creation logic is **centralized in the factory class**.
3. Promotes **code reusability** and **scalability**.

**Real-world Analogy:**
Think of a **shape factory**: You request a `"circle"` or `"square"` and the factory gives you the required shape object. You don’t worry about **how the shape object is created**.

---

## **4. Experiment Setup**

We will create the following:

1. **Shape.java** – Interface
2. **Circle.java, Rectangle.java, Square.java** – Concrete classes implementing `Shape`
3. **ShapeFactory.java** – Factory class that generates objects of concrete classes
4. **FactoryPatternDemo.java** – Demo class to test the factory pattern

---

## **5. Procedure**

1. Define a **Shape interface** with a method `draw()`.
2. Create **Circle, Rectangle, and Square** classes that implement the `Shape` interface.
3. Create a **ShapeFactory** class with a method `getShape(String shapeType)` to return objects based on input.
4. Create a **FactoryPatternDemo** class that:

   * Calls **ShapeFactory**
   * Requests a shape object (`CIRCLE, RECTANGLE, SQUARE`)
   * Calls the `draw()` method of that object.
5. Compile and run the program.

---

## **6. Program Code**

**Shape.java**

```java
public interface Shape {
    void draw();
}
```

**Circle.java**

```java
public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Circle::draw() method.");
    }
}
```

**Rectangle.java**

```java
public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}
```

**Square.java**

```java
public class Square implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Square::draw() method.");
    }
}
```

**ShapeFactory.java**

```java
public class ShapeFactory {
    public Shape getShape(String shapeType) {
        if (shapeType == null) return null;
        if (shapeType.equalsIgnoreCase("CIRCLE")) return new Circle();
        else if (shapeType.equalsIgnoreCase("RECTANGLE")) return new Rectangle();
        else if (shapeType.equalsIgnoreCase("SQUARE")) return new Square();
        return null;
    }
}
```

**FactoryPatternDemo.java**

```java
public class FactoryPatternDemo {
    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        // Get an object of Circle and call its draw method
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        shape1.draw();

        // Get an object of Rectangle and call its draw method
        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        shape2.draw();

        // Get an object of Square and call its draw method
        Shape shape3 = shapeFactory.getShape("SQUARE");
        shape3.draw();
    }
}
```

---

## **7. UML Diagram (Text Form)**

```
          Shape (interface)
               ↑
     -------------------------
     |           |           |
  Circle     Rectangle     Square
               ↑
           ShapeFactory
               |
        getShape(String)
```

---

## **8. Questions**

1. **What problem does the Factory Pattern solve?**

   * Centralizes object creation and hides instantiation details from the client.

2. **Why is the Factory Pattern preferred over directly creating objects with `new`?**

   * Promotes **loose coupling**, flexibility, and scalability.

3. **Can the Factory Pattern be extended to support more shapes without changing client code? How?**

   * Yes, add a new concrete class (e.g., `Triangle`) and update the factory. Client code does not change.

4. **Compare Factory Pattern and Singleton Pattern in terms of object creation.**

   * **Factory Pattern:** Creates multiple objects based on type.
   * **Singleton Pattern:** Ensures only one instance of a class exists.
