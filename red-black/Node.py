from typing import Any, Optional

class Node:
    def __init__(self, 
    value: Any = None, 
    color: str = "Red", 
    left: Optional['Node'] = None, 
    right: Optional['Node']= None, 
    parent: Optional['Node'] = None ) -> None:
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
