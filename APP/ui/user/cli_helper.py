def resolve_command(command):
    commands = {
        "n": {"type": "NAVIGATION", "action": "NEXT"},
        "p": {"type": "NAVIGATION", "action": "PREVIOUS"},
        "s": {"type": "SYSTEM", "action": "ADVANCED_SEARCH"},
        "d": {"type": "SYSTEM", "action": "VEHCILE_DETAILS"},
        "q": {"type": "EXIT", "action": "QUIT"}
    }
    action = commands.get(command)
    if action:
        return action
    return {"type": "INVALID", "error": "Invalid command."}

def update_navigation_state(nav_command, curt_page, pag):
    actions = {
        "NEXT": pag.next,
        "PREVIOUS": pag.prev
    }
    action = actions.get(nav_command)
    return action(curt_page)

def handle_navigation_result(res):
    if not res.meta["can_move"] or res.error:
        return res.error
    return res.payload["current_page"]
