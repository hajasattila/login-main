import tkinter as tk
import smtplib

def send_email():
    # Create an SMTP object
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

    # Connect to the server using starttls() for secure connections
    smtp_obj.starttls()

    # Login to the server using your credentials
    smtp_obj.login('plangarjanosne1937@gmail.com', 'xXxPlangar|JanosnexXx1937')

    # Construct the email message
    message = """\
    From: Your Name <plangarjanosne1937@gmail.com>
    To: Receiver Name <hajaattila@gmail.com>
    Subject: Email Subject
    
    This is the email message.
    """

    # Send the email
    smtp_obj.sendmail('plangarjanosne1937@gmail.com','hajaattila@gmail.com', message)

    # Disconnect from the server
    smtp_obj.quit()


# Create the main window
root = tk.Tk()

# Create a button widget
button = tk.Button(master=root, text="Send email", command=send_email)
button.pack()

# Run the main loop
root.mainloop()
