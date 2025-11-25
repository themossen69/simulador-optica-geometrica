def world_axis_to_screen_axis(x: float, y: float, screen_height: int) -> tuple[int, int]:
    # (0,0) in bottom-left to (0,0) in top-left
    return (int(x), int(screen_height - y))