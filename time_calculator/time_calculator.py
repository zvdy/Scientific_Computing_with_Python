def add_time(start, duration, day = None):
  days_table = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  hours_table = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

  end_minute = ""
  end_hour = ""
  end_day = ""

  start_hour = start.split()[0].split(":")[0]
  start_minute = start.split()[0].split(":")[1]
  am_pm = False  
  if start.split()[1] == "PM":
      am_pm = True

  hour_duration = duration.split(":")[0]
  minute_duration = duration.split(":")[1]
  end_minute = str((int(start_minute) + int(minute_duration)) % 60)
  if len(end_minute) == 1:
      end_minute = "0" + end_minute
  hour_from_minutes = (int(start_minute) + int(minute_duration)) // 60
  total_interval_hour = int(hour_duration) + hour_from_minutes
  days = total_interval_hour // 24
  effective_hours = total_interval_hour % 24
  index_hour = hours_table.index(start_hour)

  while True:
    if effective_hours == 0:
      break

    index_hour += 1
    effective_hours -= 1

    if index_hour > 11:
      index_hour = 0
      if am_pm:
          days += 1 
      am_pm = not am_pm

  end_hour = hours_table[index_hour]

  if day is not None:
    effective_days = days % 7
    index_day = days_table.index(day.capitalize())
    while True:
      if effective_days == 0:
        break
      index_day += 1
      effective_days -= 1
      if index_day > 6:
        index_day = 0
    end_day =", " + days_table[index_day]
  new_time = end_hour + ":" + end_minute

  if am_pm:
      new_time += " PM"
  else:
      new_time += " AM"
  new_time += end_day

  if days == 1:
      new_time += " (next day)"
  elif days > 1:
      new_time += " (" + str(days) + " days later)"

  return new_time