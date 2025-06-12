import json

import httpx

from .config import KARTAVIEW_PUBLIC_URL
from .models import PhotosResponse


class KartaViewClient:
    def __init__(self, base_url: str = KARTAVIEW_PUBLIC_URL, token: str = ""):
        self.base_url = base_url
        self.client = httpx.Client(headers={
            "Authorization": token
        })

    def _handle_error_response(self, response: httpx.Response):
        """Handle error response and extract error message"""
        try:
            error_data = response.json()
            if "errors" in error_data and len(error_data["errors"]) > 0:
                error_message = error_data["errors"][0].get("message", "Unknown error")
                raise httpx.HTTPError(f"API Error: {error_message}")
        except ValueError:
            response.raise_for_status()

    def generate_zoom_level(self, radius: int) -> int:
        """
        Calculate appropriate zoom level based on radius in km.
        
        Uses the formula: zoom = log2(earth_circumference_km / (radius_km * map_width_pixels)) - 1
        
        For web mapping systems, zoom levels typically range from 0 (world view) to 20+ (building level)
        Higher zoom = more zoomed in (smaller area)
        Lower zoom = more zoomed out (larger area)
        
        Args:
            radius: Search radius in kilometers
            
        Returns:
            int: Appropriate zoom level (0-20)
        """
        import math

        # Earth's circumference at equator in km
        earth_circumference_km = 40075.0
        
        # Typical map tile size (256px is standard)
        tile_size_pixels = 256
        
        # Calculate zoom level using standard web mercator formula
        # zoom = log2(earth_circumference / (radius * 2 * tile_size / map_width))
        # Simplified: we want the radius to fit comfortably in view
        
        # For a good view, we want the radius to be about 1/4 of the map width
        # So effective_radius = radius * 4
        effective_radius = radius * 4
        
        if effective_radius <= 0:
            return 16  # Default zoom for invalid radius
        
        # Calculate zoom level
        zoom = math.log2(earth_circumference_km / effective_radius)
        
        # Clamp to reasonable bounds (0-20)
        zoom = max(0, min(20, int(zoom)))
        
        return zoom

    def getNearbyPhotos(self, lat: float, lng: float, radius: int = 1000) -> PhotosResponse:
        params = {
            "lat": lat,
            "lng": lng,
            "zoomLevel": self.generate_zoom_level(radius),
            "join": "sequence",
            "orderBy": "id",
            "orderDirection": "desc"
        }

        '''
        API: https://api.openstreetcam.org/2.0/photo/?lat=-6.193932715082624&lng=106.84937065233879&zoomLevel=15&join=sequence&orderBy=id&orderDirection=desc 
        '''
        try:
            url = f"{self.base_url}/2.0/photo/"
            response = self.client.get(url, params=params)
            self._handle_error_response(response)
            return PhotosResponse(**response.json())
        except Exception as e:
            return f"getNearbyPhotos exception: {e}"
