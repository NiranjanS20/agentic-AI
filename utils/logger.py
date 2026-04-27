def log_message(role, content):
    with open("chat_history.log", "a") as f:
        f.write(f"{role.upper()}: {content}\n")