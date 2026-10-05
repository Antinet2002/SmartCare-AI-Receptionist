
# =========================================
# LOCAL AI RECEPTIONIST
# No OpenAI API
# No API Credits
# =========================================

SYSTEM_NAME = "SmartCare Solutions"


def get_ai_response(message, conversation_history=None):

    message = message.lower().strip()

    # -----------------------------------------
    # GREETINGS
    # -----------------------------------------

    if any(word in message for word in [
        "hello",
        "hi",
        "hey",
        "hii",
        "good morning",
        "good afternoon",
        "good evening"
    ]):
        return (
            "Hello! Welcome to SmartCare Solutions. "
            "How can I help you today?"
        )

    # -----------------------------------------
    # COMPANY
    # -----------------------------------------

    if any(word in message for word in [
        "company",
        "about",
        "smartcare",
        "who are you"
    ]):
        return (
            "SmartCare Solutions is a customer service company "
            "providing consultation, technical support and "
            "product demonstration services."
        )

    # -----------------------------------------
    # SERVICES
    # -----------------------------------------

    if any(word in message for word in [
        "service",
        "services",
        "what do you provide",
        "what can you do"
    ]):
        return (
            "We provide the following services:\n"
            "1. General Consultation\n"
            "2. Business Consultation\n"
            "3. Technical Support\n"
            "4. Product Demonstration"
        )

    # -----------------------------------------
    # WORKING HOURS
    # -----------------------------------------

    if any(word in message for word in [
        "timing",
        "time",
        "hours",
        "working hours",
        "open",
        "close"
    ]):
        return (
            "Our working hours are:\n"
            "Monday-Friday: 9:00 AM - 6:00 PM\n"
            "Saturday: 10:00 AM - 2:00 PM\n"
            "Sunday: Closed"
        )

    # -----------------------------------------
    # APPOINTMENT
    # -----------------------------------------

    if any(word in message for word in [
        "appointment",
        "book",
        "booking",
        "schedule",
        "consultation"
    ]):
        return (
            "Sure! I can help you with an appointment. "
            "Please provide your name, preferred date and time."
        )

    # -----------------------------------------
    # TECHNICAL SUPPORT
    # -----------------------------------------

    if any(word in message for word in [
        "technical",
        "technical support",
        "problem",
        "issue",
        "support"
    ]):
        return (
            "Our Technical Support service can help you "
            "with technical issues. Please describe your problem "
            "or contact our human receptionist for further assistance."
        )

    # -----------------------------------------
    # BUSINESS CONSULTATION
    # -----------------------------------------

    if any(word in message for word in [
        "business",
        "business consultation"
    ]):
        return (
            "We provide Business Consultation services. "
            "You can book an appointment for a detailed consultation."
        )

    # -----------------------------------------
    # CONTACT
    # -----------------------------------------

    if any(word in message for word in [
        "contact",
        "phone",
        "email",
        "reach"
    ]):
        return (
            "For assistance, please contact the SmartCare Solutions "
            "human receptionist."
        )

    # -----------------------------------------
    # THANK YOU
    # -----------------------------------------

    if any(word in message for word in [
        "thank",
        "thanks",
        "thank you"
    ]):
        return (
            "You're welcome! I'm happy to help."
        )

    # -----------------------------------------
    # GOODBYE
    # -----------------------------------------

    if any(word in message for word in [
        "bye",
        "goodbye",
        "see you"
    ]):
        return (
            "Thank you for contacting SmartCare Solutions. "
            "Have a great day!"
        )

    # -----------------------------------------
    # DEFAULT RESPONSE
    # -----------------------------------------

    return (
        "I'm here to help with SmartCare Solutions services, "
        "working hours and appointments. "
        "Please tell me what you need help with."
    )

