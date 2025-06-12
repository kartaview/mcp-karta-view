from mcp.server.fastmcp import FastMCP
from mcp_karta_view.models import PhotosResponse
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
def nearby_photos(latitude: float, longitude: float, radius: int = 99, limit: int = 10) -> PhotosResponse:
    """
    Search for Nearby Photos based on latitude and longitude coordinates.

    Args:
        latitude: Latitude coordinate (e.g. 1.3521)
        longitude: Longitude coordinate (e.g. 103.8198)
        radius: Radius in km (default is 99, max is 99)
        limit: Limit of photos to return (default is 10)

    Returns:
        PhotosResponse: Nearby photo results including Photos and Sequences, render photo with fileurlProc

    Raises:
        httpx.HTTPError: If the KartaView Nearby Photos service request fails
    """
    try:
        return kv_client.getNearbyPhotos(lat=latitude, lng=longitude)
    except httpx.HTTPError as e:
        # Log the error for debugging
        print(f"KartaView Nearby Photos failed: {e}")
        raise

def main():
    app.run()
