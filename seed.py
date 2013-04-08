"""
seed.py
"""
import model

db = model.connect_db()
ben_id = model.new_user(db, "ben@ben.com", "benpass123", "Ben")
task1 = model.new_task(db, "buy flowers for my wife", ben_id)
task2 = model.new_task(db, "dress rehearsal", ben_id)
