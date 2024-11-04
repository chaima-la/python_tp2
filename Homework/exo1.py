import re

def extract_emails (text): 
    

    matches = re.findall(r'\b[A-Za-z0-9._%+-]+(?:\[at\]|@)(?:[A-Za-z0-9.-]+|\[[^\]]+\])\.[A-Za-z]{2,}\b', text)


    normalized_emails = []
    for email in matches:
        
        normalized_email = email.replace('[at]', '@')
        
        normalized_email = re.sub(r'\[([^]]+)\]', r'\1', normalized_email)
        normalized_emails.append(normalized_email)

    return normalized_emails

# example
text = "Contact us at user[at]domain.com for more info.Also reach out to admin@website.co.uk or support@[web].com."
emails = print(extract_emails(text))
