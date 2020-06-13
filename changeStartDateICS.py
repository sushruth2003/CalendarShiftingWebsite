from ics import Calendar, Event, Alarms
import arrow
data = open("/Users/sushruth/Downloads/JusticeJune.ics", 'rb')
c = Calendar(data)
print(c.events)
