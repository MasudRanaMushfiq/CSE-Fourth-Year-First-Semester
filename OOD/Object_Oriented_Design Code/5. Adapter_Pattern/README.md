# 📘 Adapter Design Pattern

## 📌 Overview

The **Adapter Pattern** is a **Structural Design Pattern** that allows two **incompatible interfaces** to work together.
It acts as a **bridge** between existing classes without modifying their source code.

A real-world example is a **card reader**, which adapts a memory card so it can be read by a laptop.

---

## 🎯 Intent

* Convert one interface into another
* Enable reuse of existing code
* Improve system flexibility

---

## 🧠 Key Components

* **Target Interface** → MediaPlayer
* **Adaptee Interface** → AdvancedMediaPlayer
* **Adapter** → MediaAdapter
* **Client** → AudioPlayer

---

## 🧩 UML Concept (Textual)

```
Client → MediaPlayer → Adapter → AdvancedMediaPlayer
```

---

## 🛠 Implementation Steps

### Step 1: Create MediaPlayer Interfaces

```java
interface MediaPlayer {
    void play(String audioType, String fileName);
}

interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}
```

---

### Step 2: Create Advanced Media Players

```java
class VlcPlayer implements AdvancedMediaPlayer {
    public void playVlc(String fileName) {
        System.out.println("Playing vlc file. Name: " + fileName);
    }
    public void playMp4(String fileName) {}
}

class Mp4Player implements AdvancedMediaPlayer {
    public void playVlc(String fileName) {}
    public void playMp4(String fileName) {
        System.out.println("Playing mp4 file. Name: " + fileName);
    }
}
```

---

### Step 3: Create Adapter Class

```java
class MediaAdapter implements MediaPlayer {

    AdvancedMediaPlayer advancedPlayer;

    MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("vlc"))
            advancedPlayer = new VlcPlayer();
        else if (audioType.equalsIgnoreCase("mp4"))
            advancedPlayer = new Mp4Player();
    }

    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc"))
            advancedPlayer.playVlc(fileName);
        else if (audioType.equalsIgnoreCase("mp4"))
            advancedPlayer.playMp4(fileName);
    }
}
```

---

### Step 4: Create AudioPlayer (Client)

```java
class AudioPlayer implements MediaPlayer {

    MediaAdapter mediaAdapter;

    public void play(String audioType, String fileName) {

        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("Playing mp3 file. Name: " + fileName);
        }
        else if (audioType.equalsIgnoreCase("vlc") || audioType.equalsIgnoreCase("mp4")) {
            mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        }
        else {
            System.out.println("Invalid media. " + audioType + " format not supported");
        }
    }
}
```

---

## ▶️ Demo / Usage

```java
public class AdapterPatternDemo {
    public static void main(String[] args) {

        AudioPlayer audioPlayer = new AudioPlayer();

        audioPlayer.play("mp3", "beyond the horizon.mp3");
        audioPlayer.play("mp4", "alone.mp4");
        audioPlayer.play("vlc", "far far away.vlc");
        audioPlayer.play("avi", "mind me.avi");
    }
}
```

---

## 📤 Output

```
Playing mp3 file. Name: beyond the horizon.mp3
Playing mp4 file. Name: alone.mp4
Playing vlc file. Name: far far away.vlc
Invalid media. avi format not supported
```

---

## ✅ Advantages

* Enables compatibility between incompatible interfaces
* Promotes code reuse
* Follows Open/Closed Principle

---

## ❌ Disadvantages

* Adds extra classes
* Can increase complexity

---

## 📌 Common Use Cases

* Media players
* Payment gateways
* Legacy system integration
* Hardware adapters

---

## 🏁 Conclusion

The **Adapter Pattern** is ideal when existing systems need to work together without modifying their source code. It improves flexibility while maintaining clean architecture.

---
