# Behavioural Design Patterns (Complete PDF Course Content)

This document contains the complete, losslessly compiled content of the PDF course **"Module 2: Behavioural Design Patterns" (Slide 05)**. It integrates all text passages from the slides, full visual details, flowchart descriptions, UML diagrams (represented in ASCII), Java code examples, real-world case studies, and Bloom's Taxonomy evaluation questions.

---

## Part 1: Course Overview and Core Concepts

### What are Behavioural Design Patterns?
Behavioural design patterns focus on **how objects communicate and interact with each other**. Rather than focusing on object creation (creational patterns) or structural organization (structural patterns), behavioural patterns define how responsibilities, behaviors, and algorithms are distributed among objects [1, 2, 3].

They help make communication between objects:
* **Flexible:** Easily adapt to changing requirements [1, 2, 3].
* **Maintainable:** Changes in one part of the system do not affect other parts [1, 2, 3].
* **Loosely Coupled:** Objects depend on each other minimally, promoting independence [1, 2, 3].
* **Easier to Extend:** New behaviors and operations can be added with minimal changes [1, 2, 3].

### Major Behavioural Patterns discussed in this module:
1. **Template Method Pattern** [1, 2, 4]
2. **Chain of Responsibility Pattern** [1, 2, 4]
3. **State Pattern** [1, 2, 4]
4. **Command Pattern** [1, 2, 4]
5. **Observer Pattern** [1, 2, 4]

**Key Idea:** Behavioural patterns focus on object communication and behavior, rather than object creation or structural organization [1, 3, 4].

---

## Part 2: Comprehensive Guide to the 5 Patterns

### 1. Template Method Pattern

#### Definition & Intent
The Template Method Pattern defines the **skeleton of an algorithm in a superclass**, while allowing subclasses to redefine certain steps of the algorithm without changing its overall structure [4].
* **Main Idea:** The structure of the algorithm is fixed, but individual steps can vary dynamically [4].
* **Intent:** Define the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
* **Hollywood Principle:** *"Don't call us, we'll call you."* The superclass calls the subclass methods, controlling the sequence.

#### Structure (UML Representation)
```
          +-----------------------------+
          |        AbstractClass        |
          +-----------------------------+
          | + templateMethod()          | <-- final method containing steps
          | # step1()                   |
          | # step2()                   |
          | # step3()                   |
          +-----------------------------+
                         ^
                         | (Inheritance)
            +------------+------------+
            |                         |
  +------------------+      +------------------+
  |  ConcreteClassA  |      |  ConcreteClassB  |
  +------------------+      +------------------+
  | # step1()        |      | # step1()        |
  | # step2()        |      | # step2()        |
  +------------------+      +------------------+
```

#### Real-Life Example: Preparing a Beverage
The general process of preparing a beverage is fixed: 
`Prepare Beverage -> Boil Water -> Brew Beverage -> Pour into Cup -> Add Condiments` [4, 5]

* **For Tea:** Boil Water -> Steep Tea -> Pour -> Add Lemon [5]
* **For Coffee:** Boil Water -> Brew Coffee -> Pour -> Add Sugar/Milk [5]

The overall algorithm remains identical, but the execution of specific steps differs by concrete class [5].

#### Java Code Example
```java
// Abstract Superclass
abstract class Beverage {
    // Template Method: final prevents subclasses from overriding and changing the algorithm structure
    final void prepare() {
        boilWater();
        brew();
        pourInCup();
        addCondiments();
    }

    abstract void brew();
    abstract void addCondiments();

    void boilWater() {
        System.out.println("Boiling water");
    }

    void pourInCup() {
        System.out.println("Pouring into cup");
    }
}

// Concrete Subclass A: Tea
class Tea extends Beverage {
    void brew() {
        System.out.println("Steeping tea");
    }

    void addCondiments() {
        System.out.println("Adding lemon");
    }
}

// Concrete Subclass B: Coffee
class Coffee extends Beverage {
    void brew() {
        System.out.println("Brewing coffee");
    }

    void addCondiments() {
        System.out.println("Adding sugar and milk");
    }
}
```

#### How It Works (Execution)
```java
Tea t = new Tea();
t.prepare();
// Output:
// 1. Boiling water
// 2. Steeping tea
// 3. Pouring into cup
// 4. Adding lemon

Coffee c = new Coffee();
c.prepare();
// Output:
// 1. Boiling water
// 2. Brewing coffee
// 3. Pouring into cup
// 4. Adding sugar and milk
```

