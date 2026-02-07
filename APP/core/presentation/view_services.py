# =========================
# UI / Rendering Helpers
# =========================

def update_seen_vehicles(context_helpers, context, vehicles):
    """
    Policy service:
    Updates system context with the latest viewed vehicles.
    """
    if vehicles:
        context_helpers.set_seen_vehicles(context, vehicles)


def render_paginated_vehicles(sys_ctrl, ui, paginator_cls, render_func, vehicles):
    """
    UI service:
    Handles paginated rendering loop for vehicles.
    """
    paginator = paginator_cls(vehicles)
    ui.paginator_display(sys_ctrl, paginator, render_func)


def render_vehicle_details(ui, vehicles):
    """
    UI service:
    Handles vehicle selection + detailed rendering.
    """
    vehicle = ui.select_vehicle(vehicles)
    if vehicle:
        ui.render_vehicle_details(vehicle)
