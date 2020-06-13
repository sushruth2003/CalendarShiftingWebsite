from datetime import datetime, date, timezone, timedelta
from icalendar import Calendar, Event, Alarm
import vobject
def differ_days(date1, date2):
    a= date1
    b = date2
    return(b-a).days
def getInput():
    print('year')
    year = int(input())
    print('month')
    month  =int(input())
    print('day')
    day = int(input())
    return datetime(year = year, month = month, day = day).date()
def main():
    data = open("/Users/sushruth/Downloads/JusticeJune.ics", 'rb')
    newStart = getInput()
    minDate =date(9999, 12, 31)
    startDateList = [];
    endDateList = [];
    eventSummaryList = [];
    eventDescriptionList = [];
    cal = Calendar.from_ical(data.read())
    for event in cal.walk('vevent'):
        start = event.get('dtstart').dt
        startDateList.append(start)
        
        if(start<minDate):
            minDate =start
        end = event.get('dtend').dt
        endDateList.append(end)
    newStartDateList = []
    newEndDateList = []
    #print("minDate", minDate)
    dayOffset = differ_days(minDate, newStart)
    #print("offset", dayOffset)
    size= len(startDateList)
    for i in range(0, size):
        startDate = startDateList[i]
        newStartDate = startDate + timedelta(days=dayOffset) # adds the number of offset days to generate a new start date
        endDate = endDateList[i]
        
        newEndDate = endDate + timedelta(days=dayOffset)
        newStartDateList.append(newStartDate)
        newEndDateList.append(newEndDate)
    for i in range(0, len(newStartDateList)):
        print('newStart', newStartDateList[i])
        print ('newEnd', newEndDateList[i])
    count = 0;
    newCal = Calendar()
    for component in cal.walk():
        if(component.name == 'VEVENT'):
            event.add('dtstart', newStartDateList[count])
            event.add('dtend', newEndDateList[count])
            count += 1
            
            event  = Event()
           
            event.add('summary', component.get('summary'))
            event.add('description', component.get('description'))
            event.add('dtstamp', component.get('dtstamp'))
            event.add('uid', component.get('uid'))
            
            #event.add('duration', component.get('duration'))
            #event.add('recurrence-id', component.get('recurrence-id'))
            event.add('sequence', component.get('sequence'))
            #event.add('rrule', component.get('rrule'))
            #event.add('rdate', component.get('rdate'))
            #event.add('exdate', component.get('exdate'))
            event.add('class', component.get('class'))
            event.add('created', component.get('created'))
            event.add('last-modified', component.get('last-modified'))
            event.add('location', component.get('location'))
            event.add('transp', component.get('transp'))
            
            newCal.add_component(event)
            
        if(component.name == 'VALARM'):
            alarm= Alarm()
            alarm.add('action', component.get('action'))
            alarm.add('trigger', component.get('trigger'))
            newCal.add_component(alarm)
    f = open('modifiedjune.ics', 'wb')
    f.write(newCal.to_ical())
    f.close()
    
    
    
    
main()
