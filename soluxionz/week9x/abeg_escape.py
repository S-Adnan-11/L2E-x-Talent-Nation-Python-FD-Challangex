def build_rooms():
    return {
        "bedroom": {
            "text": "You wake up in a dark compound. Your slippers are gone. A torch is by the pillow.",
            "exits": {"north": "hall"}, "item": "torch",
        },
        "hall": {
            "text": "Three doors, one gate, and a crooked portrait looking a bit too interested.",
            "exits": {"south": "bedroom", "east": "kitchen", "west": "store",
                      "north": "gate", "run": "lose"},
        },
        "kitchen": {
            "text": "Empty pot. Key on the counter. At least something here is useful.",
            "exits": {"back": "hall"}, "item": "key",
        },
        "store": {
            "text": "A generator is humming without fuel. Abeg don't touch that wire.",
            "exits": {"back": "hall", "touch": "lose"},
        },
        "gate": {
            "text": "The locked gate leads into a pitch-black passage. Try OPEN when ready.",
            "exits": {"back": "hall"},
        },
        "secret": {
            "text": "Behind the portrait: 'A key opens the gate. A torch gets you through.' Helpful ghost lol.",
            "exits": {"back": "hall"},
        },
        "win": {
            "text": "Outside! The ghost throws your slippers after you. Good ending, no rent owed 😼.",
            "exits": {}, "ending": "won",
        },
        "lose": {
            "text": "The compound has claimed you. Lifetime rent. Well and truly cooked 😭.",
            "exits": {}, "ending": "lost",
        },
    }


def new_game():
    return {"room": "bedroom", "inventory": [], "turns": 0,
            "status": "playing", "message": "Get out before the compound locks up. Twelve actions."}


def move(state, command, rooms, max_turns=12):
    if type(max_turns) is not int or max_turns < 1:
        raise ValueError("Turn limit must be a positive integer.")
    next_state = state.copy()
    next_state["inventory"] = state["inventory"].copy()
    if state["status"] != "playing":
        return next_state
    command = command.strip().lower()
    current_room = state["room"]
    room = rooms[current_room]
    if command == "quit":
        next_state["status"] = "quit"
        next_state["message"] = "Left the game. The compound can wait."
        return next_state
    if command == "look":
        next_state["message"] = room["text"]
        return next_state
    if command == "inventory":
        next_state["message"] = "Inventory: " + (", ".join(state["inventory"]) or "empty")
        return next_state
    if command.startswith("take "):
        item = command[5:].strip()
        if room.get("item") != item:
            next_state["message"] = "That item isn't here. Try looking around."
            return next_state
        if item in state["inventory"]:
            next_state["message"] = "Already carrying that one."
            return next_state
        next_state["inventory"].append(item)
        next_state["message"] = "Picked up " + item + "."
    elif current_room == "gate" and command == "open":
        if "key" not in state["inventory"]:
            next_state["message"] = "Gate's locked. A key would help."
            return next_state
        if "torch" not in state["inventory"]:
            next_state["message"] = "Too dark beyond the gate. Find a torch first."
            return next_state
        next_state["room"] = "win"
        next_state["message"] = rooms["win"]["text"]
    elif current_room == "hall" and command == "inspect portrait":
        next_state["room"] = "secret"
        next_state["message"] = rooms["secret"]["text"]
    elif command in room["exits"]:
        next_state["room"] = room["exits"][command]
        next_state["message"] = rooms[next_state["room"]]["text"]
    else:
        next_state["message"] = "Not an option here. Try a direction, look, inventory or quit."
        return next_state

    next_state["turns"] += 1
    next_state["status"] = rooms[next_state["room"]].get("ending", "playing")
    if next_state["status"] == "playing" and next_state["turns"] >= max_turns:
        next_state["room"] = "lose"
        next_state["status"] = "lost"
        next_state["message"] = "Out of turns. " + rooms["lose"]["text"]
    return next_state


def main():
    rooms = build_rooms()
    state = new_game()
    print("abeg escape — a haunted compound with very unreasonable rent")
    while state["status"] == "playing":
        room = rooms[state["room"]]
        print("\n" + state["message"])
        if state["message"] != room["text"]:
            print(room["text"])
        choices = list(room["exits"])
        if room.get("item") and room["item"] not in state["inventory"]:
            choices.append("take " + room["item"])
        if state["room"] == "gate":
            choices.append("open")
        print("Options:", ", ".join(choices), "| look | inventory | quit")
        print("Actions used:", state["turns"], "/ 12")
        try:
            command = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            command = "quit"
        state = move(state, command, rooms)
    print(state["message"])
    print("Ending:", state["status"])


if __name__ == "__main__":
    main()
