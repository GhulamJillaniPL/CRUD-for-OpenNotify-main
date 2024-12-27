import requests
from datetime import datetime
from ..config import settings
from ..models import ISSLocation, AstronautData, Astronaut

class ISSService:
    def __init__(self):
        self.base_url = settings.open_notify_url

    def get_iss_location(self) -> ISSLocation:
        """
        Retrieve current ISS location
        """
        try:
            response = requests.get(f"{self.base_url}/iss-now.json")
            response.raise_for_status()
            data = response.json()
            
            return ISSLocation(
                latitude=float(data['iss_position']['latitude']),
                longitude=float(data['iss_position']['longitude']),
                timestamp=datetime.fromtimestamp(data['timestamp']),
                message=data['message']
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get ISS location: {str(e)}")

    def get_astronauts(self) -> AstronautData:
        """
        Retrieve current astronauts in space
        """
        try:
            response = requests.get(f"{self.base_url}/astros.json")
            response.raise_for_status()
            data = response.json()
            
            return AstronautData(
                number=data['number'],
                people=[Astronaut(**person) for person in data['people']],
                message=data['message']
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get astronaut data: {str(e)}")