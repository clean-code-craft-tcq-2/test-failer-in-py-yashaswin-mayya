import test_alerter

alert_failure_count = 0


def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = test_alerter.network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report.
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1



