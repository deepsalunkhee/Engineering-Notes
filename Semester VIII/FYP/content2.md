# BlockMeet: A Decentralized Video Conferencing System

# BlockMeet: A Decentralized Video Conferencing System

---

## Chapter 1: Introduction

### 1.1 Background

In recent years, digital communication has witnessed unprecedented growth. With the global shift towards remote work, online education, and virtual collaboration, video conferencing tools have become central to day-to-day operations. Applications like Zoom, Google Meet, and Microsoft Teams dominate the space, providing reliable connectivity and communication. However, these platforms are built on centralized architectures, where a Selective Forwarding Unit (SFU) acts as the core node to process and redistribute video and audio streams.

While centralization offers management ease and control, it introduces several problems:

- **Privacy Risks**: All data routes through central servers, potentially exposing it to unauthorized access.
- **Computational Overhead**: Servers bear the brunt of encoding, decoding, and stream management, requiring heavy infrastructure.
- **Scalability Limitations**: As the number of users increases, centralized servers often struggle to maintain low latency and high quality.

**BlockMeet** is introduced as a novel solution to these issues—a decentralized, peer-to-peer video conferencing system inspired by molecular hydrocarbon structures. By eliminating the dependency on central servers, BlockMeet promotes data privacy, reduces bottlenecks, and encourages scalability through a distributed architecture.

### 1.2 Motivation

The core motivation for BlockMeet stems from the need to protect user data while ensuring a seamless, scalable communication experience. With most current platforms susceptible to centralized data breaches, there exists a clear need for decentralized alternatives.

Drawing inspiration from the fictional concept of a decentralized internet (as featured in "Silicon Valley"), BlockMeet aims to:

- Distribute computational load among peers.
- Ensure media streams remain confined within the meeting participants.
- Decentralize file sharing using IPFS.
- Log actions immutably using blockchain.

### 1.3 Objectives

BlockMeet is designed to:

- Eliminate single-point failures in conferencing.
- Enable fully decentralized file sharing.
- Ensure transparent, tamper-proof meeting logs.
- Be scalable for moderate group sizes (5–15 participants).

### 1.4 Problem Statement

Traditional video conferencing tools suffer from several shortcomings:

1. **Centralized Control**: All data flows through third-party servers, risking privacy.
2. **Server Dependency**: Requires high computational power and dedicated infrastructure.
3. **Scalability Constraints**: Mesh networks (full P2P) are inefficient beyond a few users.

BlockMeet solves this by:

- Introducing a **hydrocarbon-inspired P2P model**.
- Using **IPFS** for decentralized file storage.
- Logging activities on the **Polygon blockchain**.

### 1.5 Methodology

BlockMeet followed an iterative, agile-inspired development lifecycle:

- **Research & Analysis**:
  - Studied existing centralized and decentralized conferencing models.
  - Analyzed limitations of SFU and mesh topologies.
- **Design**:
  - Created a structured hybrid P2P model based on hydrocarbon bonding.
- **Implementation**:
  - Frontend with **React.js**.
  - Backend with **Node.js** and Express.
  - WebSocket-based signaling server.
  - Integration with **IPFS** (via Pinata) for file storage.
  - Smart contracts on **Polygon Testnet** for logging.
- **Testing & Optimization**:
  - Real-time tests with up to 15 participants.
  - CPU and latency benchmarking.

### 1.6 Report Structure

This report is organized as follows:

- **Chapter 2** explores prior art and architectures.
- **Chapter 3** dives into BlockMeet's system design.
- **Chapter 4** elaborates the implementation and core components.
- **Chapter 5** presents results and performance insights.
- **Chapter 6** explains deployment details.
- **Chapter 7** outlines future scope and enhancements.
- **Chapter 8** summarizes findings and contributions.
- **Appendices** include technical artifacts, code snippets, and screenshots.

---

## Chapter 2: Literature Review

### 2.1 Existing Video Conferencing Architectures

#### 2.1.1 Centralized SFU-Based Architecture

Most popular video conferencing tools such as **Zoom**, **Google Meet**, and **Microsoft Teams** employ a centralized model centered around an SFU (Selective Forwarding Unit). In this model:

- Each client sends their audio/video stream to the central SFU.
- The SFU repackages and forwards streams to other participants.

**Advantages:**
- Efficient media routing.
- Easier network management and Quality of Service (QoS).

