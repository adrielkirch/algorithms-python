import tkinter as tk
import random
from collections import deque
import heapq

# Define the size of the maze
WIDTH = 31  # Must be an odd number
HEIGHT = 31  # Must be an odd number
CELL_SIZE = 20

# Directions for moving in the maze (right, left, down, up)
DIRS = [(2, 0), (-2, 0), (0, 2), (0, -2)]
MOVE_DIRS = {"Right": (1, 0), "Left": (-1, 0), "Down": (0, 1), "Up": (0, -1)}


class MazeGame:
    """
    A class to represent a maze game with different pathfinding algorithms.

    This class creates a maze, initializes a graphical user interface (GUI) using Tkinter,
    and provides various algorithms to find a path through the maze. It supports Depth-First Search (DFS),
    Breadth-First Search (BFS), Dijkstra's Algorithm, and A* Algorithm for pathfinding. The player can move
    within the maze using keyboard controls.

    Attributes:
        width (int): The width of the maze in cells.
        height (int): The height of the maze in cells.
        cell_size (int): The size of each cell in pixels.
        maze (list[list[int]]): 2D list representing the maze grid (0 for open path, 1 for wall).
        player_pos (list[int]): The current position of the player in the maze.
        visited (set[tuple[int, int]]): Set of visited positions during pathfinding.
        root (tk.Tk): The main Tkinter window.
        canvas (tk.Canvas): The canvas used to draw the maze and player.
        dfs_button (tk.Button): Button to start Depth-First Search.
        bfs_button (tk.Button): Button to start Breadth-First Search.
        dijkstra_button (tk.Button): Button to start Dijkstra's Algorithm.
        a_star_button (tk.Button): Button to start A* Algorithm.
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the MazeGame class.

        Args:
            width (int): The width of the maze in cells.
            height (int): The height of the maze in cells.
            cell_size (int): The size of each cell in pixels.

        Sets up the maze, GUI components, and initializes player position.
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = self.create_maze()  # Create the maze
        self.player_pos = [0, 1]  # Start position
        self.visited = set()  # Set to keep track of visited positions
        self.root = tk.Tk()  # Initialize the Tkinter root window
        self.root.title("Maze algorithms solver")
        self.canvas = tk.Canvas(
            self.root,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            bg="black",
        )
        # Create and pack buttons for different pathfinding algorithms
        self.canvas.pack()
        self.dfs_button = tk.Button(self.root, text="DFS", command=self.dfs_bot)
        self.dfs_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bfs_button = tk.Button(self.root, text="BFS", command=self.bfs_bot)
        self.bfs_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.dijkstra_button = tk.Button(
            self.root, text="Dijkstra", command=self.dijkstra_bot
        )
        self.dijkstra_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.a_star_button = tk.Button(
            self.root, text="A* Algorithm", command=self.a_star_bot
        )
        self.a_star_button.pack(side=tk.LEFT, padx=5, pady=5)
        # Draw the maze and player on the canvas
        self.draw_maze()  # Draw the maze on the canvas
        self.draw_player()  # Draw the player on the canvas
        # Bind key press events to move the player
        self.root.bind("<KeyPress>", self.move_player)
        self.root.mainloop()  # Start the Tkinter event loop

    def create_maze(self):
        """
        Generates a random maze using the Depth-First Search (DFS) algorithm.

        This method initializes a maze grid where all cells are initially walls. It then
        uses a stack-based approach to create a path through the maze. The path is created
        by randomly selecting neighboring cells, marking them as part of the path, and
        removing walls between cells. The maze is ensured to have an entrance and an exit.

        The resulting maze is a 2D list where:
        - `0` represents a path.
        - `1` represents a wall.

        Returns:
            list[list[int]]: A 2D list representing the generated maze. Each cell in the maze
            is either a `0` (path) or `1` (wall).

        Algorithm:
            1. Initialize the maze grid with walls (`1`).
            2. Set the starting position at `(1, 1)` as a path (`0`).
            3. Use a stack to keep track of the current path.
            4. Shuffle possible directions to ensure randomness.
            5. For each position:
                - Check the unvisited neighboring cells.
                - If there are unvisited neighbors, randomly select one, mark it as a path,
                  and remove the wall between the current cell and the neighbor.
                - If no unvisited neighbors are available, backtrack by popping the stack.
            6. Ensure there is an entrance at `(1, 0)` and an exit at `(self.height - 2, self.width - 1)`.
            7. Return the generated maze.

        Notes:
            - The maze is guaranteed to have at least one path from the entrance to the exit.
            - The `DIRS` variable should be defined elsewhere in the code, typically as a list of possible directions
              [(0, 1), (1, 0), (0, -1), (-1, 0)] representing right, down, left, and up, respectively.
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
                maze[ny - (ny - y) // 2][
                    nx - (nx - x) // 2
                ] = 0  # Remove the wall between cells
            else:
                stack.pop()  # Backtrack if no unvisited neighbors

        # Ensure there is a path from the start to the end
        maze[1][0] = 0  # Entrance
        maze[self.height - 2][self.width - 1] = 0  # Exit

        return maze

    def draw_maze(self):
        """
        Draws the generated maze onto the Tkinter canvas.

        This method iterates over the 2D list representing the maze and draws each cell as a rectangle on
        the canvas. The color of the rectangle is determined by whether the cell is a path or a wall. The
        method also draws the entrance and exit of the maze with distinct colors.

        The maze is visualized as follows:
        - `0` (path) is drawn in white.
        - `1` (wall) is drawn in black.
        - The entrance is marked in green.
        - The exit is marked in red.

        Process:
            1. Iterate through each cell in the maze.
                - For each cell, determine its color based on its value (`0` or `1`).
                - Draw a rectangle representing the cell at the appropriate position on the canvas.
            2. Draw a green rectangle to represent the entrance of the maze.
            3. Draw a red rectangle to represent the exit of the maze.

        Canvas Coordinates:
            - The top-left corner of the canvas is at (0, 0).
            - Each cell's position is calculated based on its index in the maze and the cell size.
            - The entrance is drawn at the top-left corner.
            - The exit is drawn at the bottom-right corner.

        Notes:
            - The canvas is assumed to be initialized with dimensions large enough to accommodate the entire maze.
            - The entrance and exit rectangles are hardcoded to specific sizes and positions based on the cell size.
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
        Draws the player on the Tkinter canvas.

        This method places a visual representation of the player at the current position on the canvas.
        The player is drawn as a blue rectangle, and is tagged with "player" for easy identification and manipulation.

        Process:
            1. Retrieve the current position of the player from `self.player_pos`.
            2. Calculate the top-left and bottom-right coordinates of the rectangle representing the player
               based on the player's position and the cell size.
            3. Draw a blue rectangle at the calculated coordinates on the canvas.
            4. Assign the tag "player" to the rectangle, which allows for easy manipulation or identification later.

        Canvas Coordinates:
            - The top-left corner of the player rectangle is calculated as `(x * self.cell_size, y * self.cell_size)`.
            - The bottom-right corner of the player rectangle is calculated as `((x + 1) * self.cell_size, (y + 1) * self.cell_size)`.

        Notes:
            - The `self.player_pos` attribute should contain the current (x, y) position of the player in the maze.
            - If the player is moved or if the maze is redrawn, this method should be called to update the player's position on the canvas.
            - The "player" tag allows for potential future use cases, such as moving or updating the player's position on the canvas.

        Example:
            If `self.player_pos` is `[2, 3]` and `self.cell_size` is `20`, the player will be drawn as a blue rectangle
            from `(40, 60)` to `(60, 80)` on the canvas.
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
        Moves the player on the canvas based on keyboard input.

        This method is triggered by key press events and updates the player's position on the canvas accordingly.
        It also handles checking if the new position is valid (i.e., within maze boundaries and not a wall),
        updates the visited paths, and checks for a win condition.

        Parameters:
            event (tk.Event): The Tkinter event object containing information about the key press.

        Process:
            1. Retrieve the direction of movement based on the key pressed. `MOVE_DIRS` maps key symbols to movement offsets (dx, dy).
            2. Calculate the new position `(new_x, new_y)` by adding the direction offsets to the current player position.
            3. Check if the new position is within the maze boundaries and is a path (value of 0 in `self.maze`).
            4. If the new position is valid:
                - Mark the current position as visited by adding it to `self.visited`.
                - Update the player's position to the new coordinates.
                - Remove the previous player representation from the canvas.
                - Redraw the player at the new position.
                - Update the visualization of visited paths.
                - Check for a win condition (if the player reaches the exit) and display a "You Win!" message.

        Notes:
            - The `event.keysym` attribute provides the symbol of the key pressed, which is used to determine the direction of movement.
            - The `MOVE_DIRS` dictionary should be defined elsewhere in the class, mapping key symbols (e.g., "Up", "Down", "Left", "Right") to movement offsets.
            - The win condition is checked by comparing the player's position with the exit coordinates.

        Example:
            If the `event.keysym` is "Right" and `MOVE_DIRS` is set such that "Right" maps to `(1, 0)`, the player will move one cell to the right.
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
        Updates the canvas to reflect the visited paths and redraw the player.

        This method is responsible for visualizing the cells that the player has visited
        by updating their appearance on the canvas. It first removes the player from the canvas
        to ensure that it is redrawn on top of the visited paths. Then, it iterates through
        the set of visited positions and updates their appearance. Finally, the player is
        redrawn at its current position.

        Process:
            1. Remove the existing player representation from the canvas to ensure it is not
               obscured by the visited path drawings.
            2. Iterate over the positions stored in `self.visited` and draw each visited cell
               with a specified color to indicate that it has been traversed.
            3. Redraw the player at its current position to ensure it is visible above the
               visited paths.

        Notes:
            - `self.visited` should be a set of tuples where each tuple represents a
              (x, y) coordinate of a cell that has been visited by the player.
            - The `fill_color` used for visited paths is set to "light green".
            - The player is always drawn with a "blue" fill color.
            - The player must be redrawn after the visited paths to ensure it is not covered.

        Example:
            If the player has visited the cells at coordinates (1, 1) and (2, 2),
            these cells will be drawn with a "light green" color, and the player
            will be drawn with a "blue" color at its current position.
        """
        self.canvas.delete(
            "player"
        )  # Remove the player to redraw it on top if necessary

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

    def clear_search_paths(self):
        """
        Clears the canvas of all search path indicators and redraws the maze.

        This method is used to remove any temporary visual markers indicating search paths
        from the canvas. It iterates over the entire maze and resets the color of cells
        that were previously marked during a search algorithm (e.g., A* or BFS). The maze
        is then redrawn with its original appearance, including the entrance and exit.

        Process:
            1. Iterate through each cell in the maze.
            2. For cells that are part of the maze path (indicated by a value of 0 in `self.maze`),
               reset their color to white, which represents an open path.
            3. Redraw the entrance of the maze at the top-left corner in green.
            4. Redraw the exit of the maze at the bottom-right corner in red.

        Notes:
            - This method is typically called to reset the visual representation of the maze
              after a search algorithm has been executed and its path markers need to be cleared.
            - The entrance is drawn as a green rectangle, and the exit is drawn as a red rectangle.
            - The `self.maze` attribute represents the maze layout, where 0 denotes open paths
              and 1 denotes walls.

        Example:
            If the maze had previously indicated search paths with yellow cells, calling this
            method will clear those indications and reset the maze to its original state with
            white paths, green entrance, and red exit.
        """
        # Clear all yellow cells indicating the search paths
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == 0:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="white",
                    )
        # Redraw the entrance and exit
        self.canvas.create_rectangle(
            0, self.cell_size, self.cell_size, 2 * self.cell_size, fill="green"
        )
        self.canvas.create_rectangle(
            (self.width - 1) * self.cell_size,
            (self.height - 2) * self.cell_size,
            self.width * self.cell_size,
            (self.height - 1) * self.cell_size,
            fill="red",
        )

    def dfs_bot(self):
        """
        Initiates Depth-First Search (DFS) to find a path from the start to the exit in the maze.

        This method serves as the entry point for performing DFS in the maze. It first clears any
        previous search paths from the canvas, then calls the `depth_first_search` method to
        start the search process.

        The search starts from the predefined starting point `(1, 1)` and aims to reach the
        predefined exit point `(self.width - 1, self.height - 2)`. As the search progresses,
        cells are painted to visually indicate the path being explored.

        Notes:
            - The method clears the canvas of previous search paths before initiating DFS.
            - The start and end points are fixed for this implementation.
            - The cells being visited are painted in yellow during the search.

        Example:
            Calling `dfs_bot()` will begin the DFS algorithm, updating the maze visualization
            with the path being explored and eventually finding the path to the exit if it exists.
        """
        self.clear_search_paths()
        start = (1, 1)
        end = (self.width - 1, self.height - 2)
        self.depth_first_search(start, end)

    def depth_first_search(self, start, end):
        """
        Performs Depth-First Search (DFS) to find a path from `start` to `end` in the maze.

        This method performs the DFS algorithm to explore the maze and find a path from the
        `start` position to the `end` position. As the search progresses, each visited cell is
        painted in yellow to indicate the path being explored.

        Parameters:
            start (tuple): The starting position in the maze as (x, y).
            end (tuple): The target position (exit) in the maze as (x, y).

        Process:
            1. Initialize a stack with the starting position and the current path.
            2. Maintain a set of visited positions to avoid revisiting cells.
            3. Use a recursive function `step` to handle the search process:
                - If the stack is not empty, pop the current position and path.
                - Paint the current cell in yellow and update the canvas.
                - If the current position is the end, terminate the search.
                - Otherwise, explore the neighboring cells by adding them to the stack if they
                  are valid and not visited.
                - Schedule the next step in the search process using `root.after`.

        Notes:
            - The recursive `step` function ensures the search progresses by periodically
              updating the canvas and scheduling the next search step.
            - Cells are painted yellow during the search to visually represent the exploration
              process.
            - The search continues until the exit is reached or all possible paths are explored.

        Example:
            If you call `depth_first_search((1, 1), (10, 10))`, the maze will be explored using DFS,
            and the path will be visualized with yellow cells. If a path exists, it will be found
            and displayed.
        """
        stack = [(start, [start])]
        visited = set()

        def step():
            if stack:
                current, path = stack.pop()
                if current in visited:
                    self.root.after(50, step)
                    return
                visited.add(current)

                # Paint the current cell
                self.canvas.create_rectangle(
                    current[0] * self.cell_size,
                    current[1] * self.cell_size,
                    (current[0] + 1) * self.cell_size,
                    (current[1] + 1) * self.cell_size,
                    fill="yellow",
                )
                self.canvas.update()  # Force update the canvas

                if current == end:
                    return  # End the search if the exit is reached

                for direction in MOVE_DIRS.values():
                    next_pos = (current[0] + direction[0], current[1] + direction[1])
                    if (
                        0 <= next_pos[0] < self.width
                        and 0 <= next_pos[1] < self.height
                        and self.maze[next_pos[1]][next_pos[0]] == 0
                        and next_pos not in visited
                    ):
                        stack.append((next_pos, path + [next_pos]))

                self.root.after(50, step)  # Schedule the next step

        step()

    def bfs_bot(self):
        """
        Initiates Breadth-First Search (BFS) to find a path from the start to the exit in the maze.

        This method clears any previous search paths from the canvas and then calls the
        `breadth_first_search` method to begin the BFS process.

        The search starts from the predefined starting point `(1, 1)` and aims to reach
        the predefined exit point `(self.width - 1, self.height - 2)`. As the search progresses,
        cells are painted to visually indicate the path being explored.

        Notes:
            - The method clears the canvas of previous search paths before initiating BFS.
            - The start and end points are fixed for this implementation.
            - The cells being visited are painted in light blue during the search.

        Example:
            Calling `bfs_bot()` will begin the BFS algorithm, updating the maze visualization
            with the path being explored and eventually finding the path to the exit if it exists.
        """
        self.clear_search_paths()
        start = (1, 1)
        end = (self.width - 1, self.height - 2)
        self.breadth_first_search(start, end)

    def breadth_first_search(self, start, end):
        """
        Performs Breadth-First Search (BFS) to find a path from `start` to `end` in the maze.

        This method explores the maze using BFS to find the shortest path from the
        `start` position to the `end` position. Each visited cell is painted in light blue
        to indicate the path being explored.

        Parameters:
            start (tuple): The starting position in the maze as (x, y).
            end (tuple): The target position (exit) in the maze as (x, y).

        Process:
            1. Initialize a queue with the starting position and the current path.
            2. Maintain a set of visited positions to avoid revisiting cells.
            3. Use a loop to process each position in the queue:
                - Paint the current cell in light blue and update the canvas.
                - If the current position is the end, terminate the search.
                - Otherwise, explore the neighboring cells and add them to the queue if they
                  are valid and not visited.
                - Schedule the next step in the search process using `root.after`.

        Notes:
            - The `step` function is used to manage the search process and update the canvas.
            - The search continues until the exit is reached or all possible paths are explored.

        Example:
            Calling `breadth_first_search((1, 1), (10, 10))` will perform BFS on the maze,
            visualizing the path exploration with light blue cells.
        """
        queue = deque([(start, [start])])
        visited = set()

        def step():
            if queue:
                current, path = queue.popleft()
                if current in visited:
                    self.root.after(50, step)
                    return
                visited.add(current)

                # Paint the current cell
                self.canvas.create_rectangle(
                    current[0] * self.cell_size,
                    current[1] * self.cell_size,
                    (current[0] + 1) * self.cell_size,
                    (current[1] + 1) * self.cell_size,
                    fill="light blue",
                )
                self.canvas.update()  # Force update the canvas

                if current == end:
                    return  # End the search if the exit is reached

                for direction in MOVE_DIRS.values():
                    next_pos = (current[0] + direction[0], current[1] + direction[1])
                    if (
                        0 <= next_pos[0] < self.width
                        and 0 <= next_pos[1] < self.height
                        and self.maze[next_pos[1]][next_pos[0]] == 0
                        and next_pos not in visited
                    ):
                        queue.append((next_pos, path + [next_pos]))

                self.root.after(50, step)  # Schedule the next step

        step()

    def dijkstra_bot(self):
        """
        Initiates Dijkstra's Algorithm to find the shortest path from the start to the exit in the maze.

        This method clears any previous search paths from the canvas and then calls the
        `dijkstra_algorithm` method to begin the Dijkstra's search process.

        The search starts from the predefined starting point `(1, 1)` and aims to reach
        the predefined exit point `(self.width - 1, self.height - 2)`. As the search progresses,
        cells are painted to visually indicate the path being explored.

        Notes:
            - The method clears the canvas of previous search paths before initiating Dijkstra's algorithm.
            - The start and end points are fixed for this implementation.
            - The cells being visited are painted in orange during the search.

        Example:
            Calling `dijkstra_bot()` will begin the Dijkstra's algorithm, updating the maze
            visualization with the path being explored and eventually finding the shortest path
            to the exit if it exists.
        """
        self.clear_search_paths()
        start = (1, 1)
        end = (self.width - 1, self.height - 2)
        self.dijkstra_algorithm(start, end)

    def dijkstra_algorithm(self, start, end):
        """
        Performs Dijkstra's Algorithm to find the shortest path from `start` to `end` in the maze.

        This method explores the maze using Dijkstra's algorithm to find the shortest path
        from the `start` position to the `end` position. Each visited cell is painted in orange
        to indicate the path being explored.

        Parameters:
            start (tuple): The starting position in the maze as (x, y).
            end (tuple): The target position (exit) in the maze as (x, y).

        Process:
            1. Initialize a priority queue (heap) with the starting position and initial cost.
            2. Maintain a set of visited positions to avoid revisiting cells.
            3. Use a loop to process each position in the priority queue:
                - Paint the current cell in orange and update the canvas.
                - If the current position is the end, terminate the search.
                - Otherwise, explore the neighboring cells and add them to the queue if they
                  are valid and not visited.
                - Schedule the next step in the search process using `root.after`.

        Notes:
            - The `step` function handles the search process and updates the canvas.
            - The priority queue ensures that the shortest path is found efficiently.

        Example:
            Calling `dijkstra_algorithm((1, 1), (10, 10))` will perform Dijkstra's algorithm on
            the maze, visualizing the path exploration with orange cells.
        """
        heap = [(0, start, [start])]  # (cost, position, path)
        visited = set()

        def step():
            if heap:
                cost, current, path = heapq.heappop(heap)
                if current in visited:
                    self.root.after(50, step)
                    return
                visited.add(current)

                # Paint the current cell
                self.canvas.create_rectangle(
                    current[0] * self.cell_size,
                    current[1] * self.cell_size,
                    (current[0] + 1) * self.cell_size,
                    (current[1] + 1) * self.cell_size,
                    fill="orange",
                )
                self.canvas.update()  # Force update the canvas

                if current == end:
                    return  # End the search if the exit is reached

                for direction in MOVE_DIRS.values():
                    next_pos = (current[0] + direction[0], current[1] + direction[1])
                    if (
                        0 <= next_pos[0] < self.width
                        and 0 <= next_pos[1] < self.height
                        and self.maze[next_pos[1]][next_pos[0]] == 0
                        and next_pos not in visited
                    ):
                        heapq.heappush(
                            heap,
                            (cost + 1, next_pos, path + [next_pos]),
                        )

                self.root.after(50, step)  # Schedule the next step

        step()

    def a_star_bot(self):
        """
        Initiates A* Algorithm to find the shortest path from the start to the exit in the maze.

        This method clears any previous search paths from the canvas and then calls the
        `a_star_algorithm` method to begin the A* search process.

        The search starts from the predefined starting point `(1, 1)` and aims to reach
        the predefined exit point `(self.width - 1, self.height - 2)`. As the search progresses,
        cells are painted to visually indicate the path being explored.

        Notes:
            - The method clears the canvas of previous search paths before initiating A* algorithm.
            - The start and end points are fixed for this implementation.
            - The cells being visited are painted in purple during the search.

        Example:
            Calling `a_star_bot()` will begin the A* algorithm, updating the maze visualization
            with the path being explored and eventually finding the shortest path to the exit if it exists.
        """
        self.clear_search_paths()
        start = (1, 1)
        end = (self.width - 1, self.height - 2)
        self.a_star_algorithm(start, end)

    def heuristic(self, a, b):
        """
        Computes the heuristic (Manhattan distance) between two points `a` and `b`.

        Parameters:
            a (tuple): The first point as (x, y).
            b (tuple): The second point as (x, y).

        Returns:
            int: The Manhattan distance between points `a` and `b`.

        Notes:
            - The heuristic used is the Manhattan distance, which is suitable for grid-based pathfinding.

        Example:
            Calling `heuristic((1, 1), (4, 5))` returns 7, which is the Manhattan distance between the two points.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star_algorithm(self, start, end):
        """
        Performs A* Algorithm to find the shortest path from `start` to `end` in the maze.

        This method explores the maze using A* algorithm to find the shortest path from the
        `start` position to the `end` position. Each visited cell is painted in purple to
        indicate the path being explored.

        Parameters:
            start (tuple): The starting position in the maze as (x, y).
            end (tuple): The target position (exit) in the maze as (x, y).

        Process:
            1. Initialize a priority queue (heap) with the starting position, initial cost,
               and heuristic estimate.
            2. Maintain a set of visited positions to avoid revisiting cells.
            3. Use a loop to process each position in the priority queue:
                - Paint the current cell in purple and update the canvas.
                - If the current position is the end, terminate the search.
                - Otherwise, explore the neighboring cells and add them to the queue if they
                  are valid and not visited.
                - Schedule the next step in the search process using `root.after`.

        Notes:
            - The heuristic used in A* is the Manhattan distance.
            - The priority queue ensures that the algorithm efficiently finds the shortest path.

        Example:
            Calling `a_star_algorithm((1, 1), (10, 10))` will perform A* algorithm on the maze,
            visualizing the path exploration with purple cells.
        """
        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(start, end), 0, start, [start]))
        visited = set()

        def step():
            if open_set:
                _, cost, current, path = heapq.heappop(open_set)
                if current in visited:
                    self.root.after(50, step)
                    return
                visited.add(current)

                # Paint the current cell
                self.canvas.create_rectangle(
                    current[0] * self.cell_size,
                    current[1] * self.cell_size,
                    (current[0] + 1) * self.cell_size,
                    (current[1] + 1) * self.cell_size,
                    fill="purple",
                )
                self.canvas.update()  # Force update the canvas

                if current == end:
                    return  # End the search if the exit is reached

                for direction in MOVE_DIRS.values():
                    next_pos = (current[0] + direction[0], current[1] + direction[1])
                    if (
                        0 <= next_pos[0] < self.width
                        and 0 <= next_pos[1] < self.height
                        and self.maze[next_pos[1]][next_pos[0]] == 0
                        and next_pos not in visited
                    ):
                        heapq.heappush(
                            open_set,
                            (
                                cost + 1 + self.heuristic(next_pos, end),
                                cost + 1,
                                next_pos,
                                path + [next_pos],
                            ),
                        )

                self.root.after(50, step)  # Schedule the next step

        step()


# Run the Maze Game
MazeGame(WIDTH, HEIGHT, CELL_SIZE)
