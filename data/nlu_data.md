## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:mood_affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:mood_deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:finddoctor
- please find the doctor
- can you find the doctor for me
- is doctors available
- what are all the doctor available for me
- Is any doctor available
- i had a problem please find the doctor
- i had a pain 


## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremly sad
- so sad

## intent:introduce
- how can you help
- can you help
- what service you offer
- can you help me
- please find my problem
- please help me
- help please

## intent:ask_name
- i am [poovarasan](name)
- my name is [poovarasan](name)
- [poovarasan](name) is my name


## intent:ask_problem
- i feel [sick](user_problem)
- i feeling [sick](user_problem)
- i am suffering from [fever](user_problem)
- suffered with [cold](user_problem)
- [ankle](user_problem) injury
- [head ache](user_problem) for some time
- i am affected with [cancer](user_problem)
 

## intent:ask_location
- doctors near me
- nearby doctors
- doctors near to my location
- doctors around [Chennai](location)
- [chennai](location) location
- i am from [chennai](location)
- [Chennai](location) is my location
- near to [chennai](location)
- around [chennai](location)
- [Chennai](location) is the location
- my zip code is [632602](location)
- i am from [632602](location)
- my zip [632602](location)
- my location is [632602](location)

## regex:zipcode
- [0-9]{5}(?:-[0-9]{4})?