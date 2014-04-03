"""
This class containts some frequently-used constants
"""

class Environment:
    QA = "qa"
    PRODUCTION = "production"
    LOCAL = "local"
    TEST = "test"


class Browser:
    FIREFOX = "firefox"
    INTERNET_EXPLORER = "ie"
    SAFARI = "safari"
    GOOGLE_CHROME = "chrome"
    PHANTOM_JS = "phantomjs"
    HTML_UNIT = "htmlunit"

    VERSION = {
        "firefox" : None,
        "ie" : ["8", "9", "10", "11"],
        "chrome" : None,
        "phantomjs" : None,
        "htmlunit" : None
    }

    LATEST = {
        "firefox": None,
        "ie": "11",
        "chrome": None,
        "phantomjs" : None,
        "htmlunit": None
    }


class State:
    NOTRUN = "NotRun"
    ERROR = "Error"
    FAILURE = "Fail"
    PASS = "Pass"
    SKIP = "Skip"
    BLOCKED = "Blocked"
    DEPRECATED = "Deprecated"
