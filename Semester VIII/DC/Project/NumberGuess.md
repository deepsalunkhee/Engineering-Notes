# **Distributed Number Guessing Game - Technical Documentation**  

## **1. Introduction**  
This document provides a detailed explanation of the **Distributed Number Guessing Game**, a multiplayer game where players compete to guess a randomly selected number (1–25) in real time. The game is built using **Java RMI (Remote Method Invocation)** and follows distributed systems principles such as **clock synchronization, mutual exclusion, deadlock management, and multithreading**.  

### **1.1 Key Features**  
- **Multiplayer Rooms**: Players can create or join game rooms.  
- **Real-Time Guessing**: All players see guesses as they happen.  
- **Server-Managed Logic**: Ensures fairness and synchronization.  
- **Thread-Safe Design**: Prevents race conditions and deadlocks.  

---

## **2. System Architecture**  
The game follows a **client-server model** with the following components:  

### **2.1 Components Overview**  
| **Component**         | **Description** |
|----------------------|----------------|
| **GameServer**       | RMI server handling game logic and synchronization. |
| **GameClient**       | Swing-based GUI for players to interact with the game. |
| **GameRoom**         | Manages players, guesses, and game state for each room. |
| **GameLogic**        | Core game mechanics (room creation, guess validation). |
| **ClockSync**        | Logical clock for event ordering in distributed setup. |

### **2.2 Communication Flow**  
1. **Client connects** to the server via RMI.  
2. **Server creates/joins** a room and manages players.  
3. **Game starts** when enough players join.  
4. **Guesses are submitted** and validated by the server.  
5. **Winner is declared** when the correct number is guessed.  

---

## **3. Core Concepts & Implementation**  

### **3.1 Remote Method Invocation (RMI)**  
- **Purpose**: Allows clients to call server methods remotely.  
- **Key Interface**: `RMIServerInterface` defines all remote methods.  
- **Server Setup**:  
  ```java
  // Server initialization
  GameServer server = new GameServer();
  RMIServerInterface stub = (RMIServerInterface) UnicastRemoteObject.exportObject(server, 0);
  Registry registry = LocateRegistry.createRegistry(Constants.RMI_PORT);
  registry.rebind(Constants.RMI_ID, stub);
  ```
- **Client Connection**:  
  ```java
  Registry registry = LocateRegistry.getRegistry(host, Constants.RMI_PORT);
  server = (RMIServerInterface) registry.lookup(Constants.RMI_ID);
  ```

### **3.2 Logical Clock Synchronization**  
- **Problem**: Events must be ordered correctly across clients.  
- **Solution**: `ClockSync` increments a counter on every RMI call.  
  ```java
  public synchronized void increment() { logicalClock++; }
  ```
- **Usage Example**:  
  ```java
  public String createRoom(String playerName) throws RemoteException {
      clockSync.increment(); // Ensures event ordering
      return gameLogic.createRoom(playerName);
  }
  ```

### **3.3 Mutual Exclusion & Deadlock Prevention**  
- **Challenge**: Multiple clients may try to modify game state simultaneously.  
- **Solution**:  
  - **Synchronized Methods** in `GameLogic` and `GameRoom`.  
  - Example:  
    ```java
    public synchronized boolean joinRoom(String roomId, String playerName) {
        // Only one player can join at a time
    }
    ```
  - **No Nested Locks**: Prevents circular wait (deadlock condition).  

### **3.4 Load Management & Multithreading**  
- **Client-Side Thread**: Continuously checks for game updates.  
  ```java
  private void startUpdateThread() {
      new Thread(() -> {
          while (gameRunning.get()) {
              // Poll server for updates
          }
      }).start();
  }
  ```
- **Server-Side Scaling**: Each `GameRoom` operates independently.  

---

## **4. Class Breakdown**  

### **4.1 GameServer**  
- **Role**: Main RMI server handling remote calls.  
- **Key Methods**:  
  - `createRoom()`, `joinRoom()`, `submitGuess()`, `getWinner()`.  

### **4.2 GameClient**  
- **Role**: Provides GUI and communicates with the server.  
- **Key Features**:  
  - **Login Panel**: Player name input.  
  - **Lobby Panel**: Room selection/creation.  
  - **Game Panel**: Real-time guess display.  

### **4.3 GameRoom**  
- **Role**: Manages per-room game state.  
- **Attributes**:  
  - `players` (List of players).  
  - `targetNumber` (Random number to guess).  
  - `guesses` (Log of all guesses).  

### **4.4 GameLogic**  
- **Role**: Centralized game rules and synchronization.  
- **Key Methods**:  
  - `submitGuess()` (Validates guesses).  
  - `startGame()` (Initializes target number).  

---

## **5. Sequence Diagram (High-Level Flow)**  
```plaintext
Client A                      Server                      Client B
   |                             |                           |
   |--- createRoom() ----------->|                           |
   |                             |--- Room Created           |
   |<-- Room ID ----------------|                           |
   |                             |                           |
   |--- joinRoom() ------------->|                           |
   |                             |--- Player Added           |
   |                             |--- startGame() ---------->|
   |                             |                           |
   |--- submitGuess() ---------->|                           |
   |                             |--- Broadcast Guess ------>|
   |                             |                           |
   |<-- Winner Declared ---------|                           |
```  

---

## **6. Build & Execution**  

### **6.1 Prerequisites**  
- Java JDK 8+  
- RMI Registry enabled  

### **6.2 Running the Game**  
1. **Start Server**:  
   ```bash
   java -cp out server.GameServer
   ```
2. **Start Client**:  
   ```bash
   java -cp out client.GameClient
   ```
3. **Gameplay**:  
   - Enter name → Create/Join room → Start guessing!  

---

## **7. Future Enhancements**  
1. **UDP for Broadcasts**: Faster real-time updates.  
2. **Leaderboard**: Track player stats.  
3. **Fault Tolerance**: Handle server crashes gracefully.  

---

## **8. Conclusion**  
This project demonstrates key distributed systems concepts in a practical, interactive game. By using **RMI, logical clocks, and synchronized methods**, it ensures fairness, consistency, and real-time responsiveness.  

**GitHub Repository**: [Link if applicable]  
**Author**: [Your Name]  

---

This documentation provides a **comprehensive** yet **clear** breakdown of the system. Let me know if you'd like any section expanded! 🚀
