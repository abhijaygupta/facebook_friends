import facebook



graph = facebook.GraphAPI(access_token='###', version='2.2')


# f = open('test.txt', 'r')
# str = f.read();
# x = str.find("14", 0);
# print x


friend_list = []

f = open('sharoon_friends.txt', 'r');
str = f.read();
#print str


x = 0
while (x != -1):
	x = str.find('\"id\":', x)
	if(x == -1):
		break;
	x = x + 5;
	y = str.find(",", x);
	tokenid =  str[x:y]
	#print tokenid
	if (tokenid.startswith('"') and tokenid.endswith('"')):
		tokenid = tokenid[1:-1]
	friend_list.append(tokenid)
	x = x + 1
f.close()

print(' ')



print friend_list
print len(friend_list)

for i in friend_list:
	person = graph.get_object(id=i)
	print person['name']
	print person['gender']
	print ' '

'''
friends = graph.get_connections(id='me', connection_name='friends')

print friends['name']


person = graph.get_object(id='1431065908')
print person


for friend in friends['data']:
	print friend['name']
	print friend['id']
	person = graph.get_object(id = friend['id'])
	print person
	#print person["gender"]

post = graph.get_object(id='post_id')
print(post['message'])

print "hey";
'''
