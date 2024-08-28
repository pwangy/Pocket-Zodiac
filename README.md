# ✨ Pocket Zodiac
A guide to the stars everywhere you go. 

Pocket Zodiac is an astrology app from an Eastern point of view. View your Chinese Zodiac sign, learn about the element particular to your year, unlock how it translates to your Western signs and vice versa.

## About this app
Pocket Zodiac is a full stack app built with React, Flask, and SQLAlchemy and best viewed on a small screen.
[Watch Demo](https://www.loom.com/share/a56048ce13a247ebb0ed3a0cdbd5445f)

Users can:
- [x] create an account via form or Google OAuth
- [x] Edit their personal details and delete their own account
- [x] View their personalized zodiac signs
- [x] Explore all Eastern and Western Zodiac signs and the five elements within the Chinese system.

This app makes use of the following libraries:
- Toastify
- Formik
- Yup
- React Router
- Scss
- Google OAuth
- JSON Web Token
- Marshmallow

## Pipeline
In the future, this app will...
- [ ] Incorporate the ability to consult the I Ching utilizing: [I-Ching](https://github.com/strobus/i-ching).
- [ ] Add an additonal birthdate to explore a friend or family member's zodiac.
- [ ] Full styles for a variety of screen widths.


## Getting up and running
Want to try the app on your own? Clone this repo and follow these steps.

Server
1. Navigate to the Server directory
2. Create your .env file in the root directory. It should contain:
   ```
   PIPENV_IGNORE_VIRTUALENVS=1
   FLASK_APP=app.py
   FLASK_RUN_PORT=5555
   GOAUTH_CID='Google OAuth Client ID'
   JWT_SECRET='your JWT secret'
   ```
   Replace the values of GOAUTH_CID and JWT_SECRET with your own keys.
   [Google Credentials](https://console.cloud.google.com/apis/credentials/oauthclient)

3. Install dependencies with `pipenv install` & `pipenv shell`
4. Start the server `python app.py`

Client
1. Navigate to the client directory
2. Install dependencies with `npm install`
3. Create an .env file which should live in the /client directory, it should contain your Goolge OAuth client id which you got in step 2 of the server instructions. Make sure that you name this variable `REACT_APP_GOOGLE_CLIENT_ID`.
4. Once your dependencies are done, start the frontend with `npm start`
---
### Credits
- Eastern sign descriptions: Reiko Chiba. Japanese Fortune Calendar, 2011, Tuttle Publishing, 9781462911271, 378dfbadd9e15eb3e9655dfffecbdae3 -- Anna’s Archive (pp. 9-10). Kindle Edition.

- Element descriptions: WHITE, SUZANNE. THE NEW ASTROLOGY FOR THE 21ST CENTURY: A Unique Blend of Chinese and Western Astrology (pp. 10-11). Suzanne White. Kindle Edition.

- Western sign descriptions: The Influence of the Zodiac Upon Human Life by Eleanor Kirk, 1894 - Public Domain.

- All icons (except the sparkle emoji) are from [flaticon](https://www.flaticon.com/) and were made by [Freepik](https://www.freepik.com) and [Nack_Thanakorn](https://www.flaticon.com/authors/nack-thanakorn).

---
### License : [MIT](./LICENSE.md)
