# Swift--Chat-2

Author: Dawoud Husain
Date: Aug 25 - 2021-present

This one to one private chat web application featuring an SQL database for chat history, JWT login authentication 
and support for multiple users

The front end of the app is built using vue.js and the backend is built with python's flask framework. The application uses an API called pusher allowing for the real-time data transfer between servers and clients.

Front End Information

    The vue app consists of four components, it is housed in the App.vue file
        - Users: responsible for listing all of the regesterd users 
        - Messages: renders messages
        - MessageInput: Input fourm (the bottem bar) for sending messages
        - Navbar: The navigation bar at the top

    This application uses the vue's axois libary for HTTP requests and bootstrap for CSS styling

To enable acess between the flask endpoints and the vue web application (connect backend to frontend), a proxy will be used (as seen in vue.config.js)

Backend Information:

    Main Python Packages used
        pusher: Python pusher libary used to acess the Pusher API
        Flask: framework used to build the web app
        Flask-JWT-Extended: used for JWT authentication
        Sqlalchemy: Used to create and acess the SQL chat database

    The database:
        The SQLite database consists of three models
        - Users: Contains all the users information
        - Channels: Creates and holds channels and stores the channels names into the database (prevents the need to create new channels for subsequent conversations)
        - Messages: Stores the chat messages (allows to reload the previous messages upon exiting)


