from typing import Any, Dict, List, Optional

from pydantic import BaseModel, computed_field

class CdnFilePath(BaseModel):
    wrappedProcPath: Optional[str] = None
    wrappedLthPath: Optional[str] = None
    procPath: Optional[str] = None
    lthPath: Optional[str] = None
    thPath: Optional[str] = None

class OriginalFilePath(BaseModel):
    wrappedProcPath: Optional[str] = None
    wrappedLthPath: Optional[str] = None
    procPath: Optional[str] = None
    lthPath: Optional[str] = None
    thPath: Optional[str] = None

class Geometry(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None
    matchLat: Optional[float] = None
    matchLng: Optional[float] = None

class CameraParameters(BaseModel):
    fLen: Optional[float] = None
    aperture: Optional[float] = None
    hFoV: Optional[float] = None
    vFoV: Optional[float] = None

class Sequence(BaseModel):
    id: Optional[str] = None
    currentLat: Optional[str] = None
    currentLng: Optional[str] = None
    countryCode: Optional[str] = None
    stateCode: Optional[str] = None
    address: Optional[str] = None
    sequenceType: Optional[str] = None
    countActivePhotos: Optional[str] = None
    distance: Optional[str] = None
    deviceName: Optional[str] = None
    platformName: Optional[str] = None
    uploadSource: Optional[str] = None
    storage: Optional[str] = None
    cameraParameters: Optional[CameraParameters] = None

class Photo(BaseModel):
    autoImgProcessingStatus: Optional[str] = None
    distance: Optional[str] = None
    fieldOfView: Optional[str] = None
    fileurlProc: Optional[str] = None
    fileurlTh: Optional[str] = None
    heading: Optional[str] = None
    height: Optional[str] = None
    id: Optional[str] = None
    lat: Optional[str] = None
    lng: Optional[str] = None
    matchLat: Optional[str] = None
    matchLng: Optional[str] = None
    sequence: Optional[Sequence] = None
    shotDate: Optional[str] = None
    status: Optional[str] = None
    storage: Optional[str] = None
    wayId: Optional[str] = None
    width: Optional[str] = None

class Status(BaseModel):
    apiCode: Optional[int] = None
    apiMessage: Optional[str] = None
    httpCode: Optional[int] = None
    httpMessage: Optional[str] = None

class Result(BaseModel):
    data: Optional[List[Photo]] = None

class PhotosResponse(BaseModel):
    result: Optional[Result] = None

class BriefPhoto(BaseModel):
    id: Optional[str] = None
    sequenceId: Optional[str] = None
    sequenceIndex: Optional[str] = None
    dateAdded: Optional[str] = None
    originalHeading: Optional[float] = None
    calculatedHeading: Optional[float] = None
    #orgCode: Optional[str] = None
    cdnFilePath: Optional[CdnFilePath] = None
    geometry: Optional[Geometry] = None
    imageViewEqCenter: Optional[List[float]] = None
    imageViewFov: Optional[List[float]] = None
    #confidenceScore: Optional[float] = None

class ObjectSearchResponse(BaseModel):
    #photos: Optional[List] = None
    briefPhotos: Optional[List[BriefPhoto]] = None
    error: Optional[str] = None
