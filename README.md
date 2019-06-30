# Olivier's Technical Test for Tails
Backend portion of test completed

## Requirements
* Python 3.5 or newer

## Installing
*Unless specified, all futher commands should be typed into your terminal*
1. Ensure you're running Python 3.5 or higher by entering `python --version`
2. Download this repository, and in your terminal, navigate to that folder.
3. Optional but recommended- setup a virtual environment for this app:
   * Check you've correctly navigated to the root of this app
   * Install a virtual environment by entering `python -m venv ./virtual_olivier`
   * Activate the environment by entering `source ./virtual_olivier/bin/activate`
   * At any time, deactivate by entering `deactivate`
4. Install site packages by entering `pip install -r requirements.txt`

## Running the app

1. Open terminal and navigate to the root of this project.
2. Launch the app `python -m easypostcode.postcode_distance`
3. In your web browser, view stores by entering "http://0.0.0.0:4000/view_stores"
4. In your web browser, view nearby stores with "http://0.0.0.0:4000/view_nearby_stores?postcode=XXX&radius=YYY"
    * Make sure to replace XXX with your postcode
    * Make sure to replace YYY with a radius in km

## Query stores from the terminal
    
1. Open terminal and navigate to the root of this project.
2. Enter the python shell by entering `python` into your terminal
3. Enter `from easypostcode import postcode_distance` to import the package
4. Query stores by entering `postcode_distance.find_radial_stores('XXX', YY)`
    * Make sure to replace XXX with your postcode
    * Make sure to replace YY with radius in km
5. The function will return a list of stores within the radius listed from north to south
    * Since stores have no primary keys, there is a risk of duplication
    * To mitigate, the return values are tuples in the form (StoreName, Postcode, (Longitude, Latitude))

## Testing

1. Open terminal and navigate to the root of this project
2. Enter `python tests/postcode_distance_test.py`