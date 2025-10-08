import tkinter as tk
from app import Enemy


class GameUI:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Enemy Battle Game")
        self.root.geometry("800x800")

        # Create a canvas
        self.canvas = tk.Canvas(
            self.root,
            width=550,
            height=550,
            bg="lightgray",
            relief="solid",
            borderwidth=1
        )
        self.canvas.pack(pady=20)

        # Enemy size (square dimensions)
        self.enemy_size = 40

        # Movement settings
        self.move_distance = 20
        self.canvas_width = 750
        self.canvas_height = 550

        # Create enemies with positions and colors
        self.enemies = [
            Enemy(100, 5, "Slajm", 150, 200, "green", "darkgreen"),
            Enemy(160, 10, "Goblin", 500, 200, "red", "darkred"),
            Enemy(200, 15, "Troll", 300, 300, "blue", "darkblue")
        ]

        # Draw enemies on canvas
        self.draw_enemies()

        # Create control panels
        self.create_control_panels()

    def draw_enemies(self):
        """Draw all enemies as colored squares on the canvas"""
        # Clear canvas first
        self.canvas.delete("all")

        # Draw each enemy
        for enemy in self.enemies:
            if enemy.alive:
                # Draw rectangle
                self.canvas.create_rectangle(
                    enemy.x, enemy.y,
                    enemy.x + enemy.size, enemy.y + enemy.size,
                    fill=enemy.color,
                    outline=enemy.outline,
                    width=2
                )
                # Add label
                self.canvas.create_text(
                    enemy.x + enemy.size//2, enemy.y - 15,
                    text=f"{enemy.name} ({enemy.health} HP)",
                    fill="black"
                )

    def move_enemy(self, enemy_index, direction):
        """Move specified enemy in the given direction"""
        enemy = self.enemies[enemy_index]
        enemy.move_direction(
            direction,
            self.move_distance,
            self.canvas_width,
            self.canvas_height
        )
        self.draw_enemies()

    def create_enemy_controls(self, parent_frame, enemy_name, enemy_index):
        """Create control panel for a single enemy"""
        frame = tk.Frame(parent_frame)
        frame.pack(side=tk.LEFT, padx=20)

        # Title
        tk.Label(frame, text=f"{enemy_name} Controls",
                 font=("Arial", 12, "bold")).grid(row=0, column=1, pady=5)

        # Arrow buttons in cross pattern
        directions = [
            ("↑", "up", 1, 1),
            ("←", "left", 2, 0),
            ("→", "right", 2, 2),
            ("↓", "down", 3, 1)
        ]

        for arrow, direction, row, col in directions:
            tk.Button(frame, text=arrow, width=3, height=1,
                      command=lambda d=direction: self.move_enemy(
                          enemy_index, d)
                      ).grid(row=row, column=col)

    def create_control_panels(self):
        """Create movement control panels for both enemies"""
        # Frame for all controls
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Create controls for each enemy
        for i, enemy in enumerate(self.enemies):
            self.create_enemy_controls(control_frame, enemy.name, i)

    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()


# Create and run the application
if __name__ == "__main__":
    app = GameUI()
    app.run()