#### Benefits
* **Reuses Code:** Reuses common algorithm structure, avoiding duplicate code [5].
* **Extension Points:** Allows subclasses to customize specific steps without modifying the overall process [5].
* **Control:** Superclass maintains tight control over the exact algorithm execution sequence.
* **Inheritance:** Supports easy code reuse through standard object-oriented inheritance [5].

#### When to Use
* Several classes follow the same overall process, but some steps differ [6].
* You want to avoid repeating common algorithm code across multiple similar implementations [6].

---

### 2. Chain of Responsibility Pattern

#### Definition & Intent
The Chain of Responsibility Pattern passes a request through a **chain of handler objects** until one of them can process the request [7, 8].
* **Main Idea:** Give multiple objects a chance to handle a request without coupling the sender of the request to a specific receiver [7, 8].
* **Intent:** Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

#### Structure (UML Representation)
```
  +--------------+          +-------------------------+
  |    Client    | -------> |         Handler         |
  +--------------+          +-------------------------+
                            | - next: Handler         |
                            | + setNext(Handler)      |
                            | + handleRequest(request)|
                            +-------------------------+
                                         ^
                                         |
                            +------------+------------+
                            |                         |
                 +-------------------+     +-------------------+
                 |  ConcreteHandlerA |     |  ConcreteHandlerB |
                 +-------------------+     +-------------------+
                 | + handleRequest() |     | + handleRequest() |
                 +-------------------+     +-------------------+
```

#### Flowchart of Request Processing
```
Client -> [Handler A] --(Can I handle?)--> Yes -> [Process Request & Stop]
              |
             No
              v
          [Handler B] --(Can I handle?)--> Yes -> [Process Request & Stop]
              |
             No
              v
          [Handler C] --(Can I handle?)--> Yes -> [Process Request & Stop]
              |
             No
              v
      [Unhandled Request]
```

#### Real-Life Example: University Complaint System
* **Hierarchy:** `Student -> Class Teacher -> Department Chairman -> Dean -> Vice Chancellor` [7, 8]
* A complaint is passed along this chain of authorities. If the Class Teacher cannot resolve it, it moves to the Department Chairman, then to the Dean, and eventually to the Vice Chancellor until it is handled.

#### Java Code Example 1: University Complaint Handler
```java
abstract class Handler {
    protected Handler next;

    public void setNext(Handler next) {
        this.next = next;
    }

    public abstract void handleRequest(String request);
}

class ClassTeacher extends Handler {
    public void handleRequest(String request) {
        if (request.equalsIgnoreCase("academic issue")) {
            System.out.println("Class Teacher handled: " + request);
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

// Similarly, DepartmentChairman, Dean, and ViceChancellor are implemented.
```

#### Java Code Example 2: Request Logging System
```java
abstract class Logger {
    protected Logger next;

    public void setNext(Logger next) {
        this.next = next;
    }

    public abstract void log(String level, String message);
}

class InfoLogger extends Logger {
    public void log(String level, String message) {
        if (level.equalsIgnoreCase("INFO")) {
            System.out.println("INFO Log: " + message);
        } else if (next != null) {
            next.log(level, message);
        }
    }
}

class DebugLogger extends Logger {
    public void log(String level, String message) {
        if (level.equalsIgnoreCase("DEBUG")) {
            System.out.println("DEBUG Log: " + message);
        } else if (next != null) {
            next.log(level, message);
        }
    }
}

class ErrorLogger extends Logger {
    public void log(String level, String message) {
        if (level.equalsIgnoreCase("ERROR")) {
            System.out.println("ERROR Log: " + message);
        } else if (next != null) {
            next.log(level, message);
        }
    }
}
```

#### Benefits
* **Reduced Coupling:** Decouples the sender of the request from its receivers [9].
* **Flexibility:** Handler chain order can be modified dynamically at runtime without affecting the client [9].
* **Extensibility:** New handlers can be inserted into the chain easily without modifying existing logic, adhering to the Open/Closed Principle.
* **Single Responsibility:** Each handler is responsible solely for processing its specific type of request.

#### When to Use
* Multiple objects are capable of handling a request, and the specific handler is not known beforehand [24].
* You want to issue a request to one of several objects without specifying the receiver explicitly.
* The set of objects that can handle the request should be specified dynamically.

---

### 3. State Pattern

#### Definition & Intent
The State Pattern allows an object to **change its behavior when its internal state changes** [9, 10].
* **Main Idea:** The object appears to change its class because its entire set of operations depends dynamically on its state [9, 10].
* **Intent:** Encapsulate state-specific behavior and delegate state transitions to individual state classes, removing bulky switch-case or if-else trees [11].