**Disadvantages:**
- Single point of failure.
- High server-side costs.
- Data privacy concerns.

#### 2.1.2 Super Peer (Hybrid P2P) Architecture

Used by platforms like **Skype**, the super-peer model represents a hybrid between centralized and peer-to-peer systems.

- Select nodes (super peers) handle data relay and distribution.
- These nodes are usually chosen based on system capability (bandwidth, uptime).

**Advantages:**
- Distributes some load away from central servers.
- Can provide improved performance over full-mesh P2P.

**Disadvantages:**
- Still partially centralized.
- Super peers become performance bottlenecks.

#### 2.1.3 Full-Mesh P2P Architecture

In full-mesh P2P:
- Every participant maintains a direct connection to every other participant.

**Advantages:**
- No central server needed.
- Full control over data streams.

**Disadvantages:**
- CPU and bandwidth usage grows quadratically.
- Not scalable beyond 4–6 users.

### 2.2 Decentralized Communication Alternatives

#### 2.2.1 Blockchain-Based Communication

Several research initiatives and applications have attempted to use blockchain in communication for transparency and security. However, limitations include:

- High latency (due to block confirmation times).
- Inability to handle real-time media streams.

Some projects use blockchain only for ancillary services like identity verification and payment.

#### 2.2.2 WebRTC for Real-Time P2P Streaming

**WebRTC** is a protocol suite that allows real-time communication between browsers. It supports:

- Audio/video streaming.
- Data channels for file transfer.
- Encryption by default.

**Challenges with WebRTC:**
- NAT traversal: Requires STUN/TURN servers to establish connections behind firewalls.
- Still needs a signaling mechanism to initiate connections.

### 2.3 File Storage: IPFS

**IPFS (InterPlanetary File System)** is a decentralized protocol for file sharing.

- Files are split into chunks and stored across multiple nodes.
- Each file (or chunk) is identified using a unique content hash.
- Retrieval is hash-based, ensuring immutability.

**Benefits in conferencing:**
- No central server needed.
- Integrity ensured via content addressing.
- Secure sharing with hash access control.

### 2.4 Research Gap and Innovation

Despite the availability of decentralized technologies, few platforms integrate them effectively. Most so-called "decentralized" conferencing apps still depend on:

- Centralized signaling.
- Centralized storage or CDN delivery.
- Server-side logging and management.

**BlockMeet’s Unique Contributions:**
- A **hydrocarbon-inspired architecture** to minimize full-mesh inefficiencies.
- Integration with **IPFS** for file distribution.
- Use of **Polygon blockchain** to log activities immutably.

---



## Chapter 3: System Design & Architecture

### 3.1 Hydrocarbon-Inspired P2P Architecture

BlockMeet introduces a novel architectural concept—**hydrocarbon-inspired peer-to-peer topology**. This design is influenced by the structural properties of hydrocarbons in chemistry, where atoms (peers) connect in chains or rings based on bonding constraints. In BlockMeet:

- **Super Peers** act like carbon atoms with high bonding capacity.
- **Normal Peers** are like hydrogen atoms, connected to super peers.

This structure avoids the inefficiencies of full-mesh models and distributes the load among capable nodes.

#### Structure Formation
When a meeting is created:
- The total number of participants `n` is used to calculate the required super peers:
  
  `SuperPeers = ceil(n / 3)`

- Remaining peers are assigned as **Normal Peers**.
- Each super peer handles connections with its assigned normal peers and connects to other super peers.

This ensures no single node is overwhelmed and allows parallel processing of video/audio streams.

#### Benefits:
- Efficient resource utilization.
- Enhanced scalability (tested up to 15 participants).
- No centralized server for stream forwarding.

### 3.2 System Architecture Overview

The system consists of four major components:

1. **Client Application (React.js)**
   - UI for meeting creation, file sharing, video conferencing.
   - Manages user interaction and media permissions.

2. **Backend Server (Node.js + Express)**
   - Handles user authentication and authorization.
   - Stores metadata about meetings and files.

3. **WebSocket Server**
   - Facilitates real-time peer connection signaling.
   - Implements hydrocarbon P2P connection logic.

4. **Blockchain + IPFS Integration**
   - Smart contract logs meeting activities on Polygon.
   - IPFS stores shared files securely and immutably.

### 3.3 System Workflow

