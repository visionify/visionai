import typer
import time
from rich import print


# Auth app
auth_app = typer.Typer()

@auth_app.command('status')
def auth_status():
    '''
    Check login status

    Check the current login system.
    '''
    print('Print whether logged in or not')

@auth_app.command('login')
def login(
    token: str = typer.Option(..., help='Authenticate the app through token')
):
    '''
    Login with an application token.

    Get the auth token from our website
    '''
    print('Logging using the authorization token: {token}')

@auth_app.command('logout')
def logout():
    '''
    Logout from your session

    Get the auth token from our website
    '''
    print(f'Logging out of current session')

@auth_app.callback()
def callback():
    '''
    Authorization (logging in/out)

    Login and get authorization token etc.

    You can login/logout check authorization token with this.
    '''

if __name__ == '__main__':
    auth_app()
