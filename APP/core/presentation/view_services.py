# =========================
# UI / Rendering Helpers
# =========================

def render_paginated_view(ui, paginator, render_func, data):
    """
    Render a collection (like vehicles) with pagination.
    Pure function: does not modify system context.
    """
    if data:
        pagin = paginator(data)
        return ui.paginator_display(pagin, render_func)
