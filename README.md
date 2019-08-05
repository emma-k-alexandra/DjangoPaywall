# Paywalled Django App

This simple Django app demostrates keeping content behind a login.



## Design

Super basic. Designed to keep users who are not logged in away from certain pages of a website.



## Usage

Run

```bash
python manage.py runserver
```

Use your browser to navigate to

```bash
http://localhost:8000
```

You will be presented with a login page. Clicking "Attempt to view paywalled content" will redirect you to the login page. Any invalid username/password combinations will redirect you to the login page. Use the following login information to view the paywalled content:

```bash
Username: admin
Password: admin
```

Upon a successful login, the paywalled content will appear. This page features two codes (`1234` and `5678`), each of which is loaded in a different way.

The code `1234` is loaded via Django's templating system. So, it is loaded when the page is loaded.

The code `5678` is loaded via a `fetch` request to the backend, which returns a JSON document containing the code `5678`. This request to the backend is authenticated and redirects to a login screen if the user sending the request is not authenticated. So, we can load authenticated content at any point.



This pretty much wraps up what the project does. It's just a super simple example of implementing a paywall in Django.



## Contact

Feel free to email questions and comments to [emma@emma.sh](mailto:emma@emma.sh).



## License

BTree is released under the MIT license. [See LICENSE](https://github.com/emma-foster/DjangoPaywall/blob/master/LICENSE) for details.
