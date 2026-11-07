
# UML Class Diagram 

### What is a UML Class Diagram?

A **UML (Unified Modeling Language) Class Diagram** is a graphical representation of the **classes in an object-oriented system and the relationships between those classes**.

It mainly represents the **static structure** of a system.

---

## 1. Structure of a Class

A UML class is usually divided into **3 sections**:
```text
┌──────────────────────┐
│      Student         │  ← Class Name
├──────────────────────┤
│ - id: int            │  ← Attributes / Data 
│ - name: String       │
├──────────────────────┤
│ + registerCourse()   │  ← Methods / Operations / Functions
│ + getName(): String  │
└──────────────────────┘
```

- **Class Name** → `Student`
- **Attributes** → data/properties of the class (Variable)
- **Methods/Operations** → functions/behaviors of the class

So, **both attributes and methods can be represented**.

---

## 2. Visibility Symbols

|Symbol|Meaning|
|---|---|
|`+`|Public|
|`-`|Private|
|`#`|Protected|
|`~`|Package|
- Package = a container/group used to organize related classes and other UML elements.

Example:
```text
-name: String
+getName(): String
```

`name` variable is private, while `getName()` function is public.

---

# 3. Relationships Between Classes

### Association (সংযুক্ত বা একত্রিত হওয়া বা সম্পর্কিত )

A general relationship where two classes **interact, know, or use each other**.

```text
Teacher ───────── Student
```

> **Association = "works with / interacts with"**

---

### Aggregation (সমষ্টি)

A **whole–part** relationship where the part can exist independently of the whole. Team can exist if there have no players. 

```text
Team ◇──────── Player
```

- `Team` = whole
- `Player` = part
- `◇` = hollow diamond
- Diamond is always placed beside the **whole**.

> **Aggregation = weak "has-a" relationship.**

---

### Composition (বন্দোবস্ত  বা সন্ধি  বা সংকলন বা রচনা )

A stronger whole–part relationship where the part's lifecycle is dependent on the whole. In UML **composition**, the part generally **cannot meaningfully exist without the whole**.

```text
House ◆──────── Room
```

- `House` = whole
- `Room` = part
- `◆` = filled diamond
- Diamond is placed beside the **whole**.

> **Composition = strong "has-a" relationship.**

### Important confusion to remember

| Relationship | Whole without Part | Part without Whole |
| ------------ | ------------------ | ------------------ |
| Association  | ✅                  | ✅                  |
| Aggregation  | ✅                  | ✅                  |
| Composition  | ✅*                 | ❌                  |
- **Normally in UML modeling, the whole can exist without parts even in composition**. 
- The defining restriction is on the **part**, not the whole.

The **main difference between aggregation and composition is the independence/lifecycle of the part**.

---

# 4. Generalization

Generalization represents an **"is-a" relationship** and corresponds to **inheritance** in OOP. 

```text
  Animal
    △
    │
   Dog
```

> **Dog IS-A Animal**

The triangle points toward the **general/superclass**.

---

# 5. Multiplicity

Numbers such as **`1`, `*`, `0..1`, `1..*`** near relationships are called **multiplicity**.  It tells us **how many objects of one class can be associated with one object of another class**.

They tell us **how many objects can participate in a relationship**.
```text
Hospital 1 ───────── * Patient
```

Means:
- One Hospital can have **many Patients**.
- Each Patient is associated with **one Hospital**.

Common values:

| Notation     | Meaning      |
| ------------ | ------------ |
| `1`          | Exactly one  |
| `0..1`       | Zero or one  |
| `*` / `0..*` | Zero or many |
| `1..*`       | One or many  |

**Remember:** the multiplicity is interpreted from the **opposite class**.

---




