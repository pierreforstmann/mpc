"""
 cs2dhm.py: convert seconds in days, hours and minutes
"""
total_nb_sec=int(input("Number of seconds: "))
nb_days = total_nb_sec // (24*60*60)
nb_hours = (total_nb_sec - nb_days * (24*60*60)) // (60*60)
nb_minutes = (total_nb_sec - (nb_days * (24*60*60)) - (nb_hours * (60*60))) // 60
nb_sec = (total_nb_sec - (nb_days * (24*60*60)) - (nb_hours * (60*60)) - nb_minutes * 60) 
#
print("Total number of seconds:", total_nb_sec)
print(f"Duration [{nb_days}:{nb_hours:02d}:{nb_minutes:02d}:{nb_sec:02d}]")
