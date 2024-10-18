import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request


# Initialize Flask app
app = Flask(__name__)

# Initialize SQLite database connection
db = SQL("sqlite:///exercises.db")


# Function to fetch exercise names based on the muscle group
def get(muscle_group):
    # Execute SQL query to get all exercise names for a specific muscle group
    exercise_names = db.execute(
        "SELECT exercise_name FROM exercises WHERE muscle_group = ?", muscle_group)

    # Extract exercise names from the query result
    names = [row["exercise_name"] for row in exercise_names]

    # Render the appropriate HTML template for the muscle group and pass the exercise names
    return render_template(f"{muscle_group}.html", names=names)


# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# Route for legs exercises
@app.route("/legs")
def legs():
    return get("legs")


# Route for chest exercises
@app.route("/chest")
def chest():
    return get("chest")


# Route for shoulders exercises
@app.route("/shoulders")
def shoulders():
    return get("shoulders")


# Route for arms exercises
@app.route("/arms")
def arms():
    return get("arms")


# Route for core exercises
@app.route("/core")
def core():
    return get("core")


# Route for back exercises
@app.route("/back")
def back():
    return get("back")


# Route for neck exercises
@app.route("/neck")
def neck():
    return get("neck")


# Route to handle fetching details of a specific exercise
@app.route("/fetch", methods=["GET", "POST"])
def fetch():
    if request.method == "POST":
        # Get the exercise name from the form submission
        exercise_name = request.form.get("exercise")

        # Validate input to ensure the exercise name is not empty
        if not exercise_name:
            return render_template("error.html", message="Exercise name cannot be empty."), 400

        # Query the database for details about the specific exercise
        exercise_details = db.execute(
            "SELECT description, muscle_group, youtube_link FROM exercises WHERE exercise_name = ?", exercise_name)

        # If no exercise details are found, return an error message
        if not exercise_details:
            return render_template("error.html", message="Exercise not found."), 404

        # Extract exercise details (description, muscle group, YouTube link) from the result
        exercise_detail = exercise_details[0]

        video_id = exercise_detail["youtube_link"].split('v=')[1]

        # Render the fetch.html template and pass the exercise details to it
        return render_template("fetch.html", video_id=video_id, description=exercise_detail["description"], muscle_group=exercise_detail["muscle_group"], exercise_name=exercise_name)
    else:
        # If the request is not POST, redirect the user to the previous page
        return redirect(request.headers.get("Referer", "/"))


# Main entry point to run the app
if __name__ == "__main__":
    app.run(debug=True)
