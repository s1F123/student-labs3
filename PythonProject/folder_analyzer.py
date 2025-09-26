import os
from collections import Counter


def analyze_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Указанная папка не существует.")
        return

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    extensions = [
        os.path.splitext(f)[1].lower() or 'без расширения'
        for f in files
    ]

    print(f"Всего файлов: {len(files)}")
    print("\nРаспределение по расширениям:")
    for ext, count in Counter(extensions).most_common():
        print(f"  {ext}: {count}")


if __name__ == "__main__":
    path = input("Введите путь к папке: ").strip()
    analyze_folder(path)
