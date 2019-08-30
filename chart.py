import matplotlib.pyplot as voting
party=["bjp","bsp","sp","tmc"]
votes=[10,4,3,2]
voting.axis()
voting.pie(votes,labels=party,radius=1.5,shadow="true",explode=[0.2,0,0,0],autopct='%0.1f%%',startangle=180)
voting.show()