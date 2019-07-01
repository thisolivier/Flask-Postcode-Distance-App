# Olivier's Technical Test for Tails

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
*Unless specified, all futher commands should be typed into your terminal*
1. Open terminal and navigate to the root of this project.
2. Launch the app with `python -m easypostcode.postcode_distance`
3. In your web browser, view stores by entering "http://0.0.0.0:4000/view_stores"
4. In your web browser, view nearby stores with "http://0.0.0.0:4000/view_nearby_stores?postcode=XXX&radius=YYY"
    * Make sure to replace XXX with your postcode
    * Make sure to replace YYY with a radius in km

## Query stores from the terminal
*Unless specified, all futher commands should be typed into your terminal*
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
2. Enter `python tests/postcode_distance_tests.py`

# Notes for Humans at Tails

### *Tell us what test you completed (backend or full-stack)*

Backend

### *Tell us what you'd have changed if you'd have had more time?*

Personally, my main desire would be to setup the application with the python cfg and setup files, they look awesome. The essential next steps would be to add some more sanity checks for type safety, and to propagate issues when postcodes.io doesn't return a location better. I'd also have liked to separate out the models, I decided to keep things light and to spec (by using 3 in memory lists), but I feel like a pen and paper and some ERD's would lead to an elegant solution.

If the project was deemed sucsesful though, I'd also want to know how it was going to be used- whether it should have a restful API, what volume of requests it was going to receive, as these affect decisions like whether to add event loops or, well, make the API restful.

Finally, clearly I should have written the tests for the other components, if I'd been familiar with unit tests in Python I would have written them first.

### *What bits did you find the toughest? What bit are you most proud of? In both cases, why?*
The toughest was definately getting back into the Python and Flask way of setting things up- relative dependencies expecially. I also spent a lot of time trying to implement an asynchronous getter for the postcodes.io data- I learned a lot about codeobjects and async/await, but I should have looked at implementing a small database instead to store the stateful location data.

I'm most proud that it works, I find software that works very pleasing, especially if I helped make it. I'm also proud of learning a more robust Python styleguide too in the form of PEP-8, which I'm sure I've misinterpreted in parts, but it's made the code, particularly long lists of arguments, easy to read.

### *What's one thing we could do to improve this test?*
I actually think it's a great test. I might ask applicants to 'add an extra feature they think would complete the project', but that seems mean. Getting applicants to describe the apps biggest vulnerability or security risks feels like useful information to get from an applicant too.


## *Thanks very much for the challenge, if not an interview then I'd love a code review, Olivier*