#### Structure (UML Representation)
```
     +--------------------+                 +------------------+
     |      Context       | --------------> |      State       | (Interface)
     +--------------------+                 +------------------+
     | - state: State     |                 | + handle()       |
     | + setState(State)  |                 +------------------+
     | + request()        |                          ^
     +--------------------+                          |
                                        +------------+------------+
                                        |                         |
                             +--------------------+    +--------------------+
                             |    PendingState    |    |     PaidState      |
                             +--------------------+    +--------------------+
                             | + handle()         |    | + handle()         |
                             +--------------------+    +--------------------+
```

#### State Transition Diagram (Online Order)
```
 [Pending State] --(makePayment())--> [Paid State] --(ship())--> [Shipped State] --(deliver())--> [Delivered State]
```

#### Java Code Example: Online Order System
```java
// State Interface
interface State {
    void handle(OrderContext context);
}

// Context Class
class OrderContext {
    private State currentState;

    public OrderContext() {
        // Default initial state
        currentState = new PendingState();
    }

    public void setState(State state) {
        this.currentState = state;
    }

    public void request() {
        currentState.handle(this);
    }
}

// Concrete State 1: Pending
class PendingState implements State {
    public void handle(OrderContext context) {
        System.out.println("Order is currently Pending. Processing payment...");
        context.setState(new PaidState());
    }
}

// Concrete State 2: Paid
class PaidState implements State {
    public void handle(OrderContext context) {
        System.out.println("Order has been Paid. Preparing for shipment...");
        context.setState(new ShippedState());
    }
}

// Concrete State 3: Shipped
class ShippedState implements State {
    public void handle(OrderContext context) {
        System.out.println("Order is Shipped. Out for delivery...");
        context.setState(new DeliveredState());
    }
}

// Concrete State 4: Delivered
class DeliveredState implements State {
    public void handle(OrderContext context) {
        System.out.println("Order has been Delivered successfully!");
    }
}
```

#### Benefits
* **State-Specific Behavior:** Organizes and encapsulates all code for a specific state in one class [11].
* **Eliminates Conditionals:** Eliminates massive conditional branches (massive `if-else` or `switch` blocks) that depend on state variables [11].
* **Explicit Transitions:** Makes state transitions explicit and simple to maintain [11].
* **Maintainability:** New states can be added easily without breaking other states, drastically improving maintainability [11].

#### When to Use
* An object's behavior depends strictly on its state, and its behavior must change dynamically at runtime [11].
* Operations contain massive, complicated conditional statements that depend heavily on the object's state variables.

---

### 4. Command Pattern

#### Definition & Intent
The Command Pattern **encapsulates a request as an object**, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations [12, 13].
* **Main Idea:** Turn a request into a standalone object containing all information about the call.
* **Key Components:**
  1. **Client/Sender:** Creates the command object and sets its receiver [12].
  2. **Command Interface:** Declares an interface for executing operations (typically `execute()`, `undo()`) [12].
  3. **Invoker:** Asks the command to carry out the request [12].
  4. **Receiver:** Performs the actual work [12].

#### Structure (UML Representation)
```
  +-----------------+          +---------------------+
  |     Invoker     | -------> |       Command       | (Interface)
  +-----------------+          +---------------------+
  | - cmd: Command  |          | + execute()         |
  | + setCommand()  |          | + undo()            |
  +-----------------+          +---------------------+
                                          ^
                                          |
                               +----------+----------+
                               |                     |
                    +--------------------+ +--------------------+
                    |    PasteCommand    | |   DeleteCommand    |
                    +--------------------+ +--------------------+
                    | - receiver: Doc    | | - receiver: Doc    |
                    | + execute()        | | + execute()        |
                    +--------------------+ +--------------------+
                               |                     |
                               v                     v
                    +-------------------------------------------+
                    |             Receiver: Document            |
                    +-------------------------------------------+
```

#### Major Purposes of Command Pattern
1. **Store & Schedule Requests:** Commands can be queued, scheduled, and run in lists [13].
2. **Undo & Redo Mechanisms:** Maintain a history stack of command objects to undo and redo operations seamlessly [13].
3. **Transaction Logging:** Commands are logged in sequence to aid recovery or playback after system crashes [13].

#### Java Code Example: Text Editor Paste/Delete with Undo
```java
// Command Interface
interface Command {
    void execute();
    void undo();
}

// Receiver class
class Document {
    public void insert(String text, int index) {
        System.out.println("Inserted '" + text + "' at index " + index);
    }
    public void delete(int index, int length) {
        System.out.println("Deleted content at index " + index);
    }
}

// Concrete Command: PasteCommand
class PasteCommand implements Command {
    private Document doc;
    private String text;
    private int index;

    public PasteCommand(Document doc, String text, int index) {
        this.doc = doc;
        this.text = text;
        this.index = index;
    }

    public void execute() {
        doc.insert(text, index);
    }

    public void undo() {
        doc.delete(index, text.length());
    }
}
```