1. **User Authentication**
   - JWT tokens are issued on login/signup.
   - Secured API access across client and server.

2. **Meeting Creation**
   - Host specifies meeting name and participant emails.
   - System calculates and assigns super/normal peers.
   - Peer structure is saved in server memory.

3. **Joining a Meeting**
   - Participants join via WebSocket signaling.
   - Media streams (WebRTC) are exchanged peer-to-peer.

4. **File Upload via IPFS**
   - Files are split into chunks and stored on IPFS.
   - IPFS hash is saved for retrieval.

5. **Activity Logging**
   - Actions (e.g., file upload, join, leave) are logged via smart contracts.
   - Records are stored immutably on the Polygon blockchain.

### 3.4 Architecture Diagram (Descriptive)

While this document cannot display actual images, imagine a diagram with the following components:

- **Client (Browser)** ⟷ **WebSocket Server**
- **Client** ⟷ **Client** (via WebRTC)
- **Client** ⟷ **Backend Server** (REST APIs)
- **Client** ⟷ **IPFS Gateway**
- **Client** ⟷ **Polygon Smart Contract**

Super peers sit at the center of small sub-networks, each connecting to 2–3 normal peers and other super peers.

### 3.5 Design Principles

- **Privacy-first**: No data is passed through a central server.
- **Modularity**: Components (backend, frontend, socket server) are independently deployable.
- **Scalability**: Structure maintains performance as peers increase.
- **Resilience**: No single point of failure.

---



## Chapter 4: Implementation & Core Features

### 4.1 Authentication and Authorization (JWT)

BlockMeet uses **JWT (JSON Web Token)** for secure and efficient user authentication and authorization. JWT ensures stateless session management and reduces the need for repetitive database lookups.

**How It Works:**
- On successful login or signup, the backend issues a signed JWT containing the user ID and email.
- This token is sent to the client and stored in the browser.
- All subsequent API requests include the JWT in the `Authorization` header.
- The backend verifies the token using a secret key, allowing secure access control without session storage.

**Benefits:**
- Lightweight and scalable.
- Provides secure route access.
- Prevents unauthorized access to meeting resources.

### 4.2 Real-Time Communication with WebRTC and WebSockets

**WebRTC (Web Real-Time Communication)** enables direct browser-to-browser media streams. It forms the core of BlockMeet's video conferencing system.

**Key Components:**
- **Media Stream API**: Captures camera and microphone data.
- **RTCPeerConnection**: Handles direct peer-to-peer video/audio connections.
- **ICE (Interactive Connectivity Establishment)**: Assists in network traversal.

**WebSockets** serve as the signaling channel for setting up WebRTC peer connections.

**Signaling Flow:**
1. A user joins a meeting, initiating a WebSocket connection.
2. Signaling messages (offer/answer/ICE candidates) are exchanged via the WebSocket server.
3. Once signaling is complete, direct peer-to-peer communication begins over WebRTC.

The **hydrocarbon-inspired structure** is dynamically formed using logic implemented on the WebSocket server, determining which peers act as super peers and assigning normal peers accordingly.

### 4.3 File Sharing via IPFS

For decentralized file storage, BlockMeet integrates **IPFS (InterPlanetary File System)**.

**Upload Workflow:**
- User selects a file to upload.
- The file is chunked, hashed, and pinned to IPFS via **Pinata**.
- The resulting content hash (CID) is stored in the backend database.
- Anyone with the CID can retrieve the file from the IPFS network.

**Security and Integrity:**
- File content cannot be tampered with due to hash-based addressing.
- Data is split across nodes—no single point contains the full file.

**Example Use Case:** Sharing a PDF agenda or project file during a video call.

### 4.4 Blockchain-Based Activity Logging

To ensure tamper-proof, transparent records of meeting activity, BlockMeet logs actions on the **Polygon blockchain** via smart contracts.

**Logged Events:**
- Meeting creation.
- Participant join/leave.
- File uploads/downloads.

**Implementation Details:**
- Smart contract deployed on the **Polygon Testnet** using the **HardHat** framework.
- Logs include action type, user ID, and timestamp.
- Viewable on block explorers for audit purposes.

**Why Use Blockchain?**
- Immutable and decentralized.
- Ideal for transparent record-keeping.
- Encourages trust and accountability in collaborative environments.

### 4.5 User Interface and Meeting Management

