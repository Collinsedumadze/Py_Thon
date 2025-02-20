hour_worked = int(input('How many hours have u worked: '))

rate = float(input('Rate per hour is : '))

weekly_gross_pay = hour_worked * rate * 1

monthly_gross_pay = hour_worked * rate * 4

yearly_gross_pay =  hour_worked * rate * 52

print(f"The grossly pay for the week is {weekly_gross_pay} "
      f", month is {monthly_gross_pay} and year is {yearly_gross_pay}")
            