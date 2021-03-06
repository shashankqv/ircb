SECRET_KEY = 'some key'

DB_URI = 'sqlite:///ircb.db'

LOGGING_CONF = dict(
    version=1,
    formatters=dict(
        bare={
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "format": "[%(asctime)s][%(name)10s %(levelname)7s] %(message)s"
        },
    ),
    handlers=dict(
        console={
            "class": "logging.StreamHandler",
            "formatter": "bare",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    ),
    loggers=dict(
        network={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        bouncer={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        stores={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        dispatcher={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        irc={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        }
    ),
)
