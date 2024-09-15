import globals

class User(globals.db.Model):
    id          = globals.db.Column(globals.db.Integer, primary_key=True)
    name        = globals.db.Column(globals.db.String(120), unique=True, nullable=False)
    auth_tokens = globals.db.relationship('AuthToken', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class AuthToken(globals.db.Model):
    id         = globals.db.Column(globals.db.Integer, primary_key=True)
    token      = globals.db.Column(globals.db.String(1024), nullable=False)
    user_id    = globals.db.Column(globals.db.Integer, globals.db.ForeignKey('user.id'), nullable=False)
    expires_at = globals.db.Column(globals.db.DateTime)

    def __repr__(self):
        return f'<AuthToken {self.token}>'
