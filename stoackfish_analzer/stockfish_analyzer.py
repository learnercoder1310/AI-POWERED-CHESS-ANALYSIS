import chess
import chess.engine

# Read FEN from file
with open("fen_output.txt", "r") as f:
    fen = f.read().strip()

# Path to Stockfish engine
engine_path = r"D:\Minor\Stockfish\stockfish-windows-x86-64-avx2.exe"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)
print("Stockfish initialized successfully.")

# Create a board from the FEN
board = chess.Board(fen)

try:
    # Perform analysis with Stockfish
    info = engine.analyse(board, chess.engine.Limit(depth=15))

    # Ensure info contains valid analysis data
    if info and "pv" in info and info["pv"]:
        best_move = board.san(info["pv"][0])  # Get the best move in SAN
        evaluation = info["score"].relative.score()  # Get the evaluation (centipawns)

        # Print results
        print("FEN Position:")
        print(fen)
        print("\nBest Move:", best_move)
        print("Evaluation (centipawns):", evaluation)
    else:
        print("Error: No principal variation (pv) found in analysis.")

except chess.engine.EngineTerminatedError as e:
    print("Error: Engine process terminated unexpectedly.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure engine.quit() is called only if the engine is still running
    if engine is not None:
        try:
            engine.quit()
            print("Engine terminated successfully.")
        except chess.engine.EngineTerminatedError:
            print("Engine was already terminated.")
        except Exception as e:
            print(f"Error during engine termination: {e}")