The front end is developed using **React.js** with a minimalist approach for usability.

**Key Screens:**
- **Login/Signup:** Powered by JWT.
- **Dashboard:** Options to create or join meetings.
- **Meeting Room:** Video grid, chat panel, file upload section.

**Meeting Creation Flow:**
- Host specifies a name and email list of participants.
- Backend verifies participant emails.
- Meeting is created, and hydrocarbon structure is assigned.

**Meeting Join Flow:**
- Participants see active meetings on their dashboard.
- Click to join triggers peer connection logic.

---


---

## Chapter 5: Results & Performance Analysis

### 5.1 Performance Testing Overview

To validate the effectiveness and efficiency of BlockMeet, extensive testing was conducted in real-world and simulated environments. The main focus areas were:
- **CPU and memory utilization**
- **Latency between peers**
- **Scalability with increasing participants**
- **Network bandwidth usage**

### 5.2 Scalability and CPU Utilization

Tests were conducted by initiating meetings with different participant sizes. Results showed a clear advantage of the hydrocarbon-inspired model over a traditional full-mesh approach.

| Participants | CPU Usage (Per Peer) | Latency  | Observations                              |
|--------------|----------------------|----------|-------------------------------------------|
| 2            | ~5%                  | <200 ms  | Direct P2P connection, minimal overhead    |
| 5            | ~20%                 | ~300 ms  | Super peer managing multiple peers         |
| 10           | ~40%                 | ~500 ms  | Multiple super peers distribute the load   |
| 15           | ~50–60%              | ~600 ms  | Acceptable performance, no major lags      |

**Note:** When one device was assigned multiple super-peer roles, CPU usage jumped to over 70%, sometimes causing performance issues or system slowdowns.

### 5.3 Latency Analysis

Latency was kept below 600 ms for up to 15 participants, which is considered acceptable for real-time communication. This was primarily due to:
- Efficient signaling using WebSockets
- Peer grouping through the hydrocarbon model
- Reduced number of direct connections per peer

### 5.4 File Sharing Evaluation

Tests for file upload and retrieval through IPFS showed:
- Small files (e.g., text, PDFs) uploaded in <3 seconds
- Media files (images <1 MB) uploaded in 5–8 seconds
- Retrieval using IPFS hashes was reliable and accurate

IPFS performance remained stable due to:
- Pinata gateway support
- Hash-based chunk distribution
- Decentralized retrieval not relying on a single node

### 5.5 Blockchain Logging Reliability

All meeting activities such as joining, file uploads, and exits were logged on the Polygon testnet using smart contracts.

**Advantages Observed:**
- Every log was traceable on block explorers
- Timestamps and user actions were immutable
- No failure observed in contract calls during testing

### 5.6 Bug Reports and Known Issues

- **Mobile camera access inconsistencies:** On some mobile browsers, the camera API occasionally failed to request permissions.
- **Super peer overloading:** If one system handled more than 2 super-peer roles, it led to lag spikes.
- **HTTPS enforcement:** The app works only over HTTPS due to browser media constraints. AWS deployments with HTTP were not functional.

### 5.7 Summary of Findings

- The hydrocarbon-inspired model offers a balance between scalability and performance.
- Decentralization with WebRTC + WebSockets ensures low latency without central servers.
- IPFS integration allows secure, immutable file sharing.
- Blockchain logging enables trusted record-keeping without additional infrastructure.



## Chapter 6: Deployment Strategy

### 6.1 Deployment Architecture

BlockMeet follows a multi-component deployment approach to separate concerns and improve maintainability. The architecture comprises:

1. **Frontend (React.js)**
   - Deployed using **Vercel** for fast and reliable static site hosting.
   - Provides the user interface for authentication, meeting operations, and file management.

2. **Backend Server (Node.js + Express)**
   - Also deployed on **Vercel**.
   - Manages JWT-based authentication and RESTful API endpoints.

3. **WebSocket Server**
   - Hosted on **Render**, as Vercel does not support long-lived WebSocket connections.
   - Handles peer connection signaling and hydrocarbon model logic.

4. **Smart Contracts (Polygon Testnet)**
   - Deployed using the **HardHat** framework.
   - Interactions with the blockchain are performed using Ethers.js from the frontend.

5. **IPFS Integration**
   - Managed using **Pinata**, which provides easy API access for uploading and retrieving files on IPFS.

