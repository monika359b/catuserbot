from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 12942748
    API_HASH = "07719ecad14e5172663a2f196fbdf22a"
    # the name to display in your alive message
    ALIVE_NAME = "Rohit"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://vlzamszf:F60zoy17J7b0YFk-exjZF0QcyjvEj3fc@peanut.db.elephantsql.com/vlzamszf"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJIBu4dvztOz-ZVjD64a7UUu7XZlMok1jF-Kdr0ahnSMZNzmSAThCU4prvGTAp0BBrPYXVGXKdw75yDGgBjfR_HvINlj3ete-wX9QRZpIG0MNd9A3nEEoTJrnUIkY-Z804NhAT-Ol8dxj-XiNPh5C0lloPtH1uIgPTaar0_1t6gYKDpPCcDkQXeVIKgtt0qpn3l7M8r2D4942e_9Dpbe6ZnEs6ewmeY_VcHgho9SF_odk0jvjAYqt-3rEC6X6j6fV4l9w1V9gj0gVsYZyTeqVn1WODY4IJLHAKTZAwUxKDne7lcLqktEdHJqXubvpkDHOjfYcvrLwPhi8hTod5NKIKEiyus="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5977732538:AAF4sqKoyB_7pOL7V7fVRHvWkCW8-FJuGNc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -646533288
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
