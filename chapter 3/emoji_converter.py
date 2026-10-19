# convert text based emotions into emojies
# basic version (no if, no loop)

message = input("Enter your message: ")
message = message.replace(":)", "😊")
message = message.replace(":(", "☹️")
message = message.replace(":D", "😃")
message = message.replace(";)", "😉")

print(message)