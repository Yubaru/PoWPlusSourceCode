# ==============================================================================
# TIC-TAC-TOE FOR REN'PY 8
# ==============================================================================

# 1. PYTHON LOGIC BLOCK
# We use 'init python' to define our game logic class and AI before the game starts.
init python:
    import random

    class TicTacToeGame(object):
        def __init__(self):
            # Board is a list of 9 items: None, 'X', or 'O'
            self.board = [None] * 9
            self.turn = 'X'
            self.winner = None
            self.game_over = False
            self.mode = 'PvP' # 'PvP' or 'PvC'
            self.difficulty = 'Hard' # 'Easy', 'Medium', 'Hard'
            self.ai_player = 'O' # AI is always O in this setup
            self.status_text = "Player X's Turn"

        def reset(self):
            self.board = [None] * 9
            self.turn = 'X'
            self.winner = None
            self.game_over = False
            self.status_text = "Player X's Turn"
            renpy.restart_interaction()

        def set_mode(self, mode, difficulty='Hard'):
            self.mode = mode
            self.difficulty = difficulty
            self.reset()

        def check_winner(self, board=None):
            # If no board provided, check actual game board
            if board is None:
                board = self.board

            # Winning combinations indices
            lines = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
                (0, 4, 8), (2, 4, 6)             # Diagonals
            ]

            for a, b, c in lines:
                if board[a] and board[a] == board[b] == board[c]:
                    return board[a]

            if None not in board:
                return "Draw"

            return None

        def make_move(self, index):
            # Prevent move if game over or cell occupied
            if self.board[index] is not None or self.game_over:
                return

            # Apply move
            self.board[index] = self.turn
            
            # Check for result
            res = self.check_winner()
            if res:
                self.game_over = True
                self.winner = res
                if res == "Draw":
                    self.status_text = "It's a Draw!"
                else:
                    self.status_text = f"Player {res} Wins!"
                
                # Play sound if you have one, otherwise ignore
                # renpy.play("audio/win.ogg") 
            else:
                # Switch turn
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.status_text = f"Player {self.turn}'s Turn"

                # Trigger AI if mode is PvC and it's O's turn
                if self.mode == 'PvC' and self.turn == self.ai_player and not self.game_over:
                    self.ai_move()

            renpy.restart_interaction()

        def ai_move(self):
            # Determine if AI should make a random move (blunder) based on difficulty
            make_random_move = False
            
            if self.difficulty == 'Easy':
                # Easy: Always plays randomly
                make_random_move = True
            elif self.difficulty == 'Medium':
                # Medium: 50% chance to play randomly
                if random.random() < 0.5:
                    make_random_move = True
            elif self.difficulty == 'Hard':
                # Hard: 10% chance to play randomly (Making it beatable, but tough)
                if random.random() < 0.1:
                    make_random_move = True

            # Get list of empty spots
            empty_spots = [i for i, x in enumerate(self.board) if x is None]
            
            if not empty_spots:
                return

            best_move = None

            # Logic: If we are blundering (random) OR if we decide to play optimally
            if make_random_move:
                best_move = random.choice(empty_spots)
            else:
                # Find the optimal move using Minimax
                best_score = -float('inf')
                
                for i in empty_spots:
                    self.board[i] = self.ai_player
                    score = self.minimax(self.board, 0, False)
                    self.board[i] = None # Undo move
                    
                    if score > best_score:
                        best_score = score
                        best_move = i
            
            if best_move is not None:
                self.make_move(best_move)

        def minimax(self, board, depth, is_maximizing):
            result = self.check_winner(board)
            if result == self.ai_player:
                return 10 - depth
            elif result == 'X': # Assuming Player is X
                return depth - 10
            elif result == "Draw":
                return 0

            if is_maximizing:
                best_score = -float('inf')
                for i in range(9):
                    if board[i] is None:
                        board[i] = self.ai_player
                        score = self.minimax(board, depth + 1, False)
                        board[i] = None
                        best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                for i in range(9):
                    if board[i] is None:
                        board[i] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i] = None
                        best_score = min(score, best_score)
                return best_score

# Initialize the game variable
default ttt = TicTacToeGame()


# 2. STYLES
# Define some styles to make it look nice without images
style ttt_button:
    xsize 150
    ysize 150
    background Frame(Solid("#444"), 0, 0)
    hover_background Frame(Solid("#666"), 0, 0)
    padding (10, 10)

style ttt_button_text:
    size 80
    color "#FFF"
    align (0.5, 0.5)
    outlines [(2, "#000", 0, 0)]

style ttt_label_text:
    size 40
    color "#FFF"
    outlines [(2, "#000", 0, 0)]


# 3. SCREENS
screen tictactoe_game():
    modal True
    tag menu

    # Background
    add Solid("#222")

    vbox:
        align (0.5, 0.5)
        spacing 20

        # Title / Status
        text ttt.status_text:
            style "ttt_label_text"
            xalign 0.5

        # The Grid
        frame:
            background Solid("#333")
            padding (10, 10)
            xalign 0.5
            
            grid 3 3:
                spacing 10
                
                for i in range(9):
                    button:
                        style "ttt_button"
                        action Function(ttt.make_move, i)
                        
                        # Display X, O, or nothing
                        if ttt.board[i] == 'X':
                            text "X" style "ttt_button_text" color "#f00"
                        elif ttt.board[i] == 'O':
                            text "O" style "ttt_button_text" color "#00f"
                        else:
                            text ""

        # Control Buttons
        hbox:
            xalign 0.5
            spacing 50
            
            textbutton "Reset Game":
                action Function(ttt.reset)
                text_size 30
                text_color "#FFF"
                text_hover_color "#FFD700"
            
            textbutton "Quit to Menu":
                action Return()
                text_size 30
                text_color "#FFF"
                text_hover_color "#F00"


screen tictactoe_menu():
    tag menu
    add Solid("#111")
    
    vbox:
        align (0.5, 0.5)
        spacing 30
        
        text "TIC - TAC - TOE":
            size 80
            xalign 0.5
            color "#FFF"
            outlines [(4, "#000", 0, 0)]
        
        # Spacer
        null height 10

        text "Player vs Computer":
            size 40
            xalign 0.5
            color "#AAA"

        hbox:
            xalign 0.5
            spacing 20
            
            textbutton "Easy":
                action [Function(ttt.set_mode, 'PvC', 'Easy'), Call("play_ttt")]
                text_size 30
                text_color "#8F8"
                text_hover_color "#FFF"

            textbutton "Medium":
                action [Function(ttt.set_mode, 'PvC', 'Medium'), Call("play_ttt")]
                text_size 30
                text_color "#FF8"
                text_hover_color "#FFF"

            textbutton "Hard":
                action [Function(ttt.set_mode, 'PvC', 'Hard'), Call("play_ttt")]
                text_size 30
                text_color "#F88"
                text_hover_color "#FFF"
            
        null height 10
        
        textbutton "Player vs Player (Hotseat)":
            action [Function(ttt.set_mode, 'PvP'), Call("play_ttt")]
            xalign 0.5
            text_size 40
            text_idle_color "#AAA"
            text_hover_color "#FFF"

        textbutton "Exit":
            action Quit(confirm=False)
            xalign 0.5
            text_size 30


# 4. REN'PY LABELS
label ticstart:
    # Jump straight to our custom menu
    call screen tictactoe_menu
    return

label play_ttt:
    # Show the game screen. 
    # Because the screen is 'modal', it pauses script execution until Return() is called.
    call screen tictactoe_game
    
    # When they click "Quit", we loop back to the menu
    call screen tictactoe_menu
    return