import globals

class User(globals.db.Model):
    id          = globals.db.Column(globals.db.String(120), primary_key=True)
    name        = globals.db.Column(globals.db.String(120), unique=True, nullable=False)
    auth_tokens = globals.db.relationship('OAuthToken', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class OAuthToken(globals.db.Model):
    token      = globals.db.Column(globals.db.String(1024), nullable=False, primary_key=True)
    user_id    = globals.db.Column(globals.db.String(120), globals.db.ForeignKey('user.id'), nullable=False)
    expires_at = globals.db.Column(globals.db.DateTime)

    def __repr__(self):
        return f'<OAuthToken {self.token}>'