import re

def RemoveEmojiAndWhiteSpace(text):
  if not isinstance(text, str): # Check if text is not a string
    text = str(text) # Convert text to a string if it is not
  # Remove emojis
  text = re.sub(r'[^\w\s,.]', '', text)
  # Remove newline characters
  text = text.replace('\n', ' ')
  # Remove extra spaces
  text = ' '.join(text.split())

  return text