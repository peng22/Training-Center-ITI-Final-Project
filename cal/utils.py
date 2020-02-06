from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Session

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter sessions by day
	def formatday(self, day, sessions):
		sessions_per_day = sessions.filter(start_time__day=day)
		d = ''
		for session in sessions_per_day:
			d += f'<li> {session.course} <br> {session.start_time} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, sessions):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, sessions)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter sessions by year and month
	def formatmonth(self, withyear=True):
		sessions = Session.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, sessions)}\n'
		return cal