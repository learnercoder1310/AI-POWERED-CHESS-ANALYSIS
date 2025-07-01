import cv2
import numpy as np
from ultralytics import YOLO
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "static/uploads/sample.jpg"

image = cv2.imread(image_path)
assert image is not None, f"Failed to load image from: {image_path}"

# Mapping YOLOv8 class names to FEN notation
piece_map = {
    'black-bishop': 'b', 'black-king': 'k', 'black-knight': 'n', 'black-pawn': 'p',
    'black-queen': 'q', 'black-rook': 'r',
    'white-bishop': 'B', 'white-king': 'K', 'white-knight': 'N', 'white-pawn': 'P',
    'white-queen': 'Q', 'white-rook': 'R'
}

def map_to_board_coordinates(x_center, y_center, board_width=800, board_height=800):
    col = int(x_center / (board_width / 8))
    row = int(y_center / (board_height / 8))
    return col, row

# ✅ Fix: Flip the board vertically to map rank 8 at top and rank 1 at bottom
def flip_board_vertically(board):
    return board[::-1]

def generate_fen_from_detections(detections, image_shape=(800, 800)):
    board = [['' for _ in range(8)] for _ in range(8)]
    for det in detections:
        label = det['label']
        x, y, w, h = det['bbox']
        x_center = x + w / 2
        y_center = y + h / 2
        col, row = map_to_board_coordinates(x_center, y_center, *image_shape)
        if 0 <= row < 8 and 0 <= col < 8:
            board[row][col] = piece_map.get(label, '')

    # ✅ Apply fix to correct orientation
    board = flip_board_vertically(board)

    fen_rows = []
    for row in board:
        fen_row = ''
        empty = 0
        for cell in row:
            if cell == '':
                empty += 1
            else:
                if empty > 0:
                    fen_row += str(empty)
                    empty = 0
                fen_row += cell
        if empty > 0:
            fen_row += str(empty)
        fen_rows.append(fen_row)
    return '/'.join(fen_rows)

def generate_fen_from_image(image_path):
    image = cv2.imread(image_path)
    assert image is not None, f"Failed to load image at {image_path}"

    warped_board = cv2.resize(image, (800, 800))
    model = YOLO("best.pt")
    results = model(warped_board, imgsz=800, conf=0.5)[0]

    detections = []
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        label_idx = int(box.cls[0])          `        
        label = model.names[label_idx]
        conf = float(box.conf[0])
        detections.append({
            'label': label,
            'confidence': conf,
            'bbox': [x1, y1, x2 - x1, y2 - y1]
        })

    fen = generate_fen_from_detections(detections)
    full_fen = f"{fen} w - - 0 1"

    with open("fen_output.txt", "w") as f:
        f.write(full_fen + "\n")

    return full_fen

# ✅ Executable block
if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "uploads/sample.jpg"
    try:
        fen = generate_fen_from_image(image_path)
        print("Generated FEN:", fen)
    except Exception as e:
        print("Error:", str(e))
