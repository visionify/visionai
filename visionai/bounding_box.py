import math

from .exceptions import VisionAiInvalidFormat

class BoundingBox():
    """Bounding box object"""
    def __init__(self, x1:int, y1:int, x2:int, y2:int):
        if (not isinstance(x1, int) or
                not isinstance(y1, int) or
                not isinstance(x2, int) or
                not isinstance(y2, int)):
            raise VisionAiInvalidFormat('Bounding box should have x1, y1, x2, y2 as integers.')

        if x1 >= x2:
            raise ValueError('Expected x1 < x2')

        if y1 >= y2:
            raise ValueError('Expected y1 < y2')

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    @property
    def width(self):
        """
        Return width of the BoundingBox

        :return: int -> width of BoundingBox
        """
        return self._x2 - self._x1

    @property
    def height(self) -> int:
        """
        Return height of the BoundingBox
        :return: int-> Height of BoundingBox
        """
        return self._y2 - self._y1

    @property
    def area(self) -> int:
        """
        Area of a bounding box

        :return: int -> Area of the BoundingBox.
        """
        return self.width * self.height

    @property
    def center(self) -> (int, int):
        """
        Center of a BoundingBox
        :return: x, y coordinates of the center
        """
        return int((self._x1 + self._x2)/2), int((self._y1 + self._y2)/2)

    def compute_distance(self, box2) -> float:
        """
        Return euclidian distance between centers of two boxes.

        :param box2: Another BoundingBox
        :return: float - Euclidian distance.
        """

        """Return euclidian distance between centers of
        two boxes"""
        if not isinstance(box2, BoundingBox):
            raise VisionAiInvalidFormat('Can only compute distance with another BoundingBox')

        center1_x, center1_y = self.center
        center2_x, center2_y = box2.center
        return math.sqrt(
            (center1_x - center2_x) * (center1_x - center2_x) +
            (center1_y - center2_y) * (center1_y - center2_y))

    def get_intersection_bounding_box(self, box2):
        """
        Return intersection BoundingBox

        :param box2: Other bounding box.
        :return: BoundingBox representing intersection.
        :return: None if there is no intersection.
        """

        if not isinstance(box2, BoundingBox):
            raise VisionAiInvalidFormat('box2 should be a BoundingBox')

        # Calculate intersection area first. If 0, return None.
        xA = max(self.x1, box2.x1)
        yA = max(self.y1, box2.y1)
        xB = min(self.x2, box2.x2)
        yB = min(self.y2, box2.y2)

        # Intersection area:
        interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
        if interArea == 0:
            return None

        return BoundingBox(xA, yA, xB, yB)

    def get_intersection_percent(self, box2):
        """
        Return intersection overlap percent from box2

        :param box2: Other bounding box.
        :return: float [between 0..1] Intersection area percentage.
        """

        if not isinstance(box2, BoundingBox):
            raise VisionAiInvalidFormat('box2 should be a BoundingBox')

        # Calculate intersection area first. If 0, return None.
        xA = max(self.x1, box2.x1)
        yA = max(self.y1, box2.y1)
        xB = min(self.x2, box2.x2)
        yB = min(self.y2, box2.y2)

        # Intersection area:
        interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
        return interArea / self.area