### 6.2 Challenges in Deployment

#### 6.2.1 Vercel Limitations
- Vercel does not support persistent WebSocket connections required for real-time communication.
- Solution: Moved WebSocket server to **Render**, which allows background processes and WebSocket deployment.

#### 6.2.2 HTTPS Requirement
- WebRTC and media stream access in browsers require HTTPS.
- AWS Elastic Beanstalk deployments by default serve over HTTP, causing issues with media access.
- Free SSL certificate setup on AWS was found to be complex and limited in duration.
- Final decision: Use **Vercel** and **Render**, which natively support HTTPS.

### 6.3 AWS Deployment Experimentation

An experimental deployment on **AWS Elastic Beanstalk** and **Amplify** was attempted:

- **Elastic Beanstalk**: Deployed the backend successfully, but faced SSL issues.
- **Amplify**: Planned for frontend hosting, but did not proceed due to HTTPS limitations.
- **API Gateway + Lambda**: Considered for WebSocket server but not implemented due to time and SSL complexity.

### 6.4 Final Deployment Stack

| Component          | Platform     |
|-------------------|--------------|
| Frontend (React)  | Vercel       |
| Backend (Node.js) | Vercel       |
| WebSocket Server  | Render       |
| Smart Contracts   | Polygon Testnet |
| File Storage      | IPFS via Pinata |

### 6.5 Accessibility

- The deployed application is publicly accessible via a Vercel domain.
- Users can sign up, create meetings, and test all features, including file sharing and blockchain logging.

---
## Chapter 7: Future Scope

While BlockMeet has achieved its goal of building a decentralized video conferencing system with innovative features, there are several enhancements and future directions that can significantly elevate the platform's usability, security, and scalability.

### 7.1 End-to-End Encryption (E2EE)

Currently, BlockMeet uses WebRTC’s default encryption between peers. However, true E2EE requires that even metadata and stream content remain invisible to all intermediate entities, including signaling servers.

**Future Enhancements:**
- Implement E2EE using encryption frameworks like **Insertable Streams API**.
- Ensure key exchange happens exclusively between end users.
- Encrypt metadata and chat messages.

### 7.2 Improved NAT Traversal and Connectivity

Peer-to-peer communication faces challenges when users are behind symmetric NATs or firewalls.

**Proposed Improvements:**
- Integrate more reliable **TURN server** fallback mechanisms.
- Use adaptive STUN/TURN server pools for varying network conditions.
- Explore ICE transport extensions for better candidate prioritization.

### 7.3 Mobile Compatibility and Optimization

While the desktop experience is stable, mobile browser compatibility needs enhancement.

**Goals:**
- Ensure consistent camera/microphone access across Android and iOS.
- Redesign UI for responsive behavior and touch input.
- Explore development of native mobile apps using frameworks like **React Native**.

### 7.4 Dynamic Super Peer Allocation

Currently, super peers are statically assigned at meeting creation.

**Planned Features:**
- Implement **dynamic reassignment** of super peers during the meeting if one drops out.
- Introduce **health checks** for super peers to detect overload or failure.
- Allow seamless peer reassignment to ensure minimal disruptions.

### 7.5 Integration with Identity and Access Control

To support institutional or enterprise use cases:
- Integrate with **OAuth2 providers** (e.g., Google, Microsoft).
- Allow role-based permissions for features like screen sharing, file access.
- Add SSO capabilities for corporate environments.

### 7.6 Extended Logging and Analytics

While the blockchain provides an immutable audit trail, real-time analytics are also important.

**Enhancements:**
- Use off-chain logging tools like **ELK stack** for insights.
- Visualize usage metrics: participant count, file sharing frequency, connection stability.
- Provide audit dashboards for administrators.

### 7.7 Integration with Collaborative Tools

Future versions of BlockMeet could evolve into a complete collaboration suite.

**Ideas:**
- Add **real-time whiteboarding** (Excalidraw-style).
- Shared notepads or markdown editors.
- Version-controlled file attachments.

### 7.8 Blockchain Enhancements

- Consider deploying smart contracts to **Polygon mainnet** or other **L2 chains** for production.
- Explore **ZK-rollups** or **Layer 2 logging mechanisms** to reduce gas costs.
- Introduce token-based access control or NFT-backed meeting permissions.

---









