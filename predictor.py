import os
from collections import Counter, defaultdict

# نبحث عن ملف السجل
bash_history = os.path.expanduser("~/.bash_history")
predictive_history = os.path.expanduser("~/.predictive_history")

# نحدد أي ملف نستخدم
if os.path.exists(predictive_history):
    history_file = predictive_history
elif os.path.exists(bash_history):
    history_file = bash_history
else:
    history_file = None

# لو مفيش أي history، نبدأ من الصفر برسالة ترحيب
if not history_file:
    print("👋 Welcome to Predictive Command OS!")
    print("It looks like this is your first time using me 😊")
    first_cmd = input("What would you like to do today? ")

    # ننشئ ملف predictive_history ونسجّل أول أمر
    with open(predictive_history, "w") as f:
        f.write(first_cmd + "\n")

    print(f"✅ Got it! I'll remember '{first_cmd}' as your first command.")
    exit()

# لو في ملف history، نقرأه
with open(history_file) as f:
    commands = [line.strip() for line in f if line.strip()]

# تحليل تكرار الأوامر
stats = Counter(commands)
print("\n📊 Top 5 commands you use most:")
for cmd, freq in stats.most_common(5):
    print(f"{cmd} → {freq} times")

# تحليل العلاقات بين الأوامر (Markov-like)
transitions = defaultdict(Counter)
for i in range(len(commands) - 1):
    current = commands[i]
    nxt = commands[i + 1]
    transitions[current][nxt] += 1

last_cmd = commands[-1]

# التنبؤ بالأمر القادم
if last_cmd in transitions:
    print(f"\n🤔 Based on your last command ('{last_cmd}'), you might use:")
    for cmd, count in transitions[last_cmd].most_common(3):
        print(f"→ {cmd} ({count} times after '{last_cmd}')")
else:
    print("\n🤷 Not enough data to predict yet.")