#### Benefits
* **Decouples Sender & Receiver:** Separates the object making the request from the object that actually performs the action [14].
* **First-Class Objects:** Commands are objects and can be manipulated, saved, queued, and extended [14].
* **Composite Commands:** Allows combining simple commands into complex macro-commands.
* **Undo/Redo Ready:** Simplifies implementing undo/redo since each command has a self-contained inverse operation [14].
* **Separates UI from Business Logic:** Keep user interface actions separate from core domain logic [14].

#### When to Use
* You want to parameterize objects by an action to perform.
* You need to queue, schedule, or log requests [13].
* You must support undo, redo, and macro operations [13, 14].

---

### 5. Observer Pattern

#### Definition & Intent
The Observer Pattern defines a **one-to-many relationship** where a Subject (Observable) maintains a list of dependents (Observers) and automatically notifies them of state changes [15].
* **Main Idea:** When one object changes its internal state, multiple dependent objects are notified and updated automatically [15].
* **Intent:** Ensure that a change in one object propagates automatically to a dynamic list of subscribers without tight coupling.

#### Structure (UML Representation)
```
     +--------------------------+              +------------------------+
     |         Subject          | -----------> |        Observer        | (Interface)
     +--------------------------+              +------------------------+
     | - observers: List        |              | + update(message)      |
     | + registerObserver(Obs)  |              +------------------------+
     | + unregisterObserver(Obs)|                           ^
     | + notifyObservers()      |                           |
     +--------------------------+              +------------+------------+
                                               |                         |
                                    +--------------------+    +--------------------+
                                    |   EmailSubscriber  |    |  MobileAppCitizen  |
                                    +--------------------+    +--------------------+
                                    | + update()         |    | + update()         |
                                    +--------------------+    +--------------------+
```

#### Java Code Example: General Pub-Sub
```java
import java.util.ArrayList;

interface Observer {
    void update(String message);
}

class Subject {
    private ArrayList<Observer> observers = new ArrayList<>();

    public void registerObserver(Observer o) {
        observers.add(o);
    }

    public void unregisterObserver(Observer o) {
        observers.remove(o);
    }

    public void notifyObservers(String message) {
        for (Observer o : observers) {
            o.update(message);
        }
    }
}
```

#### Benefits
* **One-to-Many Propagation:** Establishes a clean, scalable dependency network [18].
* **Loose Coupling:** The subject only knows that the observers implement a general interface; it has no concrete dependency on them [18].
* **Dynamic Subscriptions:** Observers can subscribe and unsubscribe at runtime [17, 18].
* **Open/Closed Principle:** New observer classes can be introduced without modifying the Subject class [18].

#### When to Use
* A change in one object requires changing others, and you don't know how many objects need to change.
* An object should be able to notify other objects without making assumptions about who those objects are.

---

## Part 3: Deep-Dive Comparisons and Frameworks

### 1. High-Level Comparison Matrix
This matrix synthesizes how each pattern behaves and when to deploy it [19]:

| Behavioral Pattern | What it represents (Core Focus) | Main Idea / Intent | Real-Life AAS (Agricultural Automation System) Analogy | Best Deploy Scenario |
| :--- | :--- | :--- | :--- | :--- |
| **Template Method** | **How** an algorithm is performed [19]. | Defines the skeleton of an algorithm in a base class, deferring variable steps to subclasses. | **Irrigation Scheduling:** Algorithm structure is fixed: `Check Moisture -> Check Forecast -> Decide Irrigation -> Log`. Crop classes (Rice, Wheat, Maize) implement the variable `Decide Irrigation` calculation. | Overall process is uniform and fixed, but specific execution steps must be customized by subclasses. |
| **Chain of Responsibility** | **Who** will handle the request [19]. | Pass requests down a pipeline of handlers. Each handler decides to process or pass. | **Alarm Handling Pipeline:** Alarms (e.g., Temperature spike) go through: `Sensor Check -> Local Controller -> Farm Manager -> Cloud Server`. First level that can resolve it handles it. | Multiple potential handlers exist, and the specific handler is resolved dynamically. |
| **State Pattern** | **What** to do in a specific state [19]. | Allow an object to swap behavior when its internal state changes. | **Greenhouse Ventilation:** Fan behavior depends on active state: `Idle State <-> Low-Temp State <-> High-Temp State <-> Cooling State`. | System behavior changes heavily based on its state, avoiding large conditional code blocks. |
| **Command Pattern** | Turn a request into an **Object** [19]. | Encapsulates actions as objects to support logging, queuing, scheduling, and undo/redo. | **Farm Operation Control:** Clicking "Start Pump" builds a `StartPumpCommand` object. This object can be queued, scheduled, logged, or reversed (Stop Pump). | Need to manipulate, log, queue, schedule, or undo requests as self-contained objects. |
| **Observer Pattern** | **Who needs to know** about a change [19]. | Establish a one-to-many relationship to broadcast status changes to observers. | **Soil Moisture Monitor:** Moisture changes trigger notifications to the `Irrigation Controller`, `Mobile App`, `Dashboard`, and `SMS Alert Service` (all Observers). | Changes in one system state must automatically propagate to a dynamic list of subscribers. |

