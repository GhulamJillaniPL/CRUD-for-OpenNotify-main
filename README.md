# ISS Tracking API

A FastAPI-based application that integrates with the Open Notify API to track the International Space Station (ISS) location and astronaut information in real-time.

## Features

- Real-time ISS location tracking
- Current astronauts in space information
- Direct mapping to Open Notify API endpoints
- Automatic data validation
- Interactive API documentation

## Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Internet connection for API access

## Installation on Linux

1. Update system packages:
   ```bash
   sudo apt update
   ```

2. Install Python and pip if not already installed:
   ```bash
   sudo apt install python3 python3-pip python3-venv
   ```

3. Create and navigate to project directory:
   ```bash
   mkdir iss-tracker
   cd iss-tracker
   ```

4. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Clone the repository (if using version control):
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a .env file (optional, default values are provided):
   ```bash
   touch .env
   ```

2. Add configuration if you want to override defaults:
   ```
   open_notify_url=http://api.open-notify.org
   api_title=ISS Tracking API
   api_version=v1
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. Access the application:
   - API Documentation: http://localhost:8000/docs
   - Alternative Documentation: http://localhost:8000/redoc

## API Endpoints

### Get ISS Location
- **Endpoint**: `GET /iss-now`
- **Description**: Returns current ISS location
- **Example Response**:
  ```json
  {
    "latitude": 45.12345,
    "longitude": -75.98765,
    "timestamp": "2024-01-01T12:00:00",
    "message": "success"
  }
  ```

### Get Astronauts
- **Endpoint**: `GET /astros`
- **Description**: Returns current astronauts in space
- **Example Response**:
  ```json
  {
    "message": "success",
    "number": 7,
    "people": [
      {
        "name": "Mark Vande Hei",
        "craft": "ISS"
      }
    ]
  }
  ```

## Example Usage

Using curl:

1. Get ISS location:
   ```bash
   curl http://localhost:8000/iss-now
   ```

2. Get astronaut information:
   ```bash
   curl http://localhost:8000/astros
   ```

Using Python requests:
```python
import requests

# Get ISS location
response = requests.get("http://localhost:8000/iss-now")
location = response.json()
print(f"ISS is at: {location['latitude']}, {location['longitude']}")

# Get astronaut information
response = requests.get("http://localhost:8000/astros")
astronauts = response.json()
print(f"There are {astronauts['number']} astronauts in space")
```

## Troubleshooting

1. If the server won't start:
   - Check if port 8000 is available
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

2. If API calls fail:
   - Check internet connection
   - Verify Open Notify API is accessible (try http://api.open-notify.org/iss-now.json directly)
   - Check response status codes and error messages

## Error Handling

The API includes comprehensive error handling:

- 200: Successful operation
- 500: Server error (includes detailed error message)

## Development

To contribute to the project:

1. Create a new branch for your feature
2. Make your changes
3. Run tests (when available)
4. Submit a pull request

## License

This project is licensed under the MIT License.
