#!/usr/bin/env python3

class Date(object):
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

def displayDayOfTheWeek(daysInYear, daysInMonth, daysInWeek, date):
  """曜日を表示する"""
  dayOfTheWeeks = [chr(i) for i in range(65,65+26)]
  monthsInYear = daysInYear // daysInMonth
  remainDaysInYear = daysInYear - daysInMonth * monthsInYear
  if checkAdditionalMonth(date, daysInMonth, remainDaysInYear):
    monthsInYear += 1
   
  if date.month > monthsInYear or date.day > daysInMonth:
    print(-1)
    return
  pastDays = getPastDays(date, daysInYear, daysInMonth, remainDaysInYear)
  dayOfTheWeekIndex =  (pastDays - 1) % daysInWeek
  print(dayOfTheWeeks[dayOfTheWeekIndex])
  
def checkAdditionalMonth(date, daysInMonth, remainDaysInYear):
  """dateで渡された年が1月多くなるかどうかの判定"""
  if ((date.year * remainDaysInYear) // daysInMonth) != ((date.year - 1) * remainDaysInYear // daysInMonth):
    return True
  else:
    return False
  
def getPastDays(date, daysInYear, daysInMonth, remainDaysInYear):
  """0001-01-01からdateまでの経過日数を計算"""
  pastYears = (date.year - 1) if (date.year != 1) else 0
  remainDaysTotal = pastYears * remainDaysInYear
  pastMonths = (date.month - 1) if (date.month) != 1 else 0 
  pastDays = (pastYears * daysInYear - (remainDaysTotal % daysInMonth)) + (pastMonths * daysInMonth) + date.day
  return pastDays  


def main(argv):
  daysInYear, daysInMonth, daysInWeek  = [int(v) for v in argv[:3]]
  year, month, day = [int(v) for v in argv[3].split("-")]
  date = Date(year, month, day)
  displayDayOfTheWeek(daysInYear, daysInMonth, daysInWeek, date)
  return
