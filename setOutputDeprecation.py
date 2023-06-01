import argparse
import os.path
import re


def file_path(path: str) -> str:
    """
    Custom argument type for file paths.

    Args:
        path (str): The file path to validate.

    Returns:
        str: The validated file path.

    Raises:
        argparse.ArgumentTypeError: If the path is not a valid file.
    """
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid file path")

    return path


def replace_output_line(line: str) -> str:
    """
    Replaces the output line format if it matches the pattern.

    Args:
        line (str): The input line to check and modify.

    Returns:
        str: The modified line if it matches the pattern, otherwise the original line.
    """

    match = re.match(r'(.*?)echo "::set-output name=(.*?)::(.*?)"\s*\t*\n', line)
    if not match:
        return line

    return f'{match.group(1)}echo "{match.group(2)}={match.group(3)}" >> $GITHUB_OUTPUT\n'


def main(args):
    """
    Main entry point of the script.
    """
    print(f"[🍌] Executing for {args.path}")
    with open(args.path, "r") as file:
        lines = file.readlines()

    replaced_lines: list[str] = list(map(replace_output_line, lines))

    if not args.dry:
        with open(args.path, "w") as file:
            file.writelines(replaced_lines)

    applied_changes: bool = False
    for source, target in zip(lines, replaced_lines):
        if source != target:
            print(f"[♻️] Changed\n\t{source[:-1].strip()}\n\t{target[:-1].strip()}")
            applied_changes = True

    if args.backup and applied_changes:
        print(f"[🦺] Created a copy of {args.path}")
        with open(args.path + ".bak", "w") as backup_file:
            backup_file.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "A lazy program to change ::set-output to the current convention"
    )
    parser.add_argument(
        "-p", "--path", type=file_path, required=True, help="File to change"
    )
    parser.add_argument(
        "-d",
        "--dry",
        type=bool,
        required=False,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Don't apply changes",
    )
    parser.add_argument(
        "-b",
        "--backup",
        type=bool,
        required=False,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Create a .bak with the original contents",
    )
    main(parser.parse_args())
