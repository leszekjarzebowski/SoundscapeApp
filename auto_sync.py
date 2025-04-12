from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

SOURCE_DIR = r"V:\python\SoundscapeApp"
TARGET_DIR = r"C:\Users\lesze\OneDrive\Programowanie\python\SoundscapeApp"


class SyncHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"[ZMIANA] {event.src_path} → synchronizacja...")
        subprocess.run(
            [
                "robocopy",
                SOURCE_DIR,
                TARGET_DIR,
                "/E",
                "/XD",
                ".git",
                ".venv",
                "__pycache__",
                "exports",
                "/XF",
                "*.pyc",
                "*.pyo",
                "*.db",
                "/MIR",
            ],
            shell=True,
        )
        print("✅ Synchronizacja zakończona.")


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(SyncHandler(), path=SOURCE_DIR, recursive=True)
    print("👀 Obserwuję zmiany w kodzie... [Ctrl+C, aby zakończyć]")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
