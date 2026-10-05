
from flask import Flask, render_template, request, jsonify

print("APP.PY STARTING")

from database import (
    init_db,
    save_customer,
    save_appointment,
    check_slot,
    get_appointments,
    save_conversation
)

from ai_service import get_ai_response


# -----------------------------------------
# FLASK APP
# -----------------------------------------

app = Flask(__name__)


# -----------------------------------------
# DATABASE INITIALIZATION
# -----------------------------------------

try:
    init_db()
    print("DATABASE INITIALIZED")
except Exception as e:
    print("DATABASE ERROR:", repr(e))


# -----------------------------------------
# HOME PAGE
# -----------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------------
# ADMIN PAGE
# -----------------------------------------

@app.route("/admin")
def admin():
    try:
        appointments = get_appointments()
        return render_template(
            "admin.html",
            appointments=appointments
        )
    except Exception as e:
        print("ADMIN ERROR:", repr(e))
        return "Unable to load admin page."


# -----------------------------------------
# AI CHAT API
# -----------------------------------------

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "").strip()
    name = data.get("name", "Guest")

    if not message:
        return jsonify({
            "response": "Please enter a message."
        }), 400

    try:

        print("USER MESSAGE:", message)

        response = get_ai_response(message)

        print("AI RESPONSE:", response)

        # Save conversation
        try:
            save_conversation(
                name,
                message,
                response
            )
        except Exception as db_error:
            print(
                "CONVERSATION SAVE ERROR:",
                repr(db_error)
            )

        return jsonify({
            "response": response
        }), 200

    except Exception as e:

        import traceback

        print("")
        print("========================================")
        print("              AI ERROR")
        print("========================================")
        print("ERROR:", repr(e))
        traceback.print_exc()
        print("========================================")
        print("            END AI ERROR")
        print("========================================")
        print("")

        return jsonify({
            "response":
                "Sorry, I'm having trouble right now. "
                "Please try again."
        }), 500


# -----------------------------------------
# APPOINTMENT BOOKING API
# -----------------------------------------

@app.route("/api/book", methods=["POST"])
def book():

    data = request.get_json(silent=True) or {}

    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    date = data.get("date")
    time = data.get("time")
    service = data.get("service")

    # Validate required fields
    if not name or not date or not time:

        return jsonify({
            "success": False,
            "message":
                "Name, date and time are required."
        }), 400

    try:

        # Check appointment slot
        if check_slot(date, time):

            return jsonify({
                "success": False,
                "message":
                    "This appointment slot is already booked."
            }), 409

        # Save customer
        save_customer(
            name,
            phone,
            email
        )

        # Save appointment
        save_appointment(
            name,
            phone,
            email,
            date,
            time,
            service
        )

        print(
            "APPOINTMENT BOOKED:",
            name,
            date,
            time
        )

        return jsonify({
            "success": True,
            "message":
                f"Appointment successfully booked for {name}."
        }), 200

    except Exception as e:

        import traceback

        print("")
        print("========================================")
        print("           BOOKING ERROR")
        print("========================================")
        print("ERROR:", repr(e))
        traceback.print_exc()
        print("========================================")

        return jsonify({
            "success": False,
            "message":
                "Unable to book the appointment right now."
        }), 500


# -----------------------------------------
# HEALTH CHECK
# -----------------------------------------

@app.route("/health")
def health():

    return jsonify({
        "status": "running",
        "message":
            "AI Receptionist server is running."
    })


# -----------------------------------------
# RUN SERVER
# -----------------------------------------

if __name__ == "__main__":

    print("")
    print("========================================")
    print("       SMARTCARE AI RECEPTIONIST")
    print("========================================")
    print("Server running at:")
    print("http://127.0.0.1:5000")
    print("")
    print("Admin page:")
    print("http://127.0.0.1:5000/admin")
    print("")
    print("Health check:")
    print("http://127.0.0.1:5000/health")
    print("========================================")
    print("")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )

