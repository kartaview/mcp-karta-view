from typing import Any, Dict, List, Optional

from pydantic import BaseModel, computed_field

class CameraParameters(BaseModel):
    fLen: Optional[float] = None
    aperture: Optional[float] = None
    hFoV: Optional[float] = None
    vFoV: Optional[float] = None

class Sequence(BaseModel):
    id: Optional[str] = None
    #userId: Optional[str] = None
    #dateAdded: Optional[str] = None
    #dateProcessed: Optional[str] = None
    #imageProcessingStatus: Optional[str] = None
    #isVideo: Optional[str] = None
    currentLat: Optional[str] = None
    currentLng: Optional[str] = None
    countryCode: Optional[str] = None
    stateCode: Optional[str] = None
    address: Optional[str] = None
    sequenceType: Optional[str] = None
    countActivePhotos: Optional[str] = None
    distance: Optional[str] = None
    #metaDataFilename: Optional[str] = None
    #clientTotal: Optional[str] = None
    #obdInfo: Optional[str] = None
    deviceName: Optional[str] = None
    platformName: Optional[str] = None
    #platformVersion: Optional[str] = None
    #appVersion: Optional[str] = None
    #matched: Optional[str] = None
    uploadSource: Optional[str] = None
    storage: Optional[str] = None
    #countMetadataPhotos: Optional[str] = None
    #uploadStatus: Optional[str] = None
    #processingStatus: Optional[str] = None
    #metadataStatus: Optional[str] = None
    #hasRawData: Optional[str] = None
    #countMetadataVideos: Optional[str] = None
    #qualityStatus: Optional[str] = None
    #quality: Optional[str] = None
    cameraParameters: Optional[CameraParameters] = None
    #blurVersion: Optional[str] = None
    #blurBuild: Optional[str] = None
    #status: Optional[str] = None
    #matchStatus: Optional[str] = None
    #orgCode: Optional[str] = None
    #nwLat: Optional[str] = None
    #nwLng: Optional[str] = None
    #seLat: Optional[str] = None
    #seLng: Optional[str] = None
    #fieldOfView: Optional[str] = None
    #refKey: Optional[str] = None
    #refValue: Optional[str] = None
    #deviceId: Optional[str] = None

class Photo(BaseModel):
    #autoImgProcessingResult: Optional[str] = None
    autoImgProcessingStatus: Optional[str] = None
    #cameraParameters: Optional[CameraParameters] = None
    #dateAdded: Optional[str] = None
    #dateProcessed: Optional[str] = None
    distance: Optional[str] = None
    fieldOfView: Optional[str] = None
    #filepath: Optional[str] = None
    #filepathLTh: Optional[str] = None
    #filepathProc: Optional[str] = None
    #filepathTh: Optional[str] = None
    #fileurl: Optional[str] = None
    #fileurlLTh: Optional[str] = None
    fileurlProc: Optional[str] = None
    fileurlTh: Optional[str] = None
    #from_: Optional[str] = None
    #gpsAccuracy: Optional[str] = None
    #hasObd: Optional[str] = None
    #headers: Optional[str] = None
    heading: Optional[str] = None
    height: Optional[str] = None
    id: Optional[str] = None
    #imageLthUrl: Optional[str] = None
    #imagePartProjection: Optional[str] = None
    #imageProcUrl: Optional[str] = None
    #imageThUrl: Optional[str] = None
    #isUnwrapped: Optional[str] = None
    #isWrapped: Optional[str] = None
    lat: Optional[str] = None
    lng: Optional[str] = None
    matchLat: Optional[str] = None
    matchLng: Optional[str] = None
    #matchSegmentId: Optional[str] = None
    #name: Optional[str] = None
    #orgCode: Optional[str] = None
    #projection: Optional[str] = None
    #projectionYaw: Optional[str] = None
    #qualityDetails: Optional[str] = None
    #qualityLevel: Optional[str] = None
    #qualityStatus: Optional[str] = None
    #rawDataId: Optional[str] = None
    sequence: Optional[Sequence] = None
    #sequenceIndex: Optional[str] = None
    shotDate: Optional[str] = None
    status: Optional[str] = None
    storage: Optional[str] = None
    #to: Optional[str] = None
    #unwrapVersion: Optional[str] = None
    #videoId: Optional[str] = None
    #videoIndex: Optional[str] = None
    #visibility: Optional[str] = None
    wayId: Optional[str] = None
    width: Optional[str] = None
    #wrapVersion: Optional[str] = None

class Status(BaseModel):
    apiCode: Optional[int] = None
    apiMessage: Optional[str] = None
    httpCode: Optional[int] = None
    httpMessage: Optional[str] = None

class Result(BaseModel):
    data: Optional[List[Photo]] = None

class PhotosResponse(BaseModel):
    #status: Optional[Status] = None
    result: Optional[Result] = None
