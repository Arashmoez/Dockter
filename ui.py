def print_header(header="🐳 dockter — Dockerfile & Compose Wizard"):
    print("\n" + "=" * 55)
    print(header)
    print("=" * 55)


def print_section(title):
    print(f"\n📦 {title}")
    print("-" * 55)


def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_generated_file(filename, content):
    print(f"\n📝 Generated {filename}:")
    print("-" * 55)
    print(content)
    print("-" * 55)
