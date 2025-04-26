from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from bank_operator.bank_operator import *

console = Console()


def menu():
    while True:
        console.clear()

        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")

        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "List Accounts")
        table.add_row("5", "Deposit")
        table.add_row("6", "Withdraw")
        table.add_row("7", "View Transactions")
        table.add_row("8", "Exit")

        console.print(table)

        choice = Prompt.ask("👉 Choose option", choices=[str(i) for i in range(1, 9)], default="8")

        if choice == '1':
            create_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            create_account()
        elif choice == '4':
            list_accounts()
        elif choice == '5':
            deposit_money()
        elif choice == '6':
            withdraw_money()
        elif choice == '7':
            view_transactions()
        elif choice == '8':
            console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
            break


if __name__ == "__main__":
    menu()