---

### 2. Comprehensive Dhaka Urban Management System (DUMS) Framework
The table below illustrates how a single smart city project can map and solve challenges using all 5 behavioral patterns:

| Pattern | Dhaka Project Scenario | How it Works (Under the Hood) | Main Participants | simplified Java Code Skeleton | Architectural Benefit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Template Method** | **Daily Waste Collection** | Standard process: `Plan Route -> Collect -> Transport -> Dispose`. Each zone has specific waste collection steps. | `WasteCollectionTemplate (Abstract)` -> `MotijheelCollector`, `UttaraCollector` | `abstract class WasteCollection { public final void collect() { planRoute(); collectWaste(); transport(); dispose(); } protected abstract void collectWaste(); }` | Guarantees a standardized operation pipeline while permitting zone-specific implementations. |
| **Chain of Responsibility** | **Citizen Complaint Handling** | Complaint moves: `Call Center -> Ward Office -> City Corporation -> Special Authority` | `ComplaintHandler` -> `CallCenter`, `WardOffice`, `CityCorporation` | `interface ComplaintHandler { void setNext(ComplaintHandler h); void handle(Complaint c); }` | Promotes highly flexible, decoupled, and scalable public department request processing. |
| **State Pattern** | **Bus/Metro Ticket Lifecycle** | A transit ticket behaves differently depending on its active state. | `Ticket (Context)` -> `IssuedState`, `UsedState`, `ExpiredState`, `BlockedState` | `interface TicketState { void process(Card c); } class IssuedState implements TicketState { ... }` | Prevents messy conditional blocks; simplifies modifying and testing ticket transitions. |
| **Command Pattern** | **Smart Traffic Signal Control** | Encapsulates signals as objects (Green, Red, Emergency Stop) for scheduling or logging. | `TrafficApp (Invoker)` -> `Command` -> `TrafficController (Receiver)` | `interface Command { void execute(); void unexecute(); } class StartGreenCommand implements Command { ... }` | Supports queuing, transactional logging, macro scripts, and undo/redo on traffic events. |
| **Observer Pattern** | **Air Quality Monitoring Alerts** | Air stations measure toxicity and instantly push updates to multiple displays. | `AirQualitySensorStation (Subject)` -> `CityDashboard`, `MobileAppCitizen` (Observers) | `class AirQualitySubject { private List<Observer> obs; void notifyObservers() { for(Observer o: obs) o.update(); } }` | Guarantees real-time, instantaneous broadcast of safety information to citizens and agencies. |

---

## Part 4: Real-World Scenarios and Implementations

### Scenario 1: Bank Withdrawal Authorization System
**Problem Statement:** Design a cash withdrawal system with hierarchical check limits [19, 20]:
* Withdrawals < Tk. 10,000 need only **Cashier** authorization [20].
* Withdrawals between Tk. 10,000 and Tk. 1,000,000 need **Cashier** AND **Senior Officer** authorization [20].
* Withdrawals > Tk. 1,00,000 need **Senior Officer** and **Manager** authorization [20].
* Implement this using the **Chain of Responsibility Design Pattern** [20].

#### UML Structure Map
```
                    +-----------------------------+
                    |      Approver (Abstract)    |
                    +-----------------------------+
                    | # nextApprover: Approver    |
                    | + setNextApprover(Approver) |
                    | + approve(amount: double)   | [Abstract]
                    +-----------------------------+
                                   ^
                                   |
            +----------------------+----------------------+
            |                      |                      |
    +---------------+      +---------------+      +---------------+
    |    Cashier    |      | SeniorOfficer |      |    Manager    |
    +---------------+      +---------------+      +---------------+
    | + approve()   |      | + approve()   |      | + approve()   |
    +---------------+      +---------------+      +---------------+
```

