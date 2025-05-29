#
# export.py: export webmail in mbox format
#
import imaplib
import email
import mailbox
import getpass
import re
import os

def export_folder(folder):
    print(f"Exporting : {folder}")
    # === Step 2: Select your mailbox folder ===
    # 'INBOX' is usually the primary mailbox folder.
    status, messages = mail.select(folder)
    if status != "OK":
        print("Error selecting mailbox folder")
        print(f"check {folder}")
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

    mbox_file_name = folder + ".mbox"
    print(f"Exporting to: {mbox_file_name}")
    if os.path.isfile(mbox_file_name):
        os.remove(mbox_file_name)
    mbox = mailbox.mbox(mbox_file_name)

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
        print(f"Export completed successfully to {mbox_file_name}.")
    finally:
        # Always unlock the mailbox even if errors occur
        mbox.unlock()

# === Step 1: Connect to IMAP server ===
#IMAP_SERVER = 'export.imap.mail.yahoo.com'
#IMAP_SERVER = 'imap.free.fr'
IMAP_SERVER=input("Enter your IMAP SERVER: ")
IMAP_PORT = 993  # secure SSL port

# Prompt for credentials (or set them securely)
username = input("Enter your email address: ")
password = getpass.getpass("Enter your password (or app-specific password): ")

# Connect to the server using SSL and login
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(username, password)

print("Export started ...")
status, mailbox_list = mail.list()
for mailbox_item in mailbox_list:
    decoded_mailbox_item = mailbox_item.decode()
    mailbox_name_item = decoded_mailbox_item.split(" ")[-1]
    mailbox_name_item = mailbox_name_item.replace('"','')
    if mailbox_name_item != "Contacts":
        print(f"Exporting {mailbox_name_item} ... ")
        export_folder(mailbox_name_item)
    else:
        print(f"Skipped ${mailbox_name_item}")

# Logout from the IMAP server
mail.logout()
print("... export completed.")

