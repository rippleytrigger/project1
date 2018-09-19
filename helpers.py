def set_password(self, password):
  self.password_hash = generate_password_hash(password)

def check_password(password):
  return check_password_hash(password_hash, password)



def validate_password(password):
  if not password:
      raise AssertionError('Password not provided')

  if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
      raise AssertionError('Password must contain 1 capital letter and 1 number')

  if len(password) < 8 or len(password) > 50:
      raise AssertionError('Password must be between 8 and 50 characters')


def validate_username(username):
  if not username:
      raise AssertionError('No username provided')

  if User.query.filter(User.username == username).first():
    raise AssertionError('Username is already in use')

  if len(username) < 5 or len(username) > 20:
    raise AssertionError('Username must be between 5 and 20 characters')

  return username


def validate_email(email):
  if not email:
    raise AssertionError('No email provided')

  if not re.match("[^@]+@[^@]+\.[^@]+", email):
    raise AssertionError('Provided email is not an email address')

  return email