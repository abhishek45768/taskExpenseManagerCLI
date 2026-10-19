import models as model
import services.services as service
def main():
    while True:
        print("\nExpense Manager")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Search expenses")
        print("6. Summary")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            title: str = input("Enter expense title: ")
            amount: float = float(input("Enter expense amount: "))
            category: str = input("Enter expense category: ")
            result = service.add_expense(title, amount, category)
            print(result)
        elif choice == "2":
            result=service.List_expenses()
            print("List expenses:")
            for expense in result:
                print(f"-id {expense['id']}: {expense['title']}: ${expense['amount']}")
        elif choice == "3":

            print("What is the id of the expense you want to update?")
            id = int(input("Enter the id: "))
            if id <= 0:
                print("Invalid id. Please enter a positive integer.")
                continue
            else:
                print("Enter the new details for the expense:")
                title = input("Enter title: ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                result = service.update_expense(id, title, amount, category)
                print(result)
        elif choice == "4":
            print("What is the id of the expense you want to delete?")
            id = int(input("Enter the id: "))
            if id <= 0:
                print("Invalid id. Please enter a positive integer.")
                continue
            else:
                result = service.delete_expense(id)
                print(result)
        elif choice == "5":
            print("Search expenses")
            keyword = input("Enter search keyword: ")
            result = service.search_expenses(keyword)
            print("Matching expenses:")
            for expense in result:
                print(f"- {expense['title']}: ${expense['amount']} ({expense['category']})")
        elif choice == "6":
            print("Show summary")
            result = service.summarize_expenses()
            print(f"Total amount: ${result['total_amount']}")
            print("Category summary:")
            for category, amount in result['category_summary'].items():
                print(f"- {category}: ${amount}")
        elif choice == "7":
            service.exit_program()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()