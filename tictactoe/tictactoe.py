from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint
import random

console = Console()

# ─── Board ───────────────────────────────────────────────
def create_board():
    return [" "] * 9

def print_board(board):
    symbols = {"X": "[bold red]X[/bold red]", "O": "[bold blue]O[/bold blue]", " ": "[dim]·[/dim]"}
    b = [symbols.get(cell, cell) for cell in board]
    console.print(f"\n  {b[0]} │ {b[1]} │ {b[2]}    (1│2│3)")
    console.print("  ──┼───┼──")
    console.print(f"  {b[3]} │ {b[4]} │ {b[5]}    (4│5│6)")
    console.print("  ──┼───┼──")
    console.print(f"  {b[6]} │ {b[7]} │ {b[8]}    (7│8│9)\n")

def check_winner(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def is_draw(board):
    return " " not in board

def get_empty(board):
    return [i for i, x in enumerate(board) if x == " "]

# ─── Minimax with Alpha-Beta Pruning ─────────────────────
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"): return 10 - depth
    if check_winner(board, "X"): return depth - 10
    if is_draw(board): return 0

    if is_maximizing:
        best = -1000
        for i in get_empty(board):
            board[i] = "O"
            val = minimax(board, depth+1, False, alpha, beta)
            board[i] = " "
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = 1000
        for i in get_empty(board):
            board[i] = "X"
            val = minimax(board, depth+1, True, alpha, beta)
            board[i] = " "
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break
        return best

def ai_move(board, difficulty):
    empty = get_empty(board)
    if difficulty == "easy":
        return random.choice(empty)
    elif difficulty == "medium":
        # 60% chance of smart move
        if random.random() < 0.6:
            return best_minimax_move(board)
        return random.choice(empty)
    else:  # hard
        return best_minimax_move(board)

def best_minimax_move(board):
    best_val, best_move = -1000, None
    for i in get_empty(board):
        board[i] = "O"
        val = minimax(board, 0, False, -1000, 1000)
        board[i] = " "
        if val > best_val:
            best_val, best_move = val, i
    return best_move

# ─── Game Loop ────────────────────────────────────────────
def play_game(difficulty, score):
    board = create_board()
    console.print(f"\n[bold cyan]New Game — Difficulty: {difficulty.upper()}[/bold cyan]")
    console.print("[dim]You are X, AI is O. Enter position 1-9[/dim]")
    print_board(board)

    while True:
        # Human turn
        while True:
            try:
                move = int(console.input("[bold green]Your move (1-9): [/bold green]")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                console.print("[red]Invalid! Pick an empty cell 1-9[/red]")
            except ValueError:
                console.print("[red]Enter a number![/red]")

        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            console.print("[bold green]🎉 You Win![/bold green]")
            score["wins"] += 1
            break
        if is_draw(board):
            console.print("[yellow]🤝 It's a Draw![/yellow]")
            score["draws"] += 1
            break

        # AI turn
        console.print("[dim]AI is thinking...[/dim]")
        ai = ai_move(board, difficulty)
        board[ai] = "O"
        console.print(f"[bold blue]AI played position {ai+1}[/bold blue]")
        print_board(board)

        if check_winner(board, "O"):
            console.print("[bold red]💀 AI Wins! Better luck next time.[/bold red]")
            score["losses"] += 1
            break
        if is_draw(board):
            console.print("[yellow]🤝 It's a Draw![/yellow]")
            score["draws"] += 1
            break

def show_scoreboard(score):
    table = Table(title="📊 Scoreboard", border_style="cyan")
    table.add_column("Result", style="bold")
    table.add_column("Count", justify="center")
    table.add_row("[green]Wins[/green]", str(score["wins"]))
    table.add_row("[red]Losses[/red]", str(score["losses"]))
    table.add_row("[yellow]Draws[/yellow]", str(score["draws"]))
    total = sum(score.values())
    wr = (score["wins"]/total*100) if total else 0
    table.add_row("[cyan]Win Rate[/cyan]", f"{wr:.1f}%")
    console.print(table)

def main():
    console.print(Panel.fit(
        "[bold magenta]♟️  Tic-Tac-Toe — AI Edition[/bold magenta]\n"
        "[dim]Powered by Minimax + Alpha-Beta Pruning[/dim]",
        border_style="magenta"
    ))

    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = console.input("\nChoose difficulty [easy/medium/hard]: ").strip().lower()

    score = {"wins": 0, "losses": 0, "draws": 0}

    while True:
        play_game(difficulty, score)
        show_scoreboard(score)
        again = console.input("\n[bold]Play again? (y/n): [/bold]").strip().lower()
        if again != "y":
            console.print("[cyan]Thanks for playing! GG 🎮[/cyan]")
            break

if __name__ == "__main__":
    main()