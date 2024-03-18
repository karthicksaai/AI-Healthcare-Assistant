import subprocess

def send_emergency_sms(phone_number, message):
    try:
        # Replace "YourSMSApp" with the actual package name of your SMS app
        subprocess.run(["am", "start", "-n", "com.textra/.MainActivity", "--es", "address", phone_number, "--es", "sms_body", message], shell=True)
        print("Emergency SMS sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Example usage
if __name__ == "__main__":
    emergency_contact = "+91 6374532718"  # Replace with the actual phone number
    emergency_message = "Emergency! I need help."

    send_emergency_sms(emergency_contact, emergency_message)
