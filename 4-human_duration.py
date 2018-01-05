def format_duration(seconds):
    if seconds == 0:
        return 'now'
    dur_parts = [
        ('year', seconds // (86400 * 365)),
        ('day', (seconds // 86400) % 365),
        ('hour', (seconds // 3600) % 24),
        ('minute', (seconds // 60) % 60),
        ('second', seconds % 60)
    ]

    non_zero = 0
    for e in dur_parts:
        if e[1] > 0:
            non_zero += 1

    retval = ''
    for e in dur_parts:
        if e[1] > 0:
            retval += '{:d} {}{}'.format(e[1], e[0], 's' if e[1] > 1 else '')
            if non_zero > 2:
                retval += ', '
            elif non_zero == 2:
                retval += ' and '
            non_zero -= 1
    return retval






print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
