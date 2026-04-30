from .ui import print_header, print_error
from .utils import ask
from .dockerfile_generator import (
    generate_python_dockerfile,
    generate_django_dockerfile,
    generate_node_dockerfile,
    generate_php_dockerfile,
    generate_static_dockerfile,
    generate_custom_dockerfile,
)


def main():
    while True:
        print_header()

        print("What kind of Dockerfile do you want to generate?\n")
        print("1. 🐍 Python")
        print("2. 🌐 Django")
        print("3. 🟢 Node.js")
        print("4. 🐘 PHP")
        print("5. 📄 Static HTML / Nginx")
        print("6. 🛠️ Custom")
        print("7. 🚪 Exit")

        choice = ask("\nChoose an option", "1")

        if choice == "1":
            generate_python_dockerfile()
            break

        elif choice == "2":
            generate_django_dockerfile()
            break

        elif choice == "3":
            generate_node_dockerfile()
            break

        elif choice == "4":
            generate_php_dockerfile()
            break

        elif choice == "5":
            generate_static_dockerfile()
            break

        elif choice == "6":
            generate_custom_dockerfile()
            break

        elif choice == "7":
            print("\n👋 Goodbye!")
            break

        else:
            print_error("Invalid option. Please choose a number from 1 to 7.")
            print()
