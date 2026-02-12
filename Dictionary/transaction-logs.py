# A commerce platform's payment system creates a log entry for every transaction. Each log entry is a string that contains three space-separated values: the sender's user ID, the recipient's user ID, and the transaction amount.
# Identify all users who have participated in a number of transactions greater than or equal to a given threshold.
# Each log entry is in the format: "sender_id recipient_id amount". "88 99 200"
# A user is considered "involved" in a transaction if they are the sender, the recipient, or both.
# If the sender_id and recipient_id are the same, it only counts as one transaction for that user.
# User IDs consist of digits only.
# The final list must be sorted in ascending numerical order and returned as strings.

def transaction_fraud(logs, threshold):
    users = {}
    
    for l in logs:

        l_list = l.split(" ")
        sen = l_list[0]
        rec = l_list[1]

        if sen == rec:
            users[sen] = users.get(sen, 0) + 1
        else:
            users[sen] = users.get(sen, 0) + 1
            users[rec] = users.get(rec, 0) + 1
    
    result = []
    for k, v in users.items():
        if v >= threshold:
            result.append(k)
            
    return result

print(transaction_fraud(["88 88 200", "88 87 200", "99 99 200", "88 77 200"], 2))

        
    









