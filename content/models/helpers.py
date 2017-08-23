from collections import defaultdict


def group_by_key(rows, key):
    v = defaultdict(list)

    for row in rows:
        v[row[key]].append(row)

    return v