#### Java Implementation
```java
// Abstract Handler
abstract class Approver {
    protected Approver nextApprover;

    public void setNextApprover(Approver approver) {
        this.nextApprover = approver;
    }

    public abstract void approve(double amount);
}

// Cashier Handler
class Cashier extends Approver {
    public void approve(double amount) {
        if (amount < 10000) {
            System.out.println("Cashier approved withdrawal of Tk. " + amount);
        } else if (nextApprover != null) {
            nextApprover.approve(amount);
        }
    }
}

// Senior Officer Handler
class SeniorOfficer extends Approver {
    public void approve(double amount) {
        if (amount >= 10000 && amount <= 1000000) {
            System.out.println("Senior Officer approved withdrawal of Tk. " + amount);
        } else if (nextApprover != null) {
            nextApprover.approve(amount);
        }
    }
}

// Manager Handler
class Manager extends Approver {
    public void approve(double amount) {
        if (amount > 1000000) {
            System.out.println("Manager approved withdrawal of Tk. " + amount);
        } else {
            System.out.println("Withdrawal cannot be approved by Manager.");
        }
    }
}

// Client System Execution
public class BankSystem {
    public static void main(String[] args) {
        Approver cashier = new Cashier();
        Approver senior = new SeniorOfficer();
        Approver manager = new Manager();

        // Chain Creation
        cashier.setNextApprover(senior);
        senior.setNextApprover(manager);

        // Processing withdrawal requests
        cashier.approve(5000);
        cashier.approve(50000);
        cashier.approve(5000000);
    }
}
```

#### Output
```
Cashier approved withdrawal of Tk. 5000
Senior Officer approved withdrawal of Tk. 50000
Manager approved withdrawal of Tk. 5000000
```

---

### Scenario 2: Smart Citizen Complaint Notification System (DUMS)
**Problem Statement:** Design a smart city complaint management system where citizens, officers, and administrators are updated automatically as a complaint transitions [25, 26]. Use the **Observer Pattern** [26].

#### UML Diagram
```
        +----------------------------------------+
        |                Complaint               | (Subject)
        +----------------------------------------+
        | - observers: ArrayList<Observer>       |
        | + addObserver(Observer o)              |
        | + changeStatus(status: String)         |
        +----------------------------------------+
                           | (notifies)
                           v
               +-----------------------+
               |       Observer        | (Interface)
               +-----------------------+
               | + update(msg: String) |
               +-----------------------+
                           ^
                           |
            +--------------+--------------+
            |              |              |
     +-----------+  +-----------+  +-------------+
     |  Citizen  |  |  Officer  |  |  Admin      | (Concrete Observers)
     +-----------+  +-----------+  +-------------+
     | + update()|  | + update()|  | + update()  |
     +-----------+  +-----------+  +-------------+
```

#### Java Implementation
```java
import java.util.ArrayList;

// Observer Interface
interface Observer {
    void update(String message);
}

// Concrete Observer 1
class Citizen implements Observer {
    public void update(String message) {
        System.out.println("Citizen Notification: " + message);
    }
}

// Concrete Observer 2
class Officer implements Observer {
    public void update(String message) {
        System.out.println("Officer Alert: " + message);
    }
}

// Concrete Observer 3
class Administrator implements Observer {
    public void update(String message) {
        System.out.println("Admin Dashboard Update: " + message);
    }
}

// Subject Class
class Complaint {
    private ArrayList<Observer> observers = new ArrayList<>();

    public void addObserver(Observer o) {
        observers.add(o);
    }

    public void changeStatus(String status) {
        notifyObservers("Complaint status changed to " + status);
    }

    private void notifyObservers(String message) {
        for (Observer o : observers) {
            o.update(message);
        }
    }
}

// Client execution
public class DUMS {
    public static void main(String[] args) {
        Complaint complaint = new Complaint();
        complaint.addObserver(new Citizen());
        complaint.addObserver(new Officer());
        complaint.addObserver(new Administrator());

        complaint.changeStatus("Completed");
    }
}
```

#### Output
```
Citizen Notification: Complaint status changed to Completed
Officer Alert: Complaint status changed to Completed
Admin Dashboard Update: Complaint status changed to Completed
```

---

### Scenario 3: Intelligent Irrigation Strategy Selection (AAS)
**Problem Statement:** Design an automated agricultural controller that toggles irrigation strategies (Normal, Water-saving, Emergency) at runtime depending on soil weather conditions [29]. Use the **Strategy Design Pattern** [30].

#### UML Diagram
```
  +------------------------------------+
  |         IrrigationController       | (Context)
  +------------------------------------+
  | - strategy: IrrigationStrategy     |
  | + setStrategy(IrrigationStrategy)  |
  | + execute()                        |
  +------------------------------------+
                    |
                    v (delegates to)
        +------------------------+
        |   IrrigationStrategy   | (Interface)
        +------------------------+
        | + irrigate()           |
        +------------------------+
                    ^
                    |
       +------------+------------+
       |                         |
+------------------+     +------------------+
| NormalIrrigation |     |WaterSavingIrrig. | ... (EmergencyIrrigation)
+------------------+     +------------------+
| + irrigate()     |     | + irrigate()     |
+------------------+     +------------------+
```

