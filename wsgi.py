from blog.app import create_app
from blog.models.database import db

app = create_app()


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("add-admin")
def add_admin():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="adminMy", email="admin@mail.ru", is_staff=True)

    db.session.add(admin)
    db.session.commit()

    print("done! add admin:", admin)


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", email="admin@mail.ru", is_staff=True)
    james = User(username="james", email="james@mail.ru")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("done! created users:", admin, james)


@app.cli.command("create-articles")
def create_articles():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import Articles
    django = Articles(name="Django", author="Jon", text="Django article text...")
    flask = Articles(name="Flask", author="Alex", text="Flask article text...")
    json = Articles(name="JSON:API", author="Vlad", text="JSON:API article text...")

    db.session.add(django)
    db.session.add(flask)
    db.session.add(json)
    db.session.commit()

    print("done! created articls:", django, flask, json)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
