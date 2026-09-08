# 🧩 Object-Oriented Design Patterns – Lab Assignment

## 📌 Covered Design Patterns

1. Factory Pattern
2. Abstract Factory Pattern
3. Singleton Pattern
4. Builder Pattern
5. Adapter Pattern
6. Filter (Criteria) Pattern
7. Observer Pattern
8. Chain of Responsibility Pattern

---

## 🔹 1. Factory Design Pattern

### 📖 Theory

The **Factory Pattern** defines an interface for creating objects but allows subclasses to decide which class to instantiate.
It removes direct object creation using `new` and promotes **loose coupling**.

### 📌 When to Use

* Object creation logic is complex
* The exact class is determined at runtime

### 🧠 UML Idea

```
Client → Factory → Concrete Product
```

### 💻 Code Example

```java
// Product Interface
interface Shape {
    void draw();
}

// Concrete Products
class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing Circle");
    }
}

class Rectangle implements Shape {
    public void draw() {
        System.out.println("Drawing Rectangle");
    }
}

// Factory Class
class ShapeFactory {
    public Shape getShape(String type) {
        if (type == null) return null;
        if (type.equalsIgnoreCase("CIRCLE"))
            return new Circle();
        else if (type.equalsIgnoreCase("RECTANGLE"))
            return new Rectangle();
        return null;
    }
}

// Client
public class FactoryDemo {
    public static void main(String[] args) {
        ShapeFactory factory = new ShapeFactory();
        Shape shape1 = factory.getShape("CIRCLE");
        shape1.draw();
    }
}
```

---

## 🔹 2. Abstract Factory Pattern

### 📖 Theory

The **Abstract Factory Pattern** provides an interface for creating **families of related objects** without specifying their concrete classes.

### 📌 Difference from Factory

| Factory            | Abstract Factory                |
| ------------------ | ------------------------------- |
| Creates one object | Creates related object families |

### 💻 Code Example

```java
// Abstract Products
interface Button {
    void paint();
}

interface Checkbox {
    void paint();
}

// Concrete Products
class WindowsButton implements Button {
    public void paint() {
        System.out.println("Windows Button");
    }
}

class WindowsCheckbox implements Checkbox {
    public void paint() {
        System.out.println("Windows Checkbox");
    }
}

// Abstract Factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// Concrete Factory
class WindowsFactory implements GUIFactory {
    public Button createButton() {
        return new WindowsButton();
    }
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

// Client
public class AbstractFactoryDemo {
    public static void main(String[] args) {
        GUIFactory factory = new WindowsFactory();
        factory.createButton().paint();
        factory.createCheckbox().paint();
    }
}
```

---

## 🔹 3. Singleton Pattern

### 📖 Theory

The **Singleton Pattern** ensures that **only one instance** of a class exists and provides a global access point.

### 📌 Use Case

* Database connection
* Logger
* Configuration manager

### 💻 Code Example

```java
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }

    public void showMessage() {
        System.out.println("Singleton Instance Accessed");
    }
}

public class SingletonDemo {
    public static void main(String[] args) {
        Singleton obj = Singleton.getInstance();
        obj.showMessage();
    }
}
```

---

## 🔹 4. Builder Pattern

### 📖 Theory

The **Builder Pattern** constructs complex objects step-by-step without exposing construction details.
**Builds complex objects step-by-step.**

### 💻 Code Example

```java
class Computer {
    private String CPU;
    private String RAM;

    static class Builder {
        private String CPU;
        private String RAM;

        Builder setCPU(String cpu) {
            this.CPU = cpu;
            return this;
        }

        Builder setRAM(String ram) {
            this.RAM = ram;
            return this;
        }

        Computer build() {
            Computer c = new Computer();
            c.CPU = this.CPU;
            c.RAM = this.RAM;
            return c;
        }
    }
}

public class BuilderDemo {
    public static void main(String[] args) {
        Computer pc = new Computer.Builder()
                .setCPU("Intel i5")
                .setRAM("16GB")
                .build();
        System.out.println("Computer Built");
    }
}
```

---

## 🔹 5. Adapter Pattern

### 📖 Theory

The **Adapter Pattern** allows incompatible interfaces to work together.

### 💻 Code Example

```java
interface MediaPlayer {
    void play(String file);
}

class AudioPlayer {
    void playAudio(String file) {
        System.out.println("Playing audio: " + file);
    }
}

class MediaAdapter implements MediaPlayer {
    AudioPlayer audioPlayer = new AudioPlayer();

    public void play(String file) {
        audioPlayer.playAudio(file);
    }
}

public class AdapterDemo {
    public static void main(String[] args) {
        MediaPlayer player = new MediaAdapter();
        player.play("song.mp3");
    }
}
```

---

## 🔹 6. Filter (Criteria) Pattern

### 📖 Theory

The **Filter Pattern** filters objects using different criteria and combines them logically.
**Filters objects based on conditions.**

### 💻 Code Example

```java
class Person {
    String name, gender;

    Person(String name, String gender) {
        this.name = name;
        this.gender = gender;
    }
}

interface Criteria {
    List<Person> meetCriteria(List<Person> persons);
}

class MaleCriteria implements Criteria {
    public List<Person> meetCriteria(List<Person> persons) {
        List<Person> males = new ArrayList<>();
        for (Person p : persons)
            if (p.gender.equalsIgnoreCase("Male"))
                males.add(p);
        return males;
    }
}
```

---

## 🔹 7. Observer Pattern

### 📖 Theory

The **Observer Pattern** defines a one-to-many dependency where observers are notified automatically when the subject changes state.
**One-to-many dependency. Observers get notified on state change.**

### 💻 Code Example

```java
interface Observer {
    void update(int state);
}

class Subject {
    private List<Observer> observers = new ArrayList<>();
    private int state;

    void attach(Observer o) {
        observers.add(o);
    }

    void setState(int state) {
        this.state = state;
        notifyAllObservers();
    }

    void notifyAllObservers() {
        for (Observer o : observers)
            o.update(state);
    }
}
```

---

## 🔹 8. Chain of Responsibility Pattern

### 📖 Theory

The **Chain of Responsibility Pattern** passes a request along a chain of handlers until one handles it.

### 💻 Code Example

```java
abstract class Handler {
    protected Handler next;

    void setNext(Handler next) {
        this.next = next;
    }

    abstract void handleRequest(int level);
}

class LowLevelHandler extends Handler {
    void handleRequest(int level) {
        if (level <= 1)
            System.out.println("Low level handled");
        else if (next != null)
            next.handleRequest(level);
    }
}
```

---

## ✅ Conclusion

This lab demonstrates **core Object-Oriented Design Patterns** used in:

* Software architecture
* Enterprise applications
* Embedded systems
* UI frameworks

Each pattern improves **maintainability, scalability, and reusability**.

