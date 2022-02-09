import alerter

def network_alert_stub(celcius):
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    ok = float(175)
    if celcius < ok:
        print(f'ALERT: Temperature is {celcius} celcius')
        return 200
    else:
        return 500

alerter.alert_in_celcius(400.5)
alerter.alert_in_celcius(303.6)
print(f'{alerter.alert_failure_count} alerts failed.')
assert(alerter.alert_failure_count == 1)
print('All is well (maybe!)')