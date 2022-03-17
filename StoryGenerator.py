import random

When=["A few years ago.,","Yesterday","Last night","A long time ago","On 20th Jan"]
Who=['A bunny','A lion',"A Man","A donkey","A zebra"]
Name=['Adur','leonol','Sancho','Kailash','Pranav']
Residence=['India','Korea','Japan','Russia','Phillipenes']
Went=['cinema','university','seminar','school','laundry']
Happened=['made a lot of friends','Eats a burger','Talked to god','read a book']

print(random.choice(When)+','+random.choice(Who)+','+'that lived in '+ random.choice(Residence)+', went to the '+ random.choice(Went)+' and '+ random.choice(Happened))