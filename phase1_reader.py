import os
from collections import Counter

# Specify the path of the command history
history_file = os.path.expanduser("~/.bash_history")

# If the file exists, read and analyze it
if os.path.exists(history_file):
    with open(history_file) as f:
        commands = [line.strip() for line in f if line.strip()]
    stats = Counter(commands)
    print("\n📊 Top 5 commands you use most:")
    for cmd, freq in stats.most_common(5):
        print(f"{cmd} → {freq} times")
else:
    print("⚠️ No history file found. Try typing some commands in the terminal first.")
