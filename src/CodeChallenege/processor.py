import dateutil.parser
import pytz

def distinct_emails(user_logs):
    emails = set()
    for user_log in user_logs:
        if user_log['email'] is not None:
            emails.add(user_log['email'].strip())
    return list(emails)

def domain_counts(emails):
    domains = dict()
    domains_with_multiple_users = dict()

    for email in emails:
        email_split = email.split("@")
        domain = email_split[1]
        if not domain in domains:
            domains[domain] = 1
        else:
            domains[domain] += 1
            domains_with_multiple_users[domain] = domains[domain]

    return domains_with_multiple_users

def april_logins(user_logs):
    emails = set()
    for user_log in user_logs:
        if user_log is not None and user_log['login_date'] is not None and user_log['login_date'] :
            datetime = user_log['login_date']
            time = pytz.UTC.normalize(dateutil.parser.parse(datetime))
            if(4 == time.month):
                emails.add(user_log['email'].strip())
    return list(emails)
    
