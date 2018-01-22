
with open ('book1.txt', 'r') as f:
    for line in f:
        row = line.split()
        if not row:
            continue
        name = row[0]
        max_score = max(map(int, row[1:]))
        entries.append((max_score, name))
