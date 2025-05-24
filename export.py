#
# export.py: export Yahoo Mail mbox
#
import imaplib
import email
import mailbox
import getpass

# === Step 1: Connect to Yahoo IMAP Server ===
IMAP_SERVER = 'export.imap.mail.yahoo.com'
IMAP_PORT = 993  # secure SSL port

# Prompt for credentials (or set them securely)
username = input("Enter your Yahoo email address: ")
password = getpass.getpass("Enter your password (or app-specific password): ")

# Connect to the server using SSL and login
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(username, password)

# === Step 2: Select your mailbox folder ===
# 'INBOX' is usually the primary mailbox folder.
status, messages = mail.select("FOLDER")
if status != "OK":
    print("Error selecting mailbox folder")
    print("check mail.select parameter and adapt mailbox.box parameter")
    mail.logout()
    exit(1)

# === Step 3: Search for all emails ===
status, data = mail.search(None, "ALL")
if status != "OK":
    print("Error searching mailbox.")
    mail.logout()
    exit(1)

# The returned data is a list containing a single byte string
# with space-separated email IDs
email_ids = data[0].split()

# === Step 4: Create an mbox file to export emails ===
mbox = mailbox.mbox("FOLDER.mbox")

# It’s a good idea to lock the mbox while we're writing
mbox.lock()

try:
    # Iterate over each email ID and fetch the message data
    for num in email_ids:
        typ, msg_data = mail.fetch(num, '(RFC822)')
        if typ != "OK":
            print(f"Failed to fetch message ID {num.decode()}")
            continue

        # msg_data is a list; the first element is a tuple where the second item is the raw email bytes
        raw_email = msg_data[0][1]

        # Parse the raw email into a Message object
        message = email.message_from_bytes(raw_email)

        # Add the message to our mbox
        mbox.add(message)

    # Flush any changes to disk
    mbox.flush()
    print("Export completed successfully to yahoo_emails.mbox")
finally:
    # Always unlock the mailbox even if errors occur
    mbox.unlock()

# Logout from the IMAP server
mail.logout()

