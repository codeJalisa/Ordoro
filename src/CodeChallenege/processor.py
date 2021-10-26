import dateutil.parser
import pytz

def distinct_emails(user_logs):
    emails = set()
    for user_log in user_logs:
        if user_log['email'] is not None:
            emails.add(user_log['email'])
    return list(emails)

def domain_counts(emails):
    domains = dict()
    for email in emails:
        email_split = email.split("@")
        domain = email_split[1]
        if not domain in domains:
            domains[domain] = 1
        else:
            domains[domain] += 1

    return domains

def april_logins(user_logs):
    emails = set()
    for user_log in user_logs:
        datetime = user_log['login_date']
        time = pytz.UTC.normalize(dateutil.parser.parse(datetime))
        if(4 == time.month):
            print(datetime)
            emails.add(user_log['email'])
    return list(emails)
    
