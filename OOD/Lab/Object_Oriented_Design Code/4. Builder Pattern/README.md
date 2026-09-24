# 📘 Builder Design Pattern

## 📌 Overview

The **Builder Pattern** is a **Creational Design Pattern** that constructs a **complex object step by step** using simple objects.
It separates the construction process from the final representation, allowing the same construction process to create different objects.

---

## 🎯 Intent

* Construct complex objects incrementally
* Hide construction logic from the client
* Provide flexibility in object creation

---

## 🧠 Key Components

* **Item** → Product interface
* **Concrete Items** → Actual products (Burger, Drink)
* **Packing** → Packaging abstraction
* **Meal** → Final complex object
* **MealBuilder** → Builder class
* **Client** → Uses builder to create objects

---

## 🧩 UML Concept (Textual)

```
Client → Builder → Product (Meal)
              → Item → Packing
```

---

## 🛠 Implementation Steps

### Step 1: Create Item and Packing Interfaces

```java
interface Item {
    String name();
    Packing packing();
    float price();
}

interface Packing {
    String pack();
}
```

---

### Step 2: Create Packing Implementations

```java
class Wrapper implements Packing {
    public String pack() { return "Wrapper"; }
}

class Bottle implements Packing {
    public String pack() { return "Bottle"; }
}
```

---

### Step 3: Create Abstract Item Classes

```java
abstract class Burger implements Item {
    public Packing packing() { return new Wrapper(); }
}

abstract class ColdDrink implements Item {
    public Packing packing() { return new Bottle(); }
}
```

---

### Step 4: Create Concrete Item Classes

```java
class VegBurger extends Burger {
    public float price() { return 25.0f; }
    public String name() { return "Veg Burger"; }
}

class ChickenBurger extends Burger {
    public float price() { return 50.5f; }
    public String name() { return "Chicken Burger"; }
}

class Coke extends ColdDrink {
    public float price() { return 30.0f; }
    public String name() { return "Coke"; }
}

class Pepsi extends ColdDrink {
    public float price() { return 35.0f; }
    public String name() { return "Pepsi"; }
}
```

---

### Step 5: Create Meal Class (Product)

```java
class Meal {
    private List<Item> items = new ArrayList<>();

    void addItem(Item item) { items.add(item); }

    float getCost() {
        float cost = 0;
        for (Item item : items)
            cost += item.price();
        return cost;
    }

    void showItems() {
        for (Item item : items) {
            System.out.println("Item : " + item.name() +
                    ", Packing : " + item.packing().pack() +
                    ", Price : " + item.price());
        }
    }
}
```

---

### Step 6: Create Builder Class

```java
class MealBuilder {

    Meal prepareVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new VegBurger());
        meal.addItem(new Coke());
        return meal;
    }

    Meal prepareNonVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new ChickenBurger());
        meal.addItem(new Pepsi());
        return meal;
    }
}
```

---

## ▶️ Demo / Usage

```java
public class BuilderPatternDemo {
    public static void main(String[] args) {

        MealBuilder mealBuilder = new MealBuilder();

        Meal vegMeal = mealBuilder.prepareVegMeal();
        vegMeal.showItems();
        System.out.println("Total Cost: " + vegMeal.getCost());

        Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
        nonVegMeal.showItems();
        System.out.println("Total Cost: " + nonVegMeal.getCost());
    }
}
```

---

## 📤 Output

```
Veg Meal
Item : Veg Burger, Packing : Wrapper, Price : 25.0
Item : Coke, Packing : Bottle, Price : 30.0
Total Cost: 55.0

Non-Veg Meal
Item : Chicken Burger, Packing : Wrapper, Price : 50.5
Item : Pepsi, Packing : Bottle, Price : 35.0
Total Cost: 85.5
```

---

## ✅ Advantages

* Step-by-step object creation
* Improves readability and maintainability
* Same builder can create different objects

---

## ❌ Disadvantages

* Increased number of classes
* Not suitable for simple objects

---

## 📌 Common Use Cases

* Meal ordering systems
* Report generation
* UI layout creation
* Object configuration

---

## 🏁 Conclusion

The **Builder Pattern** is ideal for creating **complex objects** with multiple parts while keeping construction logic separate from representation.

---
