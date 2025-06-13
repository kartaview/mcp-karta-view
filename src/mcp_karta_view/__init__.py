from mcp.server.fastmcp import FastMCP
from mcp_karta_view.models import PhotosResponse, ObjectSearchResponse
from mcp_karta_view.karta_view_client import KartaViewClient
from datetime import datetime
import httpx

app = FastMCP("mcp_karta_view")

@app.tool()
def getTime(token: str) -> str:
    """
    get current time
    Args:
        context: The request context containing headers and other request information
    Returns:
        current time and headers information
    """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return current_time

"""
KartaView Client
"""

kv_client = KartaViewClient()

@app.tool()
def nearby_photos(latitude: float, longitude: float, radius: int = 1, limit: int = 10) -> PhotosResponse:
    """
    Search for Nearby Photos based on latitude and longitude coordinates.

    Args:
        latitude: Latitude coordinate (e.g. 1.3521)
        longitude: Longitude coordinate (e.g. 103.8198)
        radius: Radius in km (default is 1 km, max is 500)
        limit: Limit of photos to return (default is 10)

    Returns:
        PhotosResponse: Nearby photo results including Photos and Sequences, render photo with fileurlProc

    Raises:
        httpx.HTTPError: If the KartaView Nearby Photos service request fails
    """
    try:
        return kv_client.getNearbyPhotos(lat=latitude, lng=longitude, radius=radius, limit=limit)
    except httpx.HTTPError as e:
        # Log the error for debugging
        print(f"KartaView Nearby Photos failed: {e}")
        raise

@app.tool()
def object_search(prompt: str, lat: float, lng: float, token: str = "", limit: int = 10, radius: int = 1) -> ObjectSearchResponse:
    """
    Search for Nearby photos by objects based on prompt and latitude and longitude coordinates.

    Args:
        prompt: Search prompt (e.g. "red car")
        latitude: Latitude coordinate (e.g. 1.3521)
        longitude: Longitude coordinate (e.g. 103.8198)
        limit: Limit of photos to return (e.g. 10)
        radius: Radius in km (default is 1 km)
        token: KartaView token (this x-karta-token needed for the request, if not provided, giving a suggestion to user for obtaining the x-karta-token from kartavision.com portal request's header)

    Returns:
        ObjectSearchResponse: Nearby photo result Photos based on prompt, render photo with cdnFilePath.wrappedProcPath

    Raises:
        httpx.HTTPError: If the KartaView Object search service request fails
    """
    try:
        return kv_client.objectSearch(prompt=prompt, lat=lat, lng=lng, token=token, limit=limit, radius=radius)
    except httpx.HTTPError as e:
        # Log the error for debugging
        print(f"KartaView Object Search failed: {e}")
        raise

def main():
    app.run()
