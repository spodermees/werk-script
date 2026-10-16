import time
import threading
import tkinter as tk
from tkinter import messagebox

try:
    import pyautogui
except ImportError as exc:
    raise SystemExit(
        "Je mist een dependency. Installeer deze eerst via: pip install pyautogui pynput"
    ) from exc

try:
    from pynput import keyboard, mouse
except ImportError as exc:
    raise SystemExit(
        "Je mist een dependency. Installeer deze eerst via: pip install pyautogui pynput"
    ) from exc


stop_requested = {"value": False}
positions = []
click_listener = None


class PositionPicker:
    def __init__(self, required_clicks=3):
        self.required_clicks = required_clicks
        self.positions = []
        self.listener = None
        self.window = None
        self.setup_overlay()

    def setup_overlay(self):
        self.window = tk.Tk()
        self.window.attributes("-fullscreen", True)
        self.window.attributes("-alpha", 0.1)
        self.window.configure(bg="black")

        label = tk.Label(
            self.window,
            text=f"Klik {self.required_clicks} keer op het scherm\n(Close venster of ESC om af te breken)",
            bg="black",
            fg="white",
            font=("Arial", 16),
        )
        label.pack(expand=True)
        self.window.bind("<Escape>", lambda e: self.window.destroy())

    def on_click(self, x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            self.positions.append((x, y))
            print(f"Positie {len(self.positions)}: ({x}, {y})")

            if len(self.positions) >= self.required_clicks:
                self.window.destroy()
                self.listener.stop()

    def start(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()
        self.window.mainloop()
        return self.positions


def pick_positions():
    picker = PositionPicker(required_clicks=3)
    selected = picker.start()

    if len(selected) != 3:
        messagebox.showerror("Fout", "Je moet precies 3 posities selecteren!")
        return pick_positions()

    return selected

def on_press(key):
    try:
        if key.char and key.char.lower() == "q":
            stop_requested["value"] = True
            print("Stop gevraagd via 'q'.")
    except AttributeError:
        pass


def perform_clicks(positions):
    print("Script gestart. Druk op 'q' in het toetsenbord om te stoppen.")
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.2
    click_count = 0

    while not stop_requested["value"]:
        for index, (x, y) in enumerate(positions, start=1):
            if stop_requested["value"]:
                print(f"Script gestopt na {click_count} klikken.")
                return

            click_count += 1
            print(f"Klik {index}/{len(positions)} op ({x}, {y}) [Totaal: {click_count}]")
            pyautogui.click(x=x, y=y, button="left")
            time.sleep(0.5)


def main():
    print("=== Auto-Clicker ===")
    print("Selecteer 3 posities door op het scherm te klikken...")
    global positions
    positions = pick_positions()

    print(f"Geselecteerde posities: {positions}")
    time.sleep(2)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        perform_clicks(positions)
    except KeyboardInterrupt:
        print("Script gestopt met Ctrl+C.")
    finally:
        listener.stop()
        print("Klaar!")


if __name__ == "__main__":
    main()