#### Java Implementation
```java
// Strategy Interface
interface IrrigationStrategy {
    void irrigate();
}

// Concrete Strategy 1
class NormalIrrigation implements IrrigationStrategy {
    public void irrigate() {
        System.out.println("Normal irrigation activated");
    }
}

// Concrete Strategy 2
class WaterSavingIrrigation implements IrrigationStrategy {
    public void irrigate() {
        System.out.println("Water saving irrigation activated");
    }
}

// Concrete Strategy 3
class EmergencyIrrigation implements IrrigationStrategy {
    public void irrigate() {
        System.out.println("Emergency irrigation activated");
    }
}

// Context Class
class IrrigationController {
    private IrrigationStrategy strategy;

    public void setStrategy(IrrigationStrategy strategy) {
        this.strategy = strategy;
    }

    public void execute() {
        strategy.irrigate();
    }
}

// Client execution
public class FarmSystem {
    public static void main(String[] args) {
        IrrigationController controller = new IrrigationController();

        controller.setStrategy(new WaterSavingIrrigation());
        controller.execute();

        controller.setStrategy(new EmergencyIrrigation());
        controller.execute();
    }
}
```

#### Output
```
Water saving irrigation activated
Emergency irrigation activated
```

---

### Scenario 4: Campus Transport Ticket Approval Flow (AAS/Campus)
**Problem Statement:** University transport ticketing needs hierarchical authorization:
* Request < 500 BDT -> handled by **Transport Assistant** [32].
* Request between 500 BDT and 5000 BDT -> handled by **Transport Manager** [32].
* Request > 5000 BDT -> handled by **University Administrator** [32].
* Implement this using **Chain of Responsibility Pattern** [33].

#### Java Implementation
```java
// Abstract Handler
abstract class Approver {
    protected Approver next;

    public void setNext(Approver next) {
        this.next = next;
    }

    public abstract void approve(double amount);
}

// Assistant Handler
class Assistant extends Approver {
    public void approve(double amount) {
        if (amount < 500) {
            System.out.println("Assistant approved request");
        } else if (next != null) {
            next.approve(amount);
        }
    }
}

// Manager Handler
class Manager extends Approver {
    public void approve(double amount) {
        if (amount <= 5000) {
            System.out.println("Manager approved request");
        } else if (next != null) {
            next.approve(amount);
        }
    }
}

// Administrator Handler
class Administrator extends Approver {
    public void approve(double amount) {
        System.out.println("Administrator approved request");
    }
}

// Client Main
public class CampusTransport {
    public static void main(String[] args) {
        Approver assistant = new Assistant();
        Approver manager = new Manager();
        Approver admin = new Administrator();

        // Setup pipeline
        assistant.setNext(manager);
        manager.setNext(admin);

        // Process requests
        assistant.approve(7000);
    }
}
```

#### Output
```
Administrator approved request
```

---

## Part 5: Laboratory Exam Practice & Review Questions

This section provides standard exercises mapped to **Bloom's Taxonomy Levels** to test comprehension of behavioral design patterns.

### 1. Group A: Template Method, Chain of Responsibility, & State Patterns

#### Remember [42, 46]
1. What is a behavioural design pattern? Name five behavioural patterns discussed in Module 2 [42, 46].
2. Identify the core components of the Chain of Responsibility pattern [7, 8].

#### Understand [42, 47]
3. Explain the main purpose of the Template Method Pattern [42].
4. Explain how the Chain of Responsibility Pattern processes a request through multiple handlers [42].
5. Why does the Chain of Responsibility Pattern reduce coupling between a request sender and request receiver [47]?

#### Apply [42, 47]
6. Design a university complaint-handling process using the Chain of Responsibility Pattern, where complaints may be handled by a Class Teacher, Department Chairman, Dean, or Vice Chancellor [42].
7. Apply the Chain of Responsibility Pattern to an academic transport approval system with thresholds: Teacher -> Chairman -> Dean -> Vice Chancellor [47].

#### Analyze [43, 47]
8. Analyze a legacy software module containing a large number of `if-else` or `switch` statements used to determine an object's behavior based on its current state. Explain how the State Pattern could improve the code's clean architecture [43, 47].

