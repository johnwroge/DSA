# Java Syntax and Built-in Data Structures

```java
// Variables and Data Types
int a = 10;
double b = 20.5;
boolean c = true;
char d = 'A';
String e = "Hello, World!";

// Control Flow Statements

// If-Else
if (condition) {
    // code block
} else if (anotherCondition) {
    // code block
} else {
    // code block
}

// Switch
switch (variable) {
    case value1:
        // code block
        break;
    case value2:
        // code block
        break;
    default:
        // code block
}

// Loops

// For Loop
for (int i = 0; i < 10; i++) {
    // code block
}

// While Loop
while (condition) {
    // code block
}

// Do-While Loop
do {
    // code block
} while (condition);

// Arrays
int[] intArray = {1, 2, 3, 4, 5};
String[] stringArray = {"Hello", "World"};

// ArrayList
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
list.add("Hello");
list.add("World");
String item = list.get(0);
list.remove(0);

// HashMap
import java.util.HashMap;
HashMap<String, Integer> map = new HashMap<>();
map.put("key1", 1);
map.put("key2", 2);
int value = map.get("key1");
map.remove("key1");

// Sets
import java.util.HashSet;
import java.util.Set;
Set<String> set = new HashSet<>();
set.add("Hello");
set.add("World");
set.remove("World");
boolean containsHello = set.contains("Hello");

// Maps
import java.util.Map;
import java.util.TreeMap;
Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("key1", 1);
treeMap.put("key2", 2);
int treeMapValue = treeMap.get("key1");
treeMap.remove("key1");

// Methods
public int add(int x, int y) {
    return x + y;
}

// Classes and Objects
public class MyClass {
    int x;

    public MyClass(int initialX) {
        x = initialX;
    }

    public void setX(int newX) {
        x = newX;
    }

    public int getX() {
        return x;
    }
}

// Creating an Object
MyClass obj = new MyClass(10);
obj.setX(20);
int xValue = obj.getX();

// Inheritance
public class Animal {
    public void makeSound() {
        System.out.println("Animal sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

// Polymorphism
Animal myDog = new Dog();
myDog.makeSound(); // Outputs: Bark

// Interfaces
public interface Animal {
    void makeSound();
}

public class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

// Exception Handling
try {
    int division = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
} finally {
    System.out.println("This block always executes");
}

// File I/O
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}

// Threads
public class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}

MyThread t1 = new MyThread();
t1.start();

// Heaps
import java.util.PriorityQueue;
PriorityQueue<Integer> heap = new PriorityQueue<>();
heap.add(10);
heap.add(20);
heap.add(15);
int min = heap.poll(); // 10 (the smallest element)
