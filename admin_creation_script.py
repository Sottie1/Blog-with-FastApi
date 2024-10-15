from .database import SessionLocal
from .models import User
from .auth import get_password_hash

def create_admin_user():
    db = SessionLocal()
    email = "admin@gmail.com"
    password = "adminpassword"
    username = "admin"

    # Hash the password
    hashed_password = get_password_hash(password)
    
    # Create admin user
    admin_user = User(
        email=email,
        username=username,
        password=hashed_password,
        is_admin=True  # Set the admin flag to True
    )

    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    print(f"Admin user created: {admin_user.username}")

# Run this function to create an admin user
if __name__ == "__main__":
    create_admin_user()
