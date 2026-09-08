# Filter (Criteria) Design Pattern

## Definition

**Filter Pattern (Criteria Pattern)** is a **structural design pattern** that allows filtering a collection of objects using different criteria and combining them using logical operations such as **AND** and **OR**, without modifying the object structure.

---

## Purpose

* To apply multiple filtering rules dynamically
* To keep filtering logic **decoupled** from object classes
* To combine criteria flexibly

---

## Pattern Type

**Structural Design Pattern**

---

## Main Components

* **Person** – Model class on which filtering is applied
* **Criteria** – Interface defining the filtering rule
* **Concrete Criteria** – Implements individual conditions

  * Male
  * Female
  * Single
* **Composite Criteria**

  * AndCriteria
  * OrCriteria
* **CriteriaPatternDemo** – Demonstrates pattern usage

---

## Working Principle

1. Create objects (`Person`)
2. Define filtering rules using `Criteria`
3. Apply single or combined criteria
4. Get filtered results without changing object structure

---

## Advantages

* Easy to add new criteria
* Promotes loose coupling
* Improves code readability and maintainability

---

## Disadvantages

* Increases number of classes
* Slightly complex for small applications

---

## Conclusion

The **Filter (Criteria) Pattern** provides a clean and flexible way to filter objects using multiple conditions while keeping the design modular and scalable.

---

