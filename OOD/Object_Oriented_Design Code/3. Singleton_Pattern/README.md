# 📘 Singleton Design Pattern

## 📌 Overview

The **Singleton Pattern** is a **Creational Design Pattern** that ensures a class has **only one instance** and provides a **global access point** to that instance.

It is commonly used when exactly one object is needed to coordinate actions across the system.

---

## 🎯 Intent

* Ensure only **one object** is created
* Provide **controlled global access**
* Prevent multiple instantiations

---

## 🧠 Key Characteristics

* Private constructor
* Static instance of the class
* Public static method to access the instance

---

## 🧩 UML Concept (Textual)

```
Client → Singleton
        (single instance)
```

---

## 🛠 Implementation Steps

### Step 1: Create Singleton Class

```java
class SingleObject {

    // Static instance
    private static SingleObject instance = new SingleObject();

    // Private constructor
    private SingleObject() {}

    // Public access method
    public static SingleObject getInstance() {
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello World!");
    }
}
```

---

## ▶️ Demo / Usage

```java
public class SingletonPatternDemo {
    public static void main(String[] args) {

        // Get the only object
        SingleObject object = SingleObject.getInstance();

        // Call method
        object.showMessage();
    }
}
```

---

## 📤 Output

```
Hello World!
```

---

## ✅ Advantages

* Controlled access to single instance
* Saves memory
* Easy to implement

---

## ❌ Disadvantages

* Global state may cause hidden dependencies
* Difficult to test
* Not ideal for multithreading without synchronization

---

## 📌 Common Use Cases

* Database connection
* Logger
* Configuration manager
* Cache system

---

## 🏁 Conclusion

The **Singleton Pattern** is a simple yet powerful pattern used when a **single shared resource** is required throughout an application. Proper implementation ensures efficiency and consistency.

---