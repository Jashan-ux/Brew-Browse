A Flask web app that helps users discover cafes with details like operating hours, coffee options, and available amenities. Includes clickable Google Maps links for easy navigation.

Features
Displays a list of cafes with details (name, location, hours, amenities).
Clickable "Map Link" for each cafe to navigate via Google Maps.
User-friendly, responsive design using Bootstrap.
Technologies Used
Flask: Backend framework.
Bootstrap: Frontend styling.
CSV Integration: For managing cafe data.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/repo-name.git
Navigate to the project directory:
bash
Copy code
cd repo-name
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the app:
bash
Copy code
flask run
Usage
Open your browser and go to http://127.0.0.1:5000.
Browse the list of cafes and click on "Map Link" to view the location.
File Structure
app.py: The main Flask application.
templates/: HTML templates.
static/: CSS and JS files.
cafe-data.csv: Data source for cafes.
Contributing
Feel free to fork this repo, submit issues, or make pull requests!

License
This project is licensed under the MIT License.
