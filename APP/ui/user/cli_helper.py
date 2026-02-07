def resolve_command(command):
    commands = {
        "n": {"type": "NAVIGATION", "action": "NEXT"},
        "p": {"type": "NAVIGATION", "action": "PREVIOUS"},
        "s": {"type": "SYSTEM", "action": "ADVANCED_SEARCH"},
        "d": {"type": "SYSTEM", "action": "VEHICLE_DETAILS"},
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
    if not res.ok:
        return {"ok": res.ok, "error": res.error}
    return {"ok": res.ok, "next_page": res.payload["curt_page"]}

def get_page_state(pag, page_num):
    page = pag.get_page(page_num)
    items = page.payload.get("items", [])

    if not items:
        return {
            "ok": False,
            "reason": "No Available Vehicles!"
        }
    
    return {
        "ok": True,
        "page": page
    }

def system_command_handler(sys_ctrl, sys_command):
    sys_act = {
        "ADVANCED_SEARCH": sys_ctrl.dispatcher.execute,
        "VEHICLE_DETAILS": sys_ctrl.dispatcher.execute
    }
    action = sys_act.get(sys_command)
    return action(sys_command)

# def render_vehicles(data):

#     if isinstance(data, list):
#             render_vehicles_brief(data)

#     elif isinstance(data, dict):
#         select_vehicle(data)
#         if vehcile:
#             render_vehicle_details(vehicle)
