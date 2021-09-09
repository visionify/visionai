# -*- coding: utf-8 -*-

"""
visionai.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of visionai's exceptions.
"""


class VisionAiException(Exception):
    """Ambiguous Exception occurred."""


class VisionAiInvalidFormat(VisionAiException):
    """Invalid Format Exception occurred."""


class VisionAiValueError(VisionAiException):
    """Invalid Values Specified."""

class VisionAiDecodeException(VisionAiException):
    """Decode Exception occurred"""


class VisionAiTimeoutException(VisionAiException):
    """Timeout Exception occurred"""

class VisionAiModelNotFound(VisionAiException):
    """Model file not found locally or in cloud."""

