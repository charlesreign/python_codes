"""my_data = {
    'name': 'Charles',
    'age': 12,
    'dob': 2002,
    'pob': 'Teshei'
}

print(my_data['dob'])"""

# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age',
# 'username', 'weapons', 'is_active' and 'clan'

userProfile = {
    'age': 12,
    'username': 'kiwi',
    'weapon': ['sword'],
    'is_active': True,
    'clan': 'zulu'
}

# 2 iterate and print all the keys in the above user.
print(userProfile.keys())

# 3 Add a new weapon to your user
userProfile.get("weapon").append("gun")
print(userProfile)

# 4 Add a new key to include 'is_banned'. Set it to false
userProfile.update({'is_banned': False})
print(userProfile)

# 5 Ban the user by setting the previous key to True
userProfile['is_banned'] = True
print(userProfile)

# 6 create a new user2 by copying the previous user and update the age value and username value.4

userProfile2 = userProfile.copy()
userProfile2['age'] = 20
userProfile2['username'] = 'cocoa'

# or

userProfile2.update({'age': 100, 'username': 'Timbo'})

print(userProfile2)