#### Evaluate [43, 48]
9. Evaluate the advantages and disadvantages of using the State Pattern instead of a large conditional switch statement in a traffic signal management program [43].
10. Evaluate the advantages and disadvantages of using the Chain of Responsibility Pattern when there is a massive handler list (e.g., more than 20 handlers) [48].

#### Create [43, 48]
11. Design a Java-based online order system using the State Pattern, supporting: `PendingState`, `PaidState`, `ShippedState`, and `DeliveredState` [43].
12. Create a Java-based customer-support system using the Chain of Responsibility Pattern with different support levels: Level 1, Level 2, and Level 3 support handlers [48].

---

### 2. Group B: Command Pattern

#### Remember [43, 45, 48]
1. Define the Command Pattern and identify its main participants [43, 45, 48].

#### Understand [44, 45, 48]
2. Explain the purpose of the Command Pattern and how it encapsulates a request as an object [44, 45, 48].
3. Explain how the Command Pattern supports command queueing, scheduling, and transaction logs [48].
4. Explain how the Command Pattern supports undo and redo operations [44, 45].

#### Apply [44, 45, 49]
5. Apply the Command Pattern to a text editor that supports Copy, Paste, Delete, and Undo operations. Clearly identify the Client, Command, Invoker, and Receiver [44, 45, 49].

#### Analyze [44, 46, 49]
6. Analyze how the Command Pattern reduces coupling between a GUI button and the service class that performs the actual operation [44, 46].
7. Analyze a GUI application where every click listener contains direct application logic. Explain the coupling problem and how Command Pattern can solve it [49].

#### Evaluate [44, 46, 49]
8. Evaluate whether the Command Pattern is appropriate for implementing an undo/redo mechanism. Explain your reasoning [49].

#### Create [45, 46, 49]
9. Design a Java-based remote-control system using the Command Pattern where different buttons can execute different commands such as `LightOnCommand`, `LightOffCommand`, and `FanOnCommand` [45, 46].
10. Create a Java-based restaurant ordering system using the Command Pattern where orders can be created, queued, executed, and cancelled [49].

---

### 3. Group C: Observer Pattern

#### Remember [50]
1. Define the Observer Pattern and identify the roles of Subject and Observer [50].

#### Understand [50]
2. Explain the one-to-many relationship utilized by the Observer Pattern [50].
3. Explain how the Observer Pattern reduces direct dependency between a subject and its dependent objects [50].

#### Apply [50]
4. Apply the Observer Pattern to an online news system where multiple users receive notifications whenever a new article is published [50].

#### Analyze [50]
5. Analyze a weather-monitoring system where the weather station directly calls update methods on every display component. Explain the design problems and suggest how the Observer Pattern could improve the system [50].

#### Evaluate [51]
6. Compare the Observer Pattern with manually notifying every dependent object. Evaluate the advantages of using the Observer Pattern [51].

#### Create [51]
7. Design a Java-based stock-price monitoring system using the Observer Pattern. Include a `StockMarket` Subject and at least three different Observer classes [51].

---

## Part 6: Practice Exam Question Scenarios

### 1. Smart Food Management System (Command Pattern) [38]
**Scenario:** A Smart Food Management System provides online ordering. Customers can Place, Cancel, and Modify orders, and Track delivery. The system should store customer requests so that they can be logged, cancelled, or executed later. The ordering system should allow different commands without directly coupling the customer interface with restaurant operations [38].
* **Requirement:** State the problem the Command Design Pattern solves, explain how it applies to this system, draw the UML diagram, and write the Java implementation [38].
* **Concept:** Encapsulates a request as an object, allowing operations to be stored, queued, logged, or undone [39].

### 2. Smart Traffic Management System (State Pattern) [39]
**Scenario:** A Smart Traffic Management System controls traffic signals at different intersections. A traffic signal changes its behavior depending on its current state [39]:
* `Green State` -> Allow vehicles to move.
* `Yellow State` -> Prepare vehicles to stop.
* `Red State` -> Stop vehicles.
* The behavior must change automatically without complex conditional statements [39].
* **Requirement:** State the problem the State Design Pattern solves, explain how it is used to model this behavior, draw the UML, and write the Java implementation [39].
* **Concept:** Allows an object to change its behavior when its internal state changes [40].

### 3. Smart Agricultural Adapter (Adapter Pattern) [40]
**Scenario:** A Smart Agricultural Automation System uses an existing irrigation controller that accepts data from a standard soil moisture sensor. A newly purchased IoT soil sensor provides moisture information using a different interface. The existing irrigation controller cannot directly communicate with this new sensor [40].
* **Requirement:** State the problem the Adapter Design Pattern solves, explain how it integrates the new IoT soil sensor without modifying the existing controller, draw the UML, and implement the solution [41].