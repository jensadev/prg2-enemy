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
            Enemy("Slajm", 100, 5, 40, 20, 150, 200, "green", "darkgreen"),
            Enemy("Goblin", 160, 10, 40, 20, 450, 200, "red", "darkred")
        ]
        
        # Game loop settings
        self.running = False
        self.update_interval = 50  # milliseconds between updates
        
        # Draw enemies on canvas
        self.draw_all_enemies()

        # Create control panels
        self.create_control_panels()
        
        # Start the game loop
        self.start_game_loop()

    def draw_all_enemies(self):
        """Clear canvas and let each enemy draw itself"""
        self.canvas.delete("all")
        for enemy in self.enemies:
            enemy.draw(self.canvas)
    
    def update_game(self):
        """Main game update loop - called every frame"""
        if self.running:
            # Update all enemies
            for enemy in self.enemies:
                enemy.update(self.canvas_width, self.canvas_height)
            
            # Redraw everything
            self.draw_all_enemies()
            
            # Schedule next update
            self.root.after(self.update_interval, self.update_game)
    
    def start_game_loop(self):
        """Start the main game loop"""
        self.running = True
        self.update_game()
    
    def stop_game_loop(self):
        """Stop the main game loop"""
        self.running = False

    def move_enemy(self, enemy_index, direction):
        """Queue movement for specified enemy"""
        enemy = self.enemies[enemy_index]
        enemy.queue_movement(direction)

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
        print("Starting Enemy Battle Game with game loop architecture...")
        self.root.mainloop()
        # Stop game loop when window closes
        self.stop_game_loop()


# Create and run the application
if __name__ == "__main__":
    app = GameUI()
    app.run()
