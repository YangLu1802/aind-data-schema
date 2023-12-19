"""Module for process names definitions"""

from enum import Enum


class ProcessName(str, Enum):
    """Data processing type labels"""

    ANALYSIS = "Analysis"
    COMPRESSION = "Compression"
    DENOISING = "Denoising"
    EPHYS_CURATION = "Ephys curation"
    EPHYS_POSTPROCESSING = "Ephys postprocessing"
    EPHYS_PREPROCESSING = "Ephys preprocessing"
    EPHYS_VISUALIZATION = "Ephys visualization"
    FIDUCIAL_SEGMENTATION = "Fiducial segmentation"
    IMAGE_ATLAS_ALIGNMENT = "Image atlas alignment"
    IMAGE_BACKGROUND_SUBTRACTION = "Image background subtraction"
    IMAGE_CELL_SEGMENTATION = "Image cell segmentation"
    IMAGE_CELL_QUANTIFICATION = "Image cell quantification"
    IMAGE_DESTRIPING = "Image destriping"
    IMAGE_FLATFIELD_CORRECTION = "Image flat-field correction"
    IMAGE_IMPORTING = "Image importing"
    IMAGE_THRESHOLDING = "Image thresholding"
    IMAGE_TILE_ALIGNMENT = "Image tile alignment"
    IMAGE_TILE_FUSING = "Image tile fusing"
    IMAGE_TILE_PROJECTION = "Image tile projection"
    FILE_CONVERSION = "File format conversion"
    MANUAL_ANNOTATION = "Manual annotation"
    NEUROPIL_SUBTRACTION = "Neuropil subtraction"
    OTHER = "Other"
    REGISTRATION_TO_TEMPLATE = "Registration to template"
    SKULL_STRIPPING = "Skull stripping"
    SPIKE_SORTING = "Spike sorting"
    SPATIAL_TIMESERIES_DEMIXING = "Spatial timeseries demixing"
    VIDEO_MOTION_CORRECTION = "Video motion correction"
    VIDEO_PLANE_DECROSSTALK = "Video plane decrosstalk"
    VIDEO_ROI_CLASSIFICATION = "Video ROI classification"
    VIDEO_ROI_SEGMENTATION = "Video ROI segmentation"
    VIDEO_ROI_TIMESERIES_EXTRACTION = "Video ROI timeseries extraction"
