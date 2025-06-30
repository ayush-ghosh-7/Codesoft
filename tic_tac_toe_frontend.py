import pygame
import sys
from tic_tac_toe_backend import TicTacToe, AIPlayer, HumanPlayer

# Constants
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

class TicTacToeGUI:
    def __init__(self):
        # Initialize game state
        self.game = TicTacToe()
        self.ai_player = AIPlayer('O')
        self.human_player = HumanPlayer('X')
        
        # Initialize GUI state
        self.running = True
        self.game_over = False
        self.message = ""
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        self.font = pygame.font.SysFont('Arial', 40)
        self.small_font = pygame.font.SysFont('Arial', 30)
        self.clock = pygame.time.Clock()
    
    def draw_lines(self):
        # Horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        # Vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)
    
    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                index = row * BOARD_COLS + col
                if self.game.board[index] == 'X':
                    # Draw X
                    pygame.draw.line(self.screen, CROSS_COLOR, 
                                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                    CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                    CROSS_WIDTH)
                elif self.game.board[index] == 'O':
                    # Draw O
                    pygame.draw.circle(self.screen, CIRCLE_COLOR,
                                     (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                     CIRCLE_RADIUS, LINE_WIDTH)
    
    def draw_status(self):
        if not self.game_over:
            status_text = "Your turn (X)" if not self.game.current_winner else f"{self.game.current_winner} wins!"
        else:
            status_text = self.message
            
        text_surface = self.font.render(status_text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT - 50))
        self.screen.blit(text_surface, text_rect)
        
        # Add restart button
        restart_text = self.small_font.render("Press R to restart", True, TEXT_COLOR)
        restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT - 20))
        self.screen.blit(restart_text, restart_rect)
    
    def make_move(self, row, col):
        square = row * BOARD_COLS + col
        if square in self.game.available_moves() and not self.game_over:
            # Human move
            self.game.make_move(square, 'X')
            
            # Check if game is over
            if self.game.current_winner or not self.game.empty_squares():
                self.game_over = True
                self.message = "You win!" if self.game.current_winner == 'X' else "It's a tie!"
                return
            
            # AI move
            ai_square = self.ai_player.get_move(self.game)
            self.game.make_move(ai_square, 'O')
            
            # Check if game is over after AI move
            if self.game.current_winner or not self.game.empty_squares():
                self.game_over = True
                self.message = "AI wins!" if self.game.current_winner == 'O' else "It's a tie!"
    
    def restart_game(self):
        self.game = TicTacToe()
        self.game_over = False
        self.message = ""
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart_game()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouseX, mouseY = event.pos
                
                if mouseY < HEIGHT - 100:  # Only register clicks on the board
                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE
                    
                    self.make_move(clicked_row, clicked_col)
    
    def run(self):
        self.draw_lines()
        
        while self.running:
            self.handle_events()
            
            self.screen.fill(BG_COLOR)
            self.draw_lines()
            self.draw_figures()
            self.draw_status()
            
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game_gui = TicTacToeGUI()
    game_gui.run()