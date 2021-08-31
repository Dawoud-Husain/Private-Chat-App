# Swift--Chat-2

This is a fully functional one to one private chat application featuring an SQL database for chat history, JWT login authcaiton 
and support for multiple users

The front end of the app is built using vue.js and the backend is built with python (flask)

Front End Information
    This application uses bootstrap for CSS styling 

    The vue app consists of four components, it is housed in the App.vue file
        - Users: responsible for listing all of the regesterd users 
        - Messages: renders messages
        - MessageInput: Input fourm for sending messages
        - Navbar: The navigation bar at the top


Backend Information:
    Main Python Packages used
        pusher: Python pusher libary used to acess the Pusher API
        Flask: framework used to build the web app
        Flask-JWT-Extended: used for JWT authentication
        Sqlalchemy: Used to create and acess the SQL chat database


    The database:
        The SQLite database consists of three models
        - USers: Contains all the users information
        - Channels: Creates and holds channels and stores the channels names into the database (prevents the need to create new channels for subsequent conversations)
        - Messages: Stores the chat messages (allows to reload the previous messages upon exiting)

        
