import tkinter as tk
import random

# Define the size of the maze
WIDTH = 21  # Must be an odd number
HEIGHT = 21  # Must be an odd number
CELL_SIZE = 20

# Directions for moving in the maze (right, left, down, up)
DIRS = [(2, 0), (-2, 0), (0, 2), (0, -2)]
MOVE_DIRS = {"Right": (1, 0), "Left": (-1, 0), "Down": (0, 1), "Up": (0, -1)}


class MazeGame:
    """
    A class to represent a Maze game using Tkinter for GUI.

    Attributes:
    ----------
    width : int
        Width of the maze in cells
    height : int
        Height of the maze in cells
    cell_size : int
        Size of each cell in pixels
    maze : list
        2D list representing the maze layout
    player_pos : list
        List representing the player's position [x, y]
    visited : set
        Set of visited positions by the player
    root : Tk
        Tkinter root window
    canvas : Canvas
        Tkinter canvas to draw the maze and player

    Methods:
    -------
    create_maze():
        Generates the maze using a randomized depth-first search algorithm.
    draw_maze():
        Draws the maze on the Tkinter canvas.
    draw_player():
        Draws the player on the Tkinter canvas.
    move_player(event):
        Handles player movement based on key press events.
    update_visited_paths():
        Updates the color of the visited paths to light green.
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the MazeGame class with the given width, height, and cell size.
        Sets up the Tkinter window, canvas, and binds key press events.

        Parameters:
        ----------
        width : int
            Width of the maze in cells
        height : int
            Height of the maze in cells
        cell_size : int
            Size of each cell in pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = self.create_maze()  # Create the maze
        self.player_pos = [0, 1]  # Start position
        self.visited = set()  # Set to keep track of visited positions
        self.root = tk.Tk()  # Initialize the Tkinter root window
        self.root.title("Random Maze Generator")
        self.canvas = tk.Canvas(
            self.root,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            bg="black",
        )
        self.canvas.pack()
        self.draw_maze()  # Draw the maze on the canvas
        self.draw_player()  # Draw the player on the canvas
        self.root.bind(
            "<KeyPress>", self.move_player
        )  # Bind key press events to move_player method
        self.root.mainloop()  # Start the Tkinter event loop

    def create_maze(self):
        """
        Generates the maze using a randomized depth-first search algorithm.
        Ensures that there is a path from the entrance to the exit.

        Returns:
        -------
        list
            2D list representing the maze layout
        """
        maze = [
            [1 for _ in range(self.width)] for _ in range(self.height)
        ]  # Start with walls everywhere
        stack = [(1, 1)]  # Stack to keep track of the current path
        maze[1][1] = 0  # Starting point

        while stack:
            x, y = stack[-1]  # Get the current position

            # Shuffle the directions to randomize the path
            random.shuffle(DIRS)
            # Get the list of unvisited neighbors
            neighbors = [
                (x + dx, y + dy)
                for dx, dy in DIRS
                if 0 < x + dx < self.width - 1
                and 0 < y + dy < self.height - 1
                and maze[y + dy][x + dx] == 1
            ]

            if neighbors:
                nx, ny = random.choice(neighbors)  # Choose a random neighbor
                stack.append((nx, ny))  # Add the neighbor to the stack
                maze[ny][nx] = 0  # Mark the neighbor as a path
                maze[ny - (ny - y) // 2][nx - (nx - x) // 2] = (
                    0  # Remove the wall between cells
                )
            else:
                stack.pop()  # Backtrack if no unvisited neighbors

        # Ensure there is a path from the start to the end
        maze[1][0] = 0  # Entrance
        maze[self.height - 2][self.width - 1] = 0  # Exit

        return maze

    def draw_maze(self):
        """
        Draws the maze on the Tkinter canvas.
        Colors the entrance green and the exit red.
        """
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                color = "white" if self.maze[y][x] == 0 else "black"  # Path or wall
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill=color,
                )
        # Draw the entrance
        self.canvas.create_rectangle(
            0, self.cell_size, self.cell_size, 2 * self.cell_size, fill="green"
        )
        # Draw the exit
        self.canvas.create_rectangle(
            (self.width - 1) * self.cell_size,
            (self.height - 2) * self.cell_size,
            self.width * self.cell_size,
            (self.height - 1) * self.cell_size,
            fill="red",
        )

    def draw_player(self):
        """
        Draws the player on the Tkinter canvas at the current player position.
        """
        x, y = self.player_pos
        self.canvas.create_rectangle(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill="blue",
            tags="player",
        )

    def move_player(self, event):
        """
        Handles player movement based on key press events.
        Updates the player's position and marks the path as visited.
        Checks for the win condition.

        Parameters:
        ----------
        event : Event
            Key press event
        """
        dx, dy = MOVE_DIRS.get(event.keysym, (0, 0))  # Get the direction of movement
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Check if the new position is within the bounds and is a path
        if (
            0 <= new_x < self.width
            and 0 <= new_y < self.height
            and self.maze[new_y][new_x] == 0
        ):
            self.visited.add(tuple(self.player_pos))  # Mark current position as visited
            self.player_pos = [new_x, new_y]  # Update player position
            self.canvas.delete("player")  # Remove the old player position
            self.draw_player()  # Draw the new player position
            self.update_visited_paths()  # Update the visited paths

            # Check for win condition
            if new_x == self.width - 1 and new_y == self.height - 2:
                self.canvas.create_text(
                    self.width * self.cell_size / 2,
                    self.height * self.cell_size / 2,
                    text="You Win!",
                    fill="yellow",
                    font=("Helvetica", 24),
                )

    def update_visited_paths(self):
        """
        Updates the color of the visited paths to light green.
        Redraws the player on top of the light green paths if currently on them.
        """
        self.canvas.delete("player")  # Remove the player to redraw it on top if necessary
    
        # First redraw all visited paths
        for pos in self.visited:
            x, y = pos
            fill_color = "light green"
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill=fill_color,
            )
    
        # Then redraw the player at its current position
        x, y = self.player_pos
        self.canvas.create_rectangle(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill="blue",
            tags="player",
        )



if __name__ == "__main__":
    MazeGame(WIDTH, HEIGHT, CELL_SIZE)
