# Task 7: Filter out inactive players, sort by score (highest first),
# keep the top 3, and format as "Rank <n>: <username> (<score>)".

players = [
    ("Aria", 88, True),
    ("Kael", 95, False),
    ("Zane", 91, True),
    ("Mira", 76, True),
    ("Lyra", 99, True),
    ("Dax", 84, True),
]

active = [p for p in players if p[2]]
top_three = sorted(active, key=lambda p: p[1], reverse=True)[:3]

leaderboard = [
    f"Rank {rank}: {name} ({score})"
    for rank, (name, score, _) in enumerate(top_three, start=1)
]

print(leaderboard)  # ['Rank 1: Lyra (99)', 'Rank 2: Zane (91)', 'Rank 3: Aria (88)']
