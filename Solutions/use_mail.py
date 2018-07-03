from email_client import EmailClient

def send_spam(to):
      text = ("The best washing machines in town!\n\n"
              "Only now you can buy a new washing machine "
              "for the cheapest price ever. For more info "
              "go to www.best-washing-machines.com")
    frm = "master@best-washing-machines.com"
    subject = "Hi"

    client = EmailClient('smtp.server.com')
    client.send(from, to, subject, text)
