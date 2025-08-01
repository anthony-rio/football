import cv2
import supervision as sv
import numpy as np

from football.configs import FootballFieldConfiguration


def draw_field(
    config: FootballFieldConfiguration,
    background_color: sv.Color = sv.Color(34, 139, 34),
    line_color: sv.Color = sv.Color.WHITE,
    padding: int = 50,
    line_thickness: int = 4,
    point_radius: int = 8,
    scale: float = 0.1
) -> np.ndarray:
    """
    Draws a football field with specified dimensions, colors, and scale.

    Args:
        config (FootballFieldConfiguration): Configuration object containing the
            dimensions and layout of the field.
        background_color (sv.Color, optional): Color of the field background.
            Defaults to sv.Color(34, 139, 34).
        line_color (sv.Color, optional): Color of the field lines.
            Defaults to sv.Color.WHITE.
        padding (int, optional): Padding around the field in pixels.
            Defaults to 50.
        line_thickness (int, optional): Thickness of the field lines in pixels.
            Defaults to 4.
        point_radius (int, optional): Radius of the hash mark points in pixels.
            Defaults to 8.
        scale (float, optional): Scaling factor for the field dimensions.
            Defaults to 0.1.

    Returns:
        np.ndarray: Image of the football field.
    """
    scaled_width = int(config.width * scale)
    scaled_length = int(config.length * scale)
    scaled_hash_length = int(config.hash_length * scale)

    field_image = np.ones(
        (scaled_width + 2 * padding,
         scaled_length + 2 * padding, 3),
        dtype=np.uint8
    ) * np.array(background_color.as_bgr(), dtype=np.uint8)

    # Draw field lines using edges
    for start, end in config.edges:
        point1 = (int(config.vertices[start - 1][0] * scale) + padding,
                  int(config.vertices[start - 1][1] * scale) + padding)
        point2 = (int(config.vertices[end - 1][0] * scale) + padding,
                  int(config.vertices[end - 1][1] * scale) + padding)
        cv2.line(
            img=field_image,
            pt1=point1,
            pt2=point2,
            color=line_color.as_bgr(),
            thickness=line_thickness
        )

    # Draw yard lines (every 5 yards from 10 to 110)
    yard_line_interval_scaled = int(config.yard_line_interval * scale)
    goal_line_1_scaled = int(config.goal_line_1 * scale)
    
    for i in range(1, 21):  # 15, 20, 25, ..., 105 yard lines
        yard_x = goal_line_1_scaled + (i * yard_line_interval_scaled) + padding
        if yard_x < scaled_length + padding:  # Make sure we don't go beyond the field
            cv2.line(
                img=field_image,
                pt1=(yard_x, padding),
                pt2=(yard_x, scaled_width + padding),
                color=line_color.as_bgr(),
                thickness=line_thickness
            )

    # Draw hash marks
    hash_distance_scaled = int(config.hash_distance_from_sideline * scale)
    hash_length_scaled = int(config.hash_length * scale)
    
    for i in range(0, 21):  # Hash marks at all yard lines from 10 to 110
        yard_x = goal_line_1_scaled + (i * yard_line_interval_scaled) + padding
        if yard_x < scaled_length + padding:
            # Top hash marks
            cv2.line(
                img=field_image,
                pt1=(yard_x, hash_distance_scaled + padding - hash_length_scaled // 2),
                pt2=(yard_x, hash_distance_scaled + padding + hash_length_scaled // 2),
                color=line_color.as_bgr(),
                thickness=line_thickness
            )
            # Bottom hash marks
            cv2.line(
                img=field_image,
                pt1=(yard_x, scaled_width - hash_distance_scaled + padding - hash_length_scaled // 2),
                pt2=(yard_x, scaled_width - hash_distance_scaled + padding + hash_length_scaled // 2),
                color=line_color.as_bgr(),
                thickness=line_thickness
            )

    return field_image


def draw_points_on_field(
    config: FootballFieldConfiguration,
    xy: np.ndarray,
    face_color: sv.Color = sv.Color.RED,
    edge_color: sv.Color = sv.Color.BLACK,
    radius: int = 10,
    thickness: int = 2,
    padding: int = 50,
    scale: float = 0.1,
    field: Optional[np.ndarray] = None
) -> np.ndarray:
    """
    Draws points on a football field.

    Args:
        config (FootballFieldConfiguration): Configuration object containing the
            dimensions and layout of the field.
        xy (np.ndarray): Array of points to be drawn, with each point represented by
            its (x, y) coordinates.
        face_color (sv.Color, optional): Color of the point faces.
            Defaults to sv.Color.RED.
        edge_color (sv.Color, optional): Color of the point edges.
            Defaults to sv.Color.BLACK.
        radius (int, optional): Radius of the points in pixels.
            Defaults to 10.
        thickness (int, optional): Thickness of the point edges in pixels.
            Defaults to 2.
        padding (int, optional): Padding around the field in pixels.
            Defaults to 50.
        scale (float, optional): Scaling factor for the field dimensions.
            Defaults to 0.1.
        field (Optional[np.ndarray], optional): Existing field image to draw points on.
            If None, a new field will be created. Defaults to None.

    Returns:
        np.ndarray: Image of the football field with points drawn on it.
    """
    if field is None:
        field = draw_field(
            config=config,
            padding=padding,
            scale=scale
        )

    for point in xy:
        scaled_point = (
            int(point[0] * scale) + padding,
            int(point[1] * scale) + padding
        )
        cv2.circle(
            img=field,
            center=scaled_point,
            radius=radius,
            color=face_color.as_bgr(),
            thickness=-1
        )
        cv2.circle(
            img=field,
            center=scaled_point,
            radius=radius,
            color=edge_color.as_bgr(),
            thickness=thickness
        )

    return field


def draw_paths_on_field(
    config: FootballFieldConfiguration,
    paths: List[np.ndarray],
    color: sv.Color = sv.Color.WHITE,
    thickness: int = 2,
    padding: int = 50,
    scale: float = 0.1,
    field: Optional[np.ndarray] = None
) -> np.ndarray:
    """
    Draws paths on a football field.

    Args:
        config (FootballFieldConfiguration): Configuration object containing the
            dimensions and layout of the field.
        paths (List[np.ndarray]): List of paths, where each path is an array of (x, y)
            coordinates.
        color (sv.Color, optional): Color of the paths.
            Defaults to sv.Color.WHITE.
        thickness (int, optional): Thickness of the paths in pixels.
            Defaults to 2.
        padding (int, optional): Padding around the field in pixels.
            Defaults to 50.
        scale (float, optional): Scaling factor for the field dimensions.
            Defaults to 0.1.
        field (Optional[np.ndarray], optional): Existing field image to draw paths on.
            If None, a new field will be created. Defaults to None.

    Returns:
        np.ndarray: Image of the football field with paths drawn on it.
    """
    if field is None:
        field = draw_field(
            config=config,
            padding=padding,
            scale=scale
        )

    for path in paths:
        scaled_path = [
            (
                int(point[0] * scale) + padding,
                int(point[1] * scale) + padding
            )
            for point in path if point.size > 0
        ]

        if len(scaled_path) < 2:
            continue

        for i in range(len(scaled_path) - 1):
            cv2.line(
                img=field,
                pt1=scaled_path[i],
                pt2=scaled_path[i + 1],
                color=color.as_bgr(),
                thickness=thickness
            )

    return field
