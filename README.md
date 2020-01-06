# Paywalled Django App & REST Example

This simple Django app demostrates keeping content behind a login & provides a simple REST API.

## Design

Super basic. Designed to keep users who are not logged in away from certain pages of a website & provides a simple REST API for CRUD operations.

### Notable Flaws

#### Testing

Currently, none of the code is tested via unit, integration or UI tests. In order to push this code to production, automated testing of some kind should be a part of CI/CD solutions.

#### JSON Array Vulnerability

Currently, when  calling `GET`on  `/secret` without any parameters, it returns a JSON array. This can be a [security vulnerability](https://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/). I chose to return data this way simply because it's easy for basic Django to serialize `Model`s into an array. However, in production this endpoint should return something like

```json
{
    "secrets": [...]
}
```

In order to avoid this vulnerability. It's not super simple to do with **just** Django's `serialize` module (requires some formating string non-sense, or making your model serializable), which I tried to stick with in this example.

## Usage

Run

```bash
python manage.py runserver
```

### REST API

Use your browser to navigate to

```bash
localhost:8000/rest
```

The first two lines are created simply using Django's templating system, loading in a single Secret for the code `1234`.

You can use the GET, POST, PUT and DELETE areas to perform the respective HTTP operations on Secrets. Secrets are just 4 digit integers.

Leaving the GET field empty and pressing `GET Secret` will get all Secrets. Providing a code will get only that secret.

POST will create a new secret.

PUT will change a Secret's code from the value in `From` to the value in `To`.

DELETE will delete a secret.

### Admin

The Django admin dashboard is available at

```bash
localhost:8000/admin
```

with the credentials

```bash
Username: admin
Password: adminadmin
```

Secrets are editable under the "Paywall" section.

### Paywall

Use your browser to navigate to

```bash
http://localhost:8000
```

You will be presented with a login page. Clicking "Attempt to view paywalled content" will redirect you to the login page. Any invalid username/password combinations will redirect you to the login page. Use the following login information to view the paywalled content:

```bash
Username: admin
Password: adminadmin
```

Upon a successful login, the paywalled content will appear. This page features two codes (`1234` and `5678`), each of which is loaded in a different way.

The code `1234` is loaded via Django's templating system. So, it is loaded when the page is loaded.

The code `5678` is loaded via a `fetch` request to the backend, which returns a JSON document containing the code `5678`. This request to the backend is authenticated and redirects to a login screen if the user sending the request is not authenticated. So, we can load authenticated content at any point.

This pretty much wraps up what the project does. It's just a super simple example of implementing a paywall in Django.

## Contact

Feel free to email questions and comments to [emma@emma.sh](mailto:emma@emma.sh).

## License

BTree is released under the MIT license. [See LICENSE](https://github.com/emma-foster/DjangoPaywall/blob/master/LICENSE) for details.
