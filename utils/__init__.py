from .abstract import TimeStampModel, DeletedModel
from .upload_paths import (
    courseImageUpload,
    testemonialsImageUpload,
    trainersImageUpload
)

__all__ = [
    # abstract models
    "TimeStampModel",
    "DeletedModel",

    # upload paths
    "courseImageUpload",
    "testemonialsImageUpload",
    "trainersImageUpload",

    
]