def isAlphaNumeric(x):
    return x.isalnum()

def isValidPrefixChar(y):
    if isAlphaNumeric(y) or y == '.' or y == '_' or y == '-':
        return True
    else:
        return False

def isValidDomainChar(z):
    if isAlphaNumeric(z) or z == '.' or z == '-':
        return True
    else:
        return False

def exactlyOneAt(email):
    if email.count('@') != 1:
        return False
    else:
        return True

def getPrefix(email):
    i = email.index('@')
    return email[:i]

def isValidEmail(email):
    if not exactlyOneAt(email):
        return False
    prefix = getPrefix(email)
    for char in prefix:
        if not isValidPrefixChar(char):
            return False
    return True

email = input()
print("This is a valid email:", isValidEmail(email))
