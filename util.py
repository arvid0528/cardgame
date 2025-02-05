
def mouse_within_rect(mx, my, x, y, w, h):
    return mx > x and mx < x + w and my > y and my < y + h