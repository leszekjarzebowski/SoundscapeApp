from pathlib import Path
import pathspec


def load_gitignore(directory):
    """Wczytuje wzorce z .gitignore i zwraca obiekt pathspec."""
    gitignore_path = Path(directory) / ".gitignore"
    if gitignore_path.exists():
        with open(gitignore_path, "r", encoding="utf-8") as f:
            gitignore_content = f.read()
        return pathspec.PathSpec.from_lines(
            "gitwildmatch", gitignore_content.splitlines()
        )
    return pathspec.PathSpec.from_lines("gitwildmatch", [])


def generate_tree(
    directory, indent="", prefix="├── ", output_lines=None, gitignore=None
):
    """Generuje tekstową strukturę drzewa, pomijając pliki/foldery z .gitignore oraz Git."""
    if output_lines is None:
        output_lines = []

    path = Path(directory)
    if gitignore is None:
        gitignore = load_gitignore(path)

    # Dodatkowe wzorce do pominięcia (Git-related)
    git_exclusions = pathspec.PathSpec.from_lines(
        "gitwildmatch", [".git/", ".gitignore"]
    )
    combined_gitignore = gitignore + git_exclusions

    items = []
    for item in path.iterdir():
        relative_path = str(item.relative_to(path.parent))
        # Pomijaj, jeśli pasuje do .gitignore lub dodatkowych wzorców Git
        if not combined_gitignore.match_file(relative_path):
            items.append(item)

    items = sorted(items, key=lambda x: (x.is_file(), x.name.lower()))

    for index, item in enumerate(items):
        if index == len(items) - 1:
            prefix = "└── "
            next_indent = indent + "    "
        else:
            prefix = "├── "
            next_indent = indent + "│   "

        if item.is_dir():
            output_lines.append(f"{indent}{prefix}{item.name}/")
            generate_tree(
                item,
                next_indent,
                output_lines=output_lines,
                gitignore=combined_gitignore,
            )
        else:
            output_lines.append(f"{indent}{prefix}{item.name}")

    return output_lines


# Ustawienie project_root na katalog, w którym znajduje się skrypt
project_root = Path(__file__).parent
lines = [f"{project_root.name}/"] + generate_tree(project_root)

# Zapisz do pliku
with open("project_structure.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# Opcjonalnie: wydrukuj do konsoli
print("\n".join(lines))

print("Struktura zapisana do project_structure.txt")
