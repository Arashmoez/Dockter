import json
import shlex

from .ui import print_success


def ask(prompt, default=None):
    if default is not None and default != "":
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default

    return input(f"{prompt}: ").strip()


def ask_yes_no(prompt, default="y"):
    suffix = "Y/n" if default.lower() == "y" else "y/N"
    value = input(f"{prompt} [{suffix}]: ").strip().lower()

    if not value:
        value = default.lower()

    return value in ("y", "yes")


def ask_int(prompt, default=None):
    while True:
        value = ask(prompt, str(default) if default is not None else None)

        if value == "":
            return default

        if value.isdigit():
            return int(value)

        print("❌ Please enter a valid number.")


def save_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content.strip() + "\n")

    print_success(f"Saved to {filename}")


def make_exec_cmd(command):
    parts = shlex.split(command)
    return f"CMD {json.dumps(parts)}"
