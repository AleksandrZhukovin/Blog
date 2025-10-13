from split_settings.tools import optional, include


include(
    'components/main.py',
    optional('environments/local.py')
)
