import api
import processor as process

def main():
    data = api.getData()

    user_logs = data['data']
    emails = process.distinct_emails(user_logs)
    domains = process.domain_counts(emails)
    april_logins = process.april_logins(user_logs)
    
    api.postData(emails,domains,april_logins)

main()
