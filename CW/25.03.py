import re

# findall, finditer

text = '''
The following is a typical sequence of events that takes place when sender Alice transmits a message using a mail user agent (MUA) addressed to the email address of the recipient.[34]


Email operation
The MUA formats the message in email format and uses the submission protocol, a profile of the Simple Mail Transfer Protocol (SMTP), to send the message content to the local mail submission agent (MSA), in this case smtp.a.org.
The MSA determines the destination address provided in the SMTP protocol (not from the message header)—in this case, bob@b.org—which is a fully qualified domain address (FQDA). The part before the @ sign is the local part of the address, often the username of the recipient, and the part after the @ sign is a domain name. The MSA resolves a domain name to determine the fully qualified domain name of the mail server in the Domain Name System (DNS).
The DNS server for the domain b.org (ns.b.org) responds with any MX records listing the mail exchange servers for that domain, in this case mx.b.org, a message transfer agent (MTA) server run by the recipient's ISP.[35]
smtp.a.org sends the message to mx.b.org using SMTP. This server may need to forward the message to other MTAs before the message reaches the final message delivery agent (MDA).
The MDA delivers it to the mailbox of user bob.
Bob's MUA picks up the message using either the Post Office Protocol (POP3) or the Internet Message Access Protocol (IMAP).
In addition to this example, alternatives and complications exist in the email system:

Alice or Bob may use a client connected to a corporate email system, such as IBM Lotus Notes or Microsoft Exchange. These systems often have their own internal email format and their clients typically communicate with the email server using a vendor-specific, proprietary protocol. The server sends or receives email via the Internet through the product's Internet mail gateway which also does any necessary reformatting. If Alice and Bob work for the same company, the entire transaction may happen completely within a single corporate email system.
Alice may not have an MUA on her computer but instead may connect to a webmail service. bob@gmail.com, alice1@ukr.net, alice_11@yahoo.com
Alice's computer may run its own MTA, so avoiding the transfer at step 1.
Bob may pick up his email in many ways, for example logging into mx.b.org and reading it directly, or by using a webmail service.
Domains usually have several mail exchange servers so that they can continue to accept mail even if the primary is not available.
Many MTAs used to accept messages for any recipient on the Internet and do their best to deliver them. Such MTAs are called open mail relays. This was very important in the early days of the Internet when network connections were unreliable.[36][37] However, this mechanism proved to be exploitable by originators of unsolicited bulk email and as a consequence open mail relays have become rare,[38] and many MTAs do not accept messages from open mail relays.he Internet and do their best to deliver them. Such MTAs are called open mail relays. This was very important in the early days of the Internet when network connections were unreliable.[36][37] However, this mechanism proved to be exploitable by originators of unsolicited bulk email and as a consequence open mail relays have become rare,[38] and many MTAs do not accept messages from open mail relays.
'''

# findall ищет ВСЕ совпадения по шаблону и сохраняет их в списке
results = re.findall(r"[A-Z][a-z]+", text)
# Путь деда
new_results = []

for word in results:
    new_results.append('#' + word)
print(new_results)

# Быстрый путь

print(['#' + word for word in results])

# Задача - Фильтратор почты
emails_with_words = []
emails_words_number = []
emails_with_symbols = []
