def flames_result(data):
   name1 = data.get("name1") or data.get("name") or ""
   name2 = data.get("name2") or data.get("partnerName") or ""
    
   n1 = name1.lower().replace(" ", "")
   n2 = name2.lower().replace(" ", "")

    # Remove common letters
    n1_list = list(n1)
    n2_list = list(n2)
    for ch in n1_list[:]:
        if ch in n2_list:
            n1_list.remove(ch)
            n2_list.remove(ch)

    count = len(n1_list) + len(n2_list)

    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        split = (count % len(flames)) - 1
        if split >= 0:
            right = flames[split + 1:]
            left = flames[:split]
            flames = right + left
        else:
            flames = flames[:-1]
    
    final = flames[0]
    meaning = {
        'F': ("Friends", "🤝", "You both share a strong friendly bond."),
        'L': ("Love", "💖", "There’s a spark of love between you two. Keep the bond alive!"),
        'A': ("Affection", "😊", "You have a soft spot for each other. It’s a warm connection."),
        'M': ("Marriage", "💍", "Wow! A strong potential for long-term commitment."),
        'E': ("Enemies", "⚔️", "Uh-oh! Frequent clashes possible — handle with care."),
        'S': ("Siblings", "👫", "You share sibling-like energy — playful and caring.")
    }

    title, emoji, msg = meaning[final]
    return {
        "tool": "flames-check",
        "name1": name1,
        "name2": name2,
        "result": title,
        "emoji": emoji,
        "message": msg
    }
