from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class FootballFieldConfiguration:
    # Field dimensions in inches (NCAA specifications)
    width: int = 1920   # 53.33 yards * 36 inches/yard
    length: int = 4320  # 120 yards * 36 inches/yard
    end_zone_depth: int = 360  # 10 yards * 36 inches/yard
    goal_line_1: int = 360     # 10 yards from end
    goal_line_2: int = 3960    # 110 yards from start
    hash_distance_from_sideline: int = 720  # 60 feet * 12 inches/foot
    hash_length: int = 24      # 24 inches
    yard_line_interval: int = 180  # 5 yards * 36 inches/yard
    fifty_yard_line: int = 2160    # 60 yards * 36 inches/yard
    number_distance_from_sideline: int = 324  # 9 yards * 36 inches/yard

    @property
    def vertices(self) -> List[Tuple[int, int]]:
        return [
            # Corner vertices
            (0, 0),  # 1 - Back left corner of left end zone
            (0, self.width),  # 2 - Back right corner of left end zone
            (self.length, 0),  # 3 - Back left corner of right end zone
            (self.length, self.width),  # 4 - Back right corner of right end zone
            
            # Goal line vertices
            (self.goal_line_1, 0),  # 5 - Left goal line, left sideline
            (self.goal_line_1, self.width),  # 6 - Left goal line, right sideline
            (self.goal_line_2, 0),  # 7 - Right goal line, left sideline
            (self.goal_line_2, self.width),  # 8 - Right goal line, right sideline
            
            # 50-yard line vertices
            (self.fifty_yard_line, 0),  # 9 - 50-yard line, left sideline
            (self.fifty_yard_line, self.width),  # 10 - 50-yard line, right sideline
            (self.fifty_yard_line, self.width / 2),  # 11 - 50-yard line center
            
            # Hash mark positions (top and bottom)
            (self.goal_line_1, self.hash_distance_from_sideline),  # 12 - Left goal line, top hash
            (self.goal_line_1, self.width - self.hash_distance_from_sideline),  # 13 - Left goal line, bottom hash
            (self.goal_line_2, self.hash_distance_from_sideline),  # 14 - Right goal line, top hash
            (self.goal_line_2, self.width - self.hash_distance_from_sideline),  # 15 - Right goal line, bottom hash
            (self.fifty_yard_line, self.hash_distance_from_sideline),  # 16 - 50-yard line, top hash
            (self.fifty_yard_line, self.width - self.hash_distance_from_sideline),  # 17 - 50-yard line, bottom hash
            
            # Major yard line intersections with hash marks (20, 30, 40 yard lines)
            (self.goal_line_1 + self.yard_line_interval * 2, self.hash_distance_from_sideline),  # 18 - 20 yard, top hash
            (self.goal_line_1 + self.yard_line_interval * 2, self.width - self.hash_distance_from_sideline),  # 19 - 20 yard, bottom hash
            (self.goal_line_1 + self.yard_line_interval * 4, self.hash_distance_from_sideline),  # 20 - 30 yard, top hash
            (self.goal_line_1 + self.yard_line_interval * 4, self.width - self.hash_distance_from_sideline),  # 21 - 30 yard, bottom hash
            (self.goal_line_1 + self.yard_line_interval * 6, self.hash_distance_from_sideline),  # 22 - 40 yard, top hash
            (self.goal_line_1 + self.yard_line_interval * 6, self.width - self.hash_distance_from_sideline),  # 23 - 40 yard, bottom hash
            
            # Corresponding yard lines on the other side (80, 70, 60 yard lines)
            (self.goal_line_2 - self.yard_line_interval * 6, self.hash_distance_from_sideline),  # 24 - 60 yard, top hash
            (self.goal_line_2 - self.yard_line_interval * 6, self.width - self.hash_distance_from_sideline),  # 25 - 60 yard, bottom hash
            (self.goal_line_2 - self.yard_line_interval * 4, self.hash_distance_from_sideline),  # 26 - 70 yard, top hash
            (self.goal_line_2 - self.yard_line_interval * 4, self.width - self.hash_distance_from_sideline),  # 27 - 70 yard, bottom hash
            (self.goal_line_2 - self.yard_line_interval * 2, self.hash_distance_from_sideline),  # 28 - 80 yard, top hash
            (self.goal_line_2 - self.yard_line_interval * 2, self.width - self.hash_distance_from_sideline),  # 29 - 80 yard, bottom hash
            
            # Number positioning vertices (for major yard lines)
            (self.goal_line_1 + self.yard_line_interval * 2, self.number_distance_from_sideline),  # 30 - 20 yard, number position top
            (self.goal_line_1 + self.yard_line_interval * 2, self.width - self.number_distance_from_sideline),  # 31 - 20 yard, number position bottom
            (self.fifty_yard_line, self.number_distance_from_sideline),  # 32 - 50 yard, number position top
        ]

    edges: List[Tuple[int, int]] = field(default_factory=lambda: [
        # Sidelines
        (1, 3), (2, 4),  # Top and bottom sidelines (full length)
        
        # End zone back lines
        (1, 2), (3, 4),  # Left and right end zone back lines
        
        # Goal lines
        (5, 6), (7, 8),  # Left and right goal lines
        
        # 50-yard line
        (9, 10),  # 50-yard line
        
        # Connect corners to goal lines
        (1, 5), (2, 6), (3, 7), (4, 8),
        
        # Hash mark connections (showing hash mark lines)
        (12, 13), (14, 15), (16, 17),  # Goal lines and 50-yard line hash marks
        (18, 19), (20, 21), (22, 23),  # Left side yard line hash marks
        (24, 25), (26, 27), (28, 29),  # Right side yard line hash marks
        
        # Connect goal lines to 50-yard line along sidelines
        (5, 9), (6, 10), (9, 7), (10, 8),
    ])

    labels: List[str] = field(default_factory=lambda: [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
        "31", "32"
    ])

    colors: List[str] = field(default_factory=lambda: [
        "#FF1493", "#FF1493", "#FF1493", "#FF1493",  # Corner vertices - pink
        "#FF1493", "#FF1493", "#FF1493", "#FF1493",  # Goal line vertices - pink
        "#00BFFF", "#00BFFF", "#00BFFF",  # 50-yard line vertices - blue
        "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347",  # Hash marks - tomato
        "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347",  # Yard line hash intersections - tomato
        "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347",  # More hash intersections - tomato
        "#00BFFF", "#00BFFF", "#00BFFF"  # Number positioning vertices - blue
    ])
