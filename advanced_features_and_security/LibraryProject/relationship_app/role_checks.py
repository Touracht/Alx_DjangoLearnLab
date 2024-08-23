def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

def is_member(user):
    return user.groups.filter(name='Member').exists()