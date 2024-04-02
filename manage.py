import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py <app_name> <command> [args]")
        sys.exit(1)

    # Extract the app name and command from the arguments
    app_name, command = sys.argv[1], sys.argv[2]
    additional_args = sys.argv[3:]

    # Assuming the main script is always named 'main.py' in each app folder
    script_path = f"{app_name}/main.py"
    full_command = ["python", script_path, command]
    if additional_args:
        full_command.extend(additional_args)

    subprocess.run(full_command)


if __name__ == "__main__":
    main()
