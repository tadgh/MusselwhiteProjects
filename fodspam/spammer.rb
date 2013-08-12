require 'win32ole'

fileLocation = ARGV[0]
outlook = WIN32OLE.new('Outlook.Application')
message = outlook.CreateItem(0)

message.Subject = 'Today\'s Menu'
message.HtmlBody = 'Today\'s menu can be found at ' + "<a href=\""+ ARGV[0].to_s + "\">This Link</a> "
#message.To = 'michael.gleeson@goldcorp.com;
#				alexander.pirie@goldcorp.com;
#				gary.graham@goldcorp.com;
#				kyle.barabash@goldcorp.com;
#				harvinder.reehal@goldcorp.com;
#				george.sanderson@goldcorp.com;
#				Michael.Cheung@goldcorp.com;
#				lionel.li@goldcorp.com;
#				lindsey.rocks@goldcorp.com;
#				octavia.bath@goldcorp.com;
#				patrick.donovan@goldcorp.com;
#				maryann.breton@goldcorp.com;
#				cynthia.harvey@goldcorp.com;
#				glady.saxton@goldcorp.com'
message.To = 'gary.graham@goldcorp.com'

message.Attachments.Add(ARGV[0].to_s, 1)
message.Send



