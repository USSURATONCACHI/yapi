from globals import db

class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(120), unique=True, nullable=False)
    auth_tokens = db.relationship('AuthToken', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class AuthToken(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    token      = db.Column(db.String(1024), nullable=False)
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expires_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<AuthToken {self.token}>'
