from marshmallow import Schema, fields

# Luodaan käyttäjä-entiteetti
class User:

    def __init__(self, user_id, username, email, firstname, surname):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.surname = surname
        self.firstname = firstname

# Määritellään UserSchema Marshmallow'n avulla
class UserSchema(Schema):
    user_id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    sukunimi = fields.Str(required=True, attribute="surname")
    etunimi = fields.Str(required=True, attribute="firstname")

# Esimerkki käyttäjän luomisesta ja serialisoinnista
user1 = User(1, "example123", "example@example.com", "Test", "Testi")
user2 = User(2, "Matti", "Matti@Nykanen.com", "Matti", "Nykänen")
user3 = User(3, "Hämähäkkimies", "Peter@Parker.web", "Peter", "Parker")

# Luodaan UserSchema-luokan instanssi
user_schema = UserSchema()

# Kutsutaan dump-metodia user_schema-instanssilla ja annetaan sille user-objekti
user_data1 = user_schema.dump(user1)
user_data2 = user_schema.dump(user2)
user_data3 = user_schema.dump(user3)

# Tulostetaan kaikki käyttäjäolioiden datat
print("User 1:", user_data1)
print("User 2:", user_data2)
print("User 3:", user_data3)
