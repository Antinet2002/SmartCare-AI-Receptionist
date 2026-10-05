async function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                message: message,
                name: document.getElementById("name").value || "Guest"
            })
        });

        const data = await response.json();
        addMessage(data.response, "bot");
        speak(data.response);
    } catch (error) {
        addMessage("Something went wrong. Please try again.", "bot");
    }
}

function addMessage(text, sender) {
    const chat = document.getElementById("chat");
    const div = document.createElement("div");

    div.className = `${sender} message`;
    div.innerText = text;

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

async function bookAppointment() {
    const data = {
        name: document.getElementById("name").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        email: document.getElementById("email").value.trim(),
        service: document.getElementById("service").value,
        date: document.getElementById("date").value,
        time: document.getElementById("time").value
    };

    if (!data.name || !data.date || !data.time) {
        document.getElementById("bookingResult").innerText =
            "Please enter your name, date and time.";
        return;
    }

    try {
        const response = await fetch("/api/book", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("bookingResult").innerText =
            result.message;

        if (result.success) {
            speak("Your appointment has been successfully booked.");
        }
    } catch (error) {
        document.getElementById("bookingResult").innerText =
            "Unable to book the appointment.";
    }
}

function startVoice() {
    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Speech recognition is not supported in this browser.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-IN";
    recognition.interimResults = false;

    recognition.start();

    recognition.onresult = function(event) {
        const transcript =
            event.results[0][0].transcript;

        document.getElementById("message").value = transcript;
        sendMessage();
    };
}

function speak(text) {
    if (!("speechSynthesis" in window)) return;

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN";
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}

document.getElementById("message").addEventListener(
    "keypress",
    function(event) {
        if (event.key === "Enter") sendMessage();
    }
);
