# ♟️ AI-Powered Chess Analysis

**AI-Powered Chess Analysis** is an intelligent and user-friendly system designed to analyze chessboard positions directly from an image and provide optimal move suggestions. By combining advanced computer vision techniques with a powerful chess engine, the system allows users to simply upload a photo of a chessboard and receive accurate, real-time analysis.

Utilizing the YOLOv8 object detection model for identifying each piece and the Stockfish engine for move calculation, the project offers a seamless blend of AI and strategic gameplay support. Whether you're a casual player or a chess enthusiast, this tool helps you understand the board better and make smarter decisions — all through the power of artificial intelligence.

---
![image alt](https://github.com/learnercoder1310/AI-POWERED-CHESS-ANALYSIS/blob/a5bb1d0fd15aef189020f155484c0595fd8fa482/final_output/upload_image.png)

## 🎯 Features

- 📷 **Image-Based Chessboard Detection**  
  Detects the current positions of all pieces from a user-uploaded image.

- 🧠 **AI-Based FEN Generation**  
  Automatically generates the Forsyth–Edwards Notation (FEN) from the detected board state.

- ♜ **Stockfish-Powered Best Move Suggestions**  
  Utilizes the powerful Stockfish chess engine to calculate the best possible move.

- 🌐 **User-Friendly Frontend**  
  Built with basic HTML, CSS, and JavaScript for fast and intuitive interaction.

- 🔁 **Real-Time Feedback Loop**  
  Upload → Detect → Analyze → Suggest, all in a seamless pipeline.

---

## 🛠 Tech Stack

| Layer     | Technology             |
|-----------|------------------------|
| Frontend  | HTML, CSS, JavaScript  |
| Backend   | Python (Flask)         |
| Detection | YOLOv8 (Ultralytics)   |
| Chess AI  | Stockfish (open-source)|
| ML Model  | Custom-trained on chess pieces |

---

## 🚀 How It Works

1. **Upload** an image of a chessboard via the web interface.  
2. The **YOLOv8** model identifies the positions and types of pieces on the board.  
3. These detections are used to generate a **FEN (Forsyth–Edwards Notation)** string.  
4. The FEN string is passed to the **Stockfish** engine.  
5. Stockfish suggests the **best move**, which is displayed on the frontend.

---

> ⚡ This project demonstrates the real-world potential of computer vision and AI in traditional strategy games.
