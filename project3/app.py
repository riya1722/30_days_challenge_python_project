from flask import Flask, render_template, request
import re

app = Flask(__name__)

def validate_email(email):
    k = j = d = 0
    message = ""

    if len(email) < 6:
        return "❌ Invalid: Email length should be at least 6 characters"

    if not email[0].isalpha():
        return "❌ Invalid: First character must be a letter"

    if email.count('@') != 1:
        return "❌ Invalid: Email must contain exactly one '@'"

    if not (email[-4] == '.' or email[-3] == '.'):
        return "❌ Invalid: Email must end with a proper domain like .com or .in"

    if ".." in email or "__" in email or ".@" in email or "@." in email:
        return "❌ Invalid: Consecutive special characters like '..' or '__' are not allowed"

    username, domain = email.split('@')
    allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
    if domain not in allowed_domains:
        return f"❌ Invalid: Domain '{domain}' is not allowed"

    if username.isdigit():
        return "❌ Invalid: Username part cannot be digits only"

    for i in email:
        if i.isspace():
            k = 1
        elif i.isalpha():
            if i == i.upper():
                j = 1
        elif i.isdigit():
            continue
        elif i in ['_', '.', '@']:
            continue
        else:
            d = 1

    if k == 1:
        return "❌ Invalid: Email should not contain spaces"
    if j == 1:
        return "❌ Invalid: Email should not contain uppercase letters"
    if d == 1:
        return "❌ Invalid: Email contains invalid characters"

    # Optional: Final regex pattern check
    pattern = r'^[a-z][\w\._]*@[a-z]+\.[a-z]{2,3}$'
    if not re.fullmatch(pattern, email):
        return "❌ Invalid: Email does not match expected pattern"

    return "✅ You have entered a correct Email"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        email = request.form['email']
        result = validate_email(email)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
