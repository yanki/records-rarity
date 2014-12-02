import mysql.connector
import sys
import random
from settings import *

#python insertRandVinyls.py num_vinyls_to_add

cnx = mysql.connector.connect(user='root', password='9apple',
            host='localhost', database='miyanki_records')
cursor = cnx.cursor()

adjectives = ['zesty','yawning','youthful','abandoned','able','absolute','adorable',\
'adventurous','accomplished','accurate','aching','acidic','acrobatic','wan','warlike',\
'warm','warmhearted','warped','wary','wasteful','watchful','waterlogged','watery','wavy',\
'vacant','vague','vain','valid','ugly','ultimate','unacceptable','unaware','uncomfortable',\
'uncommon','unconscious','understated','unequaled','tall','talkative','tame','tan','tangible',\
'tart','tasty','tattered','taut','tedious','teeming','sad','safe','salty','same','sandy',\
'sane','sarcastic','sardonic','satisfied','scaly','scarce','scared','scary','scented',\
'scholarly','scientific','scornful','radiant','ragged','rapid','rare','rash','raw','recent',\
'reckless','rectangular','quaint','qualified','mad','made-up','magnificent','majestic','major',\
'male','mammoth','married','marvelous','gargantuan','gaseous','general','generous','gentle','genuine',\
'giant','giddy','gigantic','fabulous','failing','faint','fair','faithful','damaged','damp','dangerous',\
'dapper','daring','darling','dark','dazzling','dead','deadly','deafening','dear','dearest','moist']
nouns = ['access','ache','act','address','aim','alert','answer','arrest','attack','auction','back',\
'bail','balance','balloon','ban','bandage','bank','bare','bargain','battle','beam','bear','beat','bend',\
'benefit','blame','blast','bleach','block','bloom','blow','board','bomb','bother','bounce','bow','box','bread',\
'break','breed','broadcast','brush','bump','burn','buy','cake','call','camp','care','catch','cause','challenge',\
'change','chant','charge','cheat','check','cheer','chip','claim','clip','cloud','clue','coach','color','comb',\
'comfort','contrast','control','cook','coop','copy','cost','count','cover','crack','crash','crate','credit',\
'crush','cure','curl','curve','cut','cycle','dam','damage','dance','deal','decay','decrease','delay','delight',\
'demand','design','dial','die','dislike','display','dive','divorce','dock','double','doubt','drain','draw','dream',\
'dress','drill','drink','drive','duck','dump','dust','dye','echo','email','end','escape','esteem','estimate','exchange',\
'excuse','exhibit','experience','eye','face','fall','favor','fax','fear','feel','fight','file','fill','film','finish',\
'fish','fix','flap','flash','float','flood','floss','flow','flower','fly','fold','fool','force','form','frame','freeze',\
'frown','function','garden','gaze','gel','glue','grate','grease','grill','grimace','grin','grip','guarantee','guard',\
'guess','guide','hammer','hand','handle','harm','harness','hate','head','heap','heat','help','hide','highlight','hike',\
'hit','hold','hop','hope','hose','hug','humor','hunt','hurry','ice','impact','inch','increase','influence','insult',\
'interest','iron','itch','jail','jam','joke','judge','jump','keep','kick','kiss','knit','knock','knot','label',\
'land','last','laugh','lead','leap','level','license','lie','lift','light','limit','link','load','loan','lock',\
'look','love','mail','make','man','march','mark','match','mate','matter','mean','measure','milk','mind','mine',\
'miss','mistake','moor','move','mug','nail','name','need','nest','notch','note','notice','number','object','offer',\
'oil','order','pack','pad','paddle','paint','park','part','pass','paste','pause','pat','pay','pedal','peel','pelt',\
'permit','phone','photograph','pick','pine','place','plan','plane','plant','play','plow','plug','point','poke','pop',\
'post','practice','praise','present','process','produce','promise','protest','pull','pump','punch','push','question',\
'quilt','quiz','race','rain','raise','rant','rate','reach','reason','record','reign','rent','repair','reply','report',\
'request','rhyme','ring','riot','risk','rock','roll','row','ruin','rule','run','sail','sand','saw','scare','scratch',\
'screw','search','season','sense','shampoo','shape','share','shelter','shock','shop','show','sign','signal','silence','sin',\
'sip','skate','sketch','ski','slice','slide','slip','smell','smile','smirk','smoke','snack','snow','sound','span','spot',\
'spray','sprout','squash','stain','stamp','stand','star','start','state','steer','step','sting','stop','store','storm',\
'stress','strip','stroke','struggle','study','stuff','stunt','suit','supply','support','surf','surprise','swap','swing',\
'swivel','tack','talk','taste','tear','tease','telephone','test','thunder','thought','tick','tie','time','tip','tire',\
'toast','touch','tour','tow','trace','track','trade','train','transport','trap','travel','treat','trick','trim','trust',\
'tug','turn','twist','upstage','use','vacuum','value','visit','voice','vote','walk','waltz','wake','watch','water','wave',\
'wear','whip','whisper','whistle','wick','wink','wire','wish','work','wrap','wreck','yawn','zone']
genres = ['Rock','Rap','Hip Hop','Alternative','Classical','Power Violence','Indie',\
'Electronic','Metal','World Music','Jazz','Blues','Pop','Reggae','Punk','R&B','County','Holiday']

adjective_len = len(adjectives)-1
noun_len = len(nouns)-1
genre_len = len(genres)-1

art = "http://www.psdgraphics.com/wp-content/uploads/2010/11/music-note.jpg"

def randartist():
    return adjectives[random.randint(0,adjective_len)] + " " +\
adjectives[random.randint(0,adjective_len)] + " " + nouns[random.randint(0,noun_len)]

def randalbum():
    return adjectives[random.randint(0,adjective_len)] + " " + nouns[random.randint(0,noun_len)]

for i in range(0, int(sys.argv[1])):
    add_vinyl = ("INSERT INTO records "
                "(artist, tracklist, genre, album, rarity, art, year) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    artist = randartist().title()
    tracklist = ""
    album = randalbum().title()
    genre = genres[random.randint(0,genre_len)]
    rarity = random.uniform(0.0,10.0)
    year = random.randint(1900,2015)
    data_vinyl = (artist, tracklist, genre, album, rarity, art, year)
    cursor.execute(add_vinyl, data_vinyl)
    cnx.commit()

cursor.close()
cnx.close()
