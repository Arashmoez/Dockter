from textwrap import dedent

from .ui import print_section, print_error, print_generated_file
from .utils import ask, ask_yes_no, save_file, make_exec_cmd


def generate_python_dockerfile(return_content=False):
    print_section("Python Dockerfile Generator 🐍")

    python_version = ask("Python version", "3.12-slim")
    workdir = ask("Working directory", "/app")
    requirements_file = ask("Requirements file", "requirements.txt")
    port = ask("Expose port? Leave empty for none", "8000")
    start_command = ask("Start command", "python app.py")

    cmd_instruction = make_exec_cmd(start_command)

    content = dedent(f"""
        FROM python:{python_version}

        ENV PYTHONDONTWRITEBYTECODE=1
        ENV PYTHONUNBUFFERED=1

        WORKDIR {workdir}

        COPY {requirements_file} .
        RUN pip install --no-cache-dir -r {requirements_file}

        COPY . .
    """)

    if port:
        content += f"\nEXPOSE {port}\n"

    content += f"\n{cmd_instruction}\n"

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def generate_django_dockerfile(return_content=False):
    print_section("Django Dockerfile Generator 🌿")

    python_version = ask("Python version", "3.12-slim")
    workdir = ask("Working directory", "/app")
    requirements_file = ask("Requirements file", "requirements.txt")
    project_module = ask("Django project module name, example: config", "config")
    port = ask("Expose port", "8000")

    use_gunicorn = ask_yes_no("Use Gunicorn instead of Django dev server?", "y")
    run_collectstatic = ask_yes_no("Add collectstatic step to startup command?", "n")

    if use_gunicorn:
        start_command = f"gunicorn {project_module}.wsgi:application --bind 0.0.0.0:{port}"
    else:
        start_command = f"python manage.py runserver 0.0.0.0:{port}"

    if run_collectstatic:
        if use_gunicorn:
            start_command = (
                f'sh -c "python manage.py collectstatic --noinput && '
                f'gunicorn {project_module}.wsgi:application --bind 0.0.0.0:{port}"'
            )
        else:
            start_command = (
                f'sh -c "python manage.py collectstatic --noinput && '
                f'python manage.py runserver 0.0.0.0:{port}"'
            )

    cmd_instruction = make_exec_cmd(start_command)

    content = dedent(f"""
        FROM python:{python_version}

        ENV PYTHONDONTWRITEBYTECODE=1
        ENV PYTHONUNBUFFERED=1

        WORKDIR {workdir}

        COPY {requirements_file} .
        RUN pip install --no-cache-dir -r {requirements_file}

        COPY . .

        EXPOSE {port}

        {cmd_instruction}
    """)

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def generate_node_dockerfile(return_content=False):
    print_section("Node.js Dockerfile Generator 🟢")

    node_version = ask("Node.js version", "20-alpine")
    workdir = ask("Working directory", "/app")
    package_manager = ask("Package manager npm/yarn/pnpm", "npm").lower()
    port = ask("Expose port? Leave empty for none", "3000")
    start_command = ask("Start command", "npm start")

    if package_manager == "yarn":
        install_cmd = "RUN yarn install"
    elif package_manager == "pnpm":
        install_cmd = "RUN npm install -g pnpm && pnpm install"
    else:
        install_cmd = "RUN npm install"

    cmd_instruction = make_exec_cmd(start_command)

    content = dedent(f"""
        FROM node:{node_version}

        WORKDIR {workdir}

        COPY package*.json ./
        {install_cmd}

        COPY . .
    """)

    if port:
        content += f"\nEXPOSE {port}\n"

    content += f"\n{cmd_instruction}\n"

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def generate_php_dockerfile(return_content=False):
    print_section("PHP Dockerfile Generator 🐘")

    php_version = ask("PHP version", "8.2-apache")
    workdir = ask("Working directory", "/var/www/html")
    port = ask("Expose port", "80")

    content = dedent(f"""
        FROM php:{php_version}

        WORKDIR {workdir}

        COPY . .

        EXPOSE {port}
    """)

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def generate_static_dockerfile(return_content=False):
    print_section("Static HTML Dockerfile Generator 🌐")

    nginx_version = ask("Nginx version", "alpine")
    html_source = ask("HTML source directory", ".")
    port = ask("Expose port", "80")

    content = dedent(f"""
        FROM nginx:{nginx_version}

        COPY {html_source} /usr/share/nginx/html

        EXPOSE {port}
    """)

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def generate_custom_dockerfile(return_content=False):
    print_section("Custom Dockerfile Generator 🛠️")

    base_image = ask("Base image", "ubuntu:22.04")
    workdir = ask("Working directory", "/app")
    copy_all = ask_yes_no("Copy current directory into image?", "y")
    run_command = ask("RUN command, leave empty for none", "")
    port = ask("Expose port? Leave empty for none", "")
    start_command = ask("Start command", "bash")

    cmd_instruction = make_exec_cmd(start_command)

    content = dedent(f"""
        FROM {base_image}

        WORKDIR {workdir}
    """)

    if copy_all:
        content += "\nCOPY . .\n"

    if run_command:
        content += f"\nRUN {run_command}\n"

    if port:
        content += f"\nEXPOSE {port}\n"

    content += f"\n{cmd_instruction}\n"

    if return_content:
        return content.strip()

    save_file("Dockerfile", content)
    print_generated_file("Dockerfile", content)


def dockerfile_menu(return_content=False):
    while True:
        print_section("Dockerfile Presets 🐳")
        print("1️⃣  Python")
        print("2️⃣  Django")
        print("3️⃣  Node.js")
        print("4️⃣  PHP")
        print("5️⃣  Static HTML")
        print("6️⃣  Custom")
        print("7️⃣  Back")

        choice = ask("Choose an option")

        if choice == "1":
            return generate_python_dockerfile(return_content=return_content)
        elif choice == "2":
            return generate_django_dockerfile(return_content=return_content)
        elif choice == "3":
            return generate_node_dockerfile(return_content=return_content)
        elif choice == "4":
            return generate_php_dockerfile(return_content=return_content)
        elif choice == "5":
            return generate_static_dockerfile(return_content=return_content)
        elif choice == "6":
            return generate_custom_dockerfile(return_content=return_content)
        elif choice == "7":
            return None
        else:
            print_error("Invalid choice. Try again.